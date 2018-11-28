#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int poly(int n)
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
    freopen("C-sm1.txt","rt",stdin);
    freopen("C-smOut.txt","wt",stdout);
    cin >> TN;cin.get();
    for(;TC<=TN;TC++)
    {
                     int a,b,cnt=0;
                     cin >> a >> b;cin.get();
                     for(int k=a;k<=b;k++)
                     if(int(sqrt(k))==sqrt(k))
                     if(poly(k))
                     if(poly(int(sqrt(k))))
                     cnt++;
                     cout << "Case #" << TC << ": " << cnt << endl;
    }
}
                     
                     
                     
                     
