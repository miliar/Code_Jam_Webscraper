#include <bits/stdc++.h>
using namespace std;
#define lli long long int
#define infinite 0xffff
#define Min(a,b)  (((a)<(b))?(a):(b))
#define Max(a,b)  (((a)>(b))?(a):(b))
#define fr(i,j,s) for(i = j ; i < s ; i++)
#define ifr(i,j,s) for(i = j ; i >= s , i--)

int main(void)
{
    lli t,k,n,c,p,i,j;
    cin>>t;
    char s[100];
    fr(j,0,t)
    {
        cin>>s;
        n=strlen(s);
        c = 0;
        if(s[0] == '+')
            c=0;
        else
            c=1;
        fr(i,1,n)
        {
            if(s[i-1] == '+' && s[i] == '-')
            {
                c += 2 ;
            }
        }
        cout<<"Case #"<<(j+1)<<": "<<c<<endl;
    }   
    return 0;
}