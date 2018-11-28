#include<bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        string s;
        cin>>s;

        int i=0,e=s.size()-1,ans=0;

        while(e>=0 && s[e]=='+')e--;
        char ch = '#';
        for(i=0;i<=e;i++){
            if(s[i]!=ch){
                ans++;
                ch=s[i];
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }

    return 0;
}
