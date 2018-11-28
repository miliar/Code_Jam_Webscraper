#include<bits/stdc++.h>
using namespace std;
char s[1000100];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    int q,k,i,cnt;
    cin>>q;
    for(k=1;k<=q;k++)
    {
        cnt=0;
        scanf(" %s",s);
        strcat(s,"+");
        for(i=1;i<strlen(s);i++)
        {
            if(s[i]!=s[i-1])cnt++;
        }
        cout<<"Case #"<<k<<':'<<' '<<cnt<<endl;
    }

}
