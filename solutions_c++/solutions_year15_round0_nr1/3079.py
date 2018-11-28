#include <iostream>
#include <cstdlib>
#include <stdio.h>

using namespace std;
///CODEJAMM
int T,SMAX;
int sol,up;


int main()
{
freopen("A-large.in","r",stdin);
freopen("SDDDDDD1.out","w",stdout);
cin>>T;
for (int i=0;i<T;i++)
{
    up=0;
    sol=0;
    cin>>SMAX;
    char c;
    getchar();
    for (int j=0;j<=SMAX;j++)
    {
       c=getchar();
       int n=c-'0';
       if (j<=up)
           up+=n;
       else
       {
           sol+=j-up;
           up=j;
           up+=n;
       }
    }
    cout<<"Case #"<<(i+1)<<": "<<sol<<endl;
}
return 0;
}
