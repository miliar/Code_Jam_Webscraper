/*
    anick saha
*/
 

#include<iostream>
#include<cstdio> 
#include<vector> 
using namespace std;
 
 
#define MAX(A,B) (A)>(B)?(A):(B)
#define MIN(A,B) (A)<(B)?(A):(B)
#define lcm(a,b)  { return a*b/gcd(a,b);  }
 
 
typedef long long ll;
typedef long double ld;
typedef long long unsigned int llu;
 
 
 

#define M 1000000007


long long reverse(long long x)
{
     long long r=0,d;
     while(x>0)
     {
               d=x%10;
               r=r*10+d;
               x=x/10;
     }
     return r;
}
     
bool palin(long long x)
{
     long long y=reverse(x);
     if(x==y)
     return 1;
     return 0;
}

vector<long long> foo;

void pre()
{
     for(long long i=1;i<10000001;i++)
     {
             if(palin(i))
             {
                                
                                long long j=i*i;
                                if(palin(j))
                                foo.push_back(j);
                                
             }
     }
}
     
int main()
{
 
	 int t,k=0,cases=0,c1,c2;
	 
	 pre();
     
     	
	 long long j,a,b;
     
	 
     
	 scanf("%d",&t);
     
     for(cases=1;cases<=t;cases++)
     {
               printf("Case #%d: ",cases);
               
			   scanf("%lld%lld",&a,&b);
               
			   if(a>foo[foo.size()-1])
               
			   {printf("0\n");continue;}
               
			   if(b>foo[foo.size()-1])
               b=foo[foo.size()-1];
               
			   for(int i=0;i<foo.size();i++)
               {
                       if(foo[i]>=a)
                       {c1=i;
                       break;}
               }
               
			   for(int i=0;i<foo.size();i++)
               {
                       if(foo[i]<=b)
                       c2=i;
               }
               
			   printf("%d\n",c2-c1+1);        
     
     }
     return 0;
}

