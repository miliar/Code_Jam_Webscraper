#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<stdio.h>
#include<set>
#include<cmath>

using namespace std;

int main() {
    freopen("exam.in","r",stdin);
    freopen("exam.out","w",stdout);
    int n,T;
    string str;
    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        scanf("%d",&n);
        cin>>str;
        int ans=0,p=0;
        for(int i=0; i<str.size(); i++)
        {
            if(str[i]=='0') continue;
            if(p<i) { ans+=i-p; p=i; }
            p+=str[i]-'0';
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
