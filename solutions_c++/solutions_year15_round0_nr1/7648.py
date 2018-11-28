#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("output.in", "w", stdout);
    int t, n, i, j, st[1010]={0}, l;
    char s[1010], ch;
    cin>>t;
    for(j=1; j<=t; j++){
        cin>>n;
        cin>>s;
        st[0]=s[0]-'0';
        l=0;
        for(i=1; i<=n; i++)
        {
            if((st[i-1]>=i)||((s[i]-'0')==0))
                st[i]=st[i-1]+(s[i]-'0');
            else
            {
                st[i]=i+(s[i]-'0');
                l+=i-st[i-1];
            }
            //cout<<st[i]<<" ";
        }
        cout<<"Case #"<<j<<": "<< l<<"\n";
    }
    return 0;
}
