#include<iostream>
#include<map>
#include<math.h>
#include<stdlib.h>
#include<string>
using namespace std;
/*int pal(unsigned long long x) 
{int i,j,flag=0;
string strn=to_string(x);
int len=strn.length();
for(i=0,j=len-1;i<=(len/2);++i,--j)
{
if(strn.at(i)==strn.at(j))
flag=1;
else {flag=0; break;}
}
if(flag)
return 1;
else return 0;
}*/
int main()
{map<int,int>x;
         //for(int i=1;i<=10000;i++) x[i]=0;
          unsigned long long int a1[39]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
         //for(int i=0;i<100;i++)
        // x[a1[i]]=i+1;
        freopen("input.txt","r",stdin);
         freopen("output.txt","w",stdout);
         int t;
        cin>>t;
        for(int l=1;l<=t;l++)
        {unsigned long long a,b;
        cin>>a>>b;
         int c=0;
        for(int i=0;i<39;i++)
        {       if(a1[i]>=a&&a1[i]<=b)
                    c++;
        }
        cout<<"Case #"<<l<<": "<<c<<endl;
        }
return 0;
}
