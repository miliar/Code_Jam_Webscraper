#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a,b,c,d,e,f,g,h,i,j,k,l;
    freopen("input4.in","r",stdin);
    freopen("output4.txt","w",stdout);
    cin>>a;
    char str[3000];
    for(i=1;i<=a;i++)
    {
        int a[26],b[10];
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        cin>>str;
        for(j=0;j<strlen(str);j++)
        {
            a[str[j]-65]++;
        }


            b[0]=a['Z'-65];
            a['Z'-65]-=b[0];
            a['E'-65]-=b[0];
            a['R'-65]-=b[0];
            a['O'-65]-=b[0];

            b[2]=a['W'-65];
            a['T'-65]-=b[2];
            a['W'-65]-=b[2];
            a['O'-65]-=b[2];

            b[4]=a['U'-65];
            a['F'-65]-=b[4];
            a['O'-65]-=b[4];
            a['U'-65]-=b[4];
            a['R'-65]-=b[4];

            b[6]=a['X'-65];
            a['S'-65]-=b[6];
            a['I'-65]-=b[6];
            a['X'-65]-=b[6];
            b[1]=a['O'-65];
            a['N'-65]-=b[1];
            b[3]=a['R'-65];
            b[7]=a['S'-65];
            a['V'-65]-=b[7];
            a['N'-65]-=b[7];
            b[8]=a['G'-65];
            b[5]=a['V'-65];
            b[9]=a['N'-65]/2;
            cout<<"Case #"<<i<<": ";
            for(j=0;j<10;j++)
            {
                while(b[j]!=0)
                {
                    cout<<j;
                    b[j]--;
                }
            }
            cout<<"\n";
    }
    return 0;
}
