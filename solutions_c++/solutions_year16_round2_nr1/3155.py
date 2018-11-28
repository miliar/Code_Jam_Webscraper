#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,j,z;
    cin>>t;
    for(z=0;z<t;z++)
    {
        char s[2001];
        cin>>s;
        int hashi[26];
        int count[10];
        memset(count,0,sizeof(count));
        memset(hashi,0,sizeof(hashi));
        for(i=0;i<strlen(s);i++)
        {
            hashi[s[i]-65]++;
        }
        count[0]=hashi[25];
        count[2]=hashi[22];
        count[4]=hashi[20];
        count[6]=hashi[23];
        count[8]=hashi[6];
        count[1]=hashi[14]-hashi[22]-count[4]-count[0];
        count[3]=hashi[19]-hashi[6]-count[2];
        count[5]=hashi[5]-hashi[20];
        count[7]=hashi[18]-hashi[23];
        count[9]=(hashi[13]-count[1]-count[7])/2;
        cout<<"Case #"<<z+1<<": ";
        for(i=0;i<10;i++)
        {
            for(j=0;j<count[i];j++)
            {
                cout<<i;
            }
        }
        cout<<endl;
    }
}
