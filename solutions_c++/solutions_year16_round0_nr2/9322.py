#include <iostream>
#include <stdio.h>
#include <unistd.h>
using namespace std;
int T;


int main()
{   freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        string s;
        cin>>s;
        int ans=0;
        for(int i=1;i<s.size();i++)
            if(s[i]!=s[i-1])ans++;
        if(s[s.size()-1]=='-')ans++;
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }

    return 0;
}
