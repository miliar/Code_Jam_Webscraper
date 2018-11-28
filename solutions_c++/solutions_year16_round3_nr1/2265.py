#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int nums[26];

void solve(int n,vector<vector<char>> &result){
    //int sum = accumulate(nums,nums + n -1,0);
    int remain = n;
    while(remain != 0){
        vector<char> currresult;
        int maxIndex = max_element(nums,nums+n) - nums;
        currresult.push_back('A'+maxIndex);
        nums[maxIndex] --;
        if(nums[maxIndex] == 0) remain --;
        int nextmaxindex = max_element(nums,nums+n) - nums;
        if(!(nums[nextmaxindex] == 1 && remain == 2)){
            currresult.push_back('A' + nextmaxindex);
            nums[nextmaxindex] --;
        }
        if(nums[nextmaxindex] == 0) remain --;
        result.push_back(currresult);
    }
}

int main()
{
    int t;
    cin>>t;
    int line = 1;
    while(t--){
        int n;
        cin>>n;
        for(int i = 0;i<n;i++)
            cin>>nums[i];

        cout<<"Case #"<<line<<": ";
        vector<vector<char>> result;
        solve(n,result);
        for(auto &row:result){
            for(auto ele:row)
                cout<<ele;
            cout<<" ";
        }
        cout<<endl;
        line ++;
    }
    return 0;
}

