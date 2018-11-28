#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
    int testCases;
    cin >> testCases;
    long long n;
    for(int testCaseNo=0;testCaseNo<testCases;testCaseNo++){
        cin >> n;
        long long current = n;
        vector<int> digits;
        if(n == 0){
            cout << "Case #" << testCaseNo+1 <<": INSOMNIA" << endl;
        }
        else {
            while(1){
                long long remainingNum = current;
                while(remainingNum > 0){
                    int rem = remainingNum % 10;
                    remainingNum = remainingNum / 10;
                    if (find(digits.begin(), digits.end(), rem) == digits.end())
                    digits.push_back(rem);
                    
                    
                }
                if(digits.size() == 10){
                    cout << "Case #" << testCaseNo+1 <<": " << current <<endl;
                    break;
                }
                else
                current += n;
            }
        }
    }
    return 0;
}