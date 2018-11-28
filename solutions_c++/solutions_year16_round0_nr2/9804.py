#include <iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
#define lld long long int
char str[102];

void rotat(lld n)
{
    lld i,j;
    char stb[102];
    for(i=0;i<=n;i++)
    {
        stb[i]=str[i];
    }
    for(i=0;i<=n;i++)
    {
        if(stb[n-i] == '-')
            str[i]= '+';
        else
            str[i]= '-';
    }
}
int main()
{
    lld t,i,j,cnt,l,n;
    freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>t;
    for(l=1;l<=t;l++)
    {
        cin>>str;
        cnt=0;
        n = strlen(str);
        for(i=n-1;i>=0;i--)
        {
            //cout<<str<<"   ";
            if(str[i] != '+')
            {
                if(str[0] == '-')
                {
                    //cout<<"a\n";
                    rotat(i);
                    cnt++;
                }
                else
                {
                    //cout<<"b\n";
                    for(j=0;j<i&&(str[j]=='+');j++);
                    rotat(j-1);
                    rotat(i);
                    cnt+=2;
                }
            }
        }



        cout<<"Case #"<<l<<": ";
        cout<<cnt;
        cout<<endl;
    }
	return 0;
}
