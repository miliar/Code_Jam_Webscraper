#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define sl(n) scanf("%lld",&n)
ll a[10];
int main()
{
    ifstream fin;
    ofstream fout("ans.txt");
    fin.open ("input.in");

    if(!fin.is_open())
    {
        fout<<"file error";
    }
    else
    {
        ll t;
        fin>>t;
        ll t1=t;
        while(t--)
        {
            string s;
            fin>>s;
            ll x=0,fl=0,i;
            int l=s.length();
            for(i=l-1;i>=0;i--)
            {
                fl=0;
                //fout<<i;

                if(s[i]=='-')
                {
                    x++;
                }
                else{
                       // i--;
                    continue;
                }
                while((s[i-1]=='-')&&(i>=0))
                {
                    i--;
                }
                while((s[i-1]=='+')&&(i>=0))
                {
                    if(fl==0)
                        x++;
                    fl=1;
                    i--;
                }
            }
            fout<<"Case #"<<t1-t<<": "<<x<<endl;
        }
    }
}

