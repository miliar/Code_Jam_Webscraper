#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;
int main(){
    int testCase;scanf("%d",&testCase);
    int plus=0;
    int minus=1;
    ofstream fout;
    fout.open("B.out");
    string s;
    for(int t=1;t<=testCase;t++){
        cin>>s;
        int dp[101][2];
        if(s[0]=='+')
        {
            dp[0][plus]=0;
            dp[0][minus]=1;
        }
        else{
            dp[0][plus]=1;
            dp[0][minus]=0;
        }
        for(int i=1;i<s.length();i++){
            if(s[i]=='+'){
                dp[i][plus]=min(dp[i-1][plus],dp[i-1][minus]+1);
                dp[i][minus]=min(dp[i-1][plus]+1,dp[i-1][minus]+2);
            }
            else{
                dp[i][plus]=min(dp[i-1][minus]+1,dp[i-1][plus]+2);
                dp[i][minus]=min(dp[i-1][minus],dp[i-1][plus]+1);
            }
        }
        fout<<"Case #"<<t<<": "<<min(dp[s.length()-1][minus]+1,dp[s.length()-1][plus])<<endl;
    }
    fout.close();
    return 0;
}

