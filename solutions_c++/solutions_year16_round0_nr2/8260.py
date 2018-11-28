#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input5.in","r",stdin);
    freopen("output5.txt","w",stdout);
    long long int a,b,c,d,e,f,g,h,i,j,k,l;
    cin>>a;
    char str[1000];
    for(j=1;j<=a;j++)
    {
        cin>>str;
        l=strlen(str);
        c=0;
        for(i=0;i<l;i++)
        {
            if(str[i]=='-')
            {
                if(i==0)
                    c++;
                else if(str[i-1]=='+')
                    c+=2;
            }
        }
        cout<<"Case #"<<j<<": "<<c<<"\n";
    }
    return 0;
}
