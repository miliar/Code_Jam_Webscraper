#include <bits/stdc++.h>
#define ll long long
#define modl 1000000007

using namespace std;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        int count=0;
        string s;
        cin>>s;
        for(int i=1;i<s.length();i++){
            if(s[i]!=s[i-1])count++;
        }
        if(s[s.length()-1]=='-')count++;
        printf("Case #%d: %d\n",t,count);
    }
    return 0;
}
