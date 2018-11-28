#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int poly(long long n)
{
    char a[100];
    int i=0;
    for(i=0;i<100;i++)
    a[i]='\0';
    i=0;
    while(n!=0)
    {
               a[i++]=char((n%10)+int('0'));
               n/=10;
    }
    i=0;
    int len=strlen(a);
    for(i=0;i<(len/2);i++)
    {
                            if(a[i]!=a[len-i-1])
                            return 0;
    }
    return 1;
}
                          
    

int main()
{
    int TC=1,TN;
    freopen("C-small.in","rt",stdin);
    freopen("C-smOut.txt","wt",stdout);
    cin >> TN;cin.get();
    for(;TC<=TN;TC++)
    {
                     long long a,b,cnt=0;
                     cin >> a >> b;cin.get();
                     long long sqa=(long long)sqrt(a),sqb=(long long)sqrt(b);
                     for(long long k=sqa;k<=sqb;k++)
                     if(k*k>=a && k*k<=b)
                     if(poly(k))
                     if(poly(k*k))
                     cnt++;
                     cout << "Case #" << TC << ": " << cnt << endl;
    }
}
                     
                     
                     
                     
