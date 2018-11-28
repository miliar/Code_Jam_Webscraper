#include<iostream>
#include<fstream>
using namespace std;
#define ll long long

int main()
{
    ofstream pno;
    pno.open("ans.text");
    ll int i,t,ans,j,k,n,smax;
    cin>>t;
    j=0;
    while(t--)
    {
        j=j+1;
        cin>>smax;
        char s[smax+2];
        cin>>s;
        k=s[0]-'0';
        ans=0;
        smax++;
        for(i=1;i<smax;i++)
        {
            if(k<i)
                {ans=ans+(i-k);k=k+i-k;}
                k=k+s[i]-'0';
        }
        pno<<"Case #"<<j<<": "<<ans<<endl;

    }
}

