#include<iostream>
#include<string>
#include<vector>
#include<climits>
#include<cmath>

using namespace std;

int len = 0;

bool    chk(vector<vector<int> > &ref, vector<int> &cnt, vector<int> &arr, int cntS){
    //cout << "@ " << cntS << endl;
    //for(int i = 0; i < 10; i ++) cout << cnt[i] << " ";
    //cout << endl;
    //for(int i = 0; i < 26; i ++) cout << (char)('A' + i) << "-" << arr[i] << " ";
    //cout << endl;
    if(cntS == len)  return true;
    if(cntS > len)   return false;
    for(int i = 0; i < 10; i++){
        bool flag = true;

        for(int j = 0; j < 26; j++){
            if(ref[i][j] && ref[i][j] > arr[j]){
                flag = false;
                break;
            }
        }

        if(flag == false)   continue;

        for(int j = 0; j < 26; j++){
            if(ref[i][j] != 0){
                //cout << (char)('A' + j);
                arr[j] -= ref[i][j];
                cntS += ref[i][j];
            }
        }
        //cout << "Call @ " << i << endl;
        cnt[i]++;
        if(chk(ref, cnt, arr, cntS) == true)    return true;
        cnt[i]--;
        for(int j = 0; j < 26; j++){
            if(ref[i][j] != 0){
                arr[j] += ref[i][j];
                cntS -= ref[i][j];
            }
        }
    }
    return false;
} 

int main(){
    int t;
    cin >> t;
    for(int itrS = 0; itrS < t; itrS++){
        string str;
        cin >> str;
        len = str.length();
        vector<int> arr(26, 0);
        for(int i = 0; i < str.length(); i++){
            arr[str.at(i) - 'A']++;
        }

        vector<vector<int> > ref(10, vector<int>(26, 0));
        string nums[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
        for(int i = 0; i < 10; i++){
            for(int j = 0; j < nums[i].length(); j++)
                ref[i][nums[i].at(j) - 'A']++;
        }

        vector<int> cnt(10, 0);
        //for(int i = 0; i < 10; i++) cout << cnt[i] << " ";
        chk(ref, cnt, arr, 0);
        cout << "Case #" << itrS + 1 << ": ";
        for(int i = 0; i < 10; i++) 
            for(; cnt[i] > 0; cnt[i]--)    cout << i;
        cout << endl;
    }
    return 0;
}
