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
    lli t,k,n,c,p,i,j,start,end;
    cin>>t;
    char s[3003],ss[1000];
    fr(j,0,t)
    {
        cin>>ss;
        n=strlen(ss);
        c = 0;
        start = 1500 ;
        end = 1501;
        s[end] == 'A';
        fr(i,0,n)
        {
            if(ss[i] >= s[start+1] )
            {
                s[start--] = ss[i] ;
            }
            else
            {
                s[end++] = ss[i];
            }
        }
        s[end]= '\0';
        printf("Case #%lld: %s\n",j+1,&s[start+1]);
    }   
    return 0;
}