#include<iostream>
#include<cmath>
#include<cstdio>
#include<stack>
#include<vector>
#include<climits>
using namespace std;
#define mx 100001
#define read(x) scanf("%d",&x)
#define MOD 1000000007
typedef long long int ull;


 int fn(ull n,int bits)
 {
     while(n)
     {
        bits|=1<<(n%10);
        n/=10; 
     }
     return bits;
 }
 
 int main()
 {
 	int t,i,bits,target=(1<<10)-1;
 	read(t);
  ull n,num;
  for(i=1;i<=t;i++)
  {
    cin>>n;
    printf("Case #%d: ",i);
    if(!n){printf("INSOMNIA\n");continue;}
    
    num=n;
    bits=0;
    bits=fn(num,bits);

    while(bits!=target)
    { 
        num+=n;
        bits=fn(num,bits);
    } 
    printf("%lld\n",num);
    }
 }