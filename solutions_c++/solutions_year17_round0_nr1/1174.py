#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <set>
#include <numeric>
#include <cmath>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <queue>
#include <numeric>
#include <iomanip>
#define ll long long
using namespace std;
int testCase;
bool check(string &s){
    for(int i=0;i<s.length();i++)if(s[i]=='-')return false;
    return true;
}
int main(){
    freopen("/Users/papaya0033/Desktop/A-small-attempt0.in","r",stdin);
    freopen("/Users/papaya0033/Desktop/a.out","w",stdout);
    scanf("%d",&testCase);
    string s;
    for(int t=1;t<=testCase;t++){
        int r; cin>>s>>r;
        int cnt=0;
        for(int i=0;i<s.length()-r+1;i++){
            if(s[i]=='-'){
                cnt++;
                for(int j=i;j<i+r;j++){
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
            }
        }
        printf("Case #%d: ",t);
        if(check(s))printf("%d\n",cnt);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
