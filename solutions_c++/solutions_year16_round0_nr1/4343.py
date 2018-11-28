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
    int s[10];
    fr(j,0,t)
    {
        cin>>n;
        if(n == 0)
        {
            cout<<"Case #"<<(j+1)<<": INSOMNIA"<<endl;
            continue;
        }
        fr(i,0,10)
        {
            s[i] = 0 ;
        }
        i = 1 ;
        while(1)
        {
            k = i * n ;
            while( k != 0)
            {
                s[k%10] = 1 ;
                k /= 10;
            }
            fr(p,0,10)
            {
                if(s[p] == 0 )
                    break;
            }   
            if(p == 10)
            {
                cout<<"Case #"<<(j+1)<<": "<<(i*n)<<endl;
                break;
            }
            i++;
        }
    }   
    return 0;
}