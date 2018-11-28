#include<iostream>
#include<cmath>
#include<cstdio>
#include<queue>
#include<stack>
#include<vector>
#include<climits>
using namespace std;
#define mx 100001
#define read(x) scanf("%d",&x)
#define MOD 1000000007
typedef pair<int,int> pr;
typedef long long int ull;


ull getDivisor(ull num)
{
  for(ull a=2;a*a<=num;a++)
    if( (num%a)==0)
      return a;

    return -1;
}

void printbase2(ull num)
{
   if(num)
    {
      printbase2(num/2);
      printf("%lld",num&1);
    }
 }

 
 int main()
 {
   
   int t,i,j,k,len,req,tt;
   
   read(t);
   for(tt=1;tt<=t;tt++)
   {
      read(len);read(req);
      printf("Case #%d:\n",tt);

      ull num =(1<<(len-1))+1;
      for(;req>0;num+=2)
      {

         vector <ull> v;
         ull base;
         int flag=true;
         //cout<<num<<endl;
         for(base=2;base<=10;base++)
         {

           ull basenum=0;
           ull curr=1;
           for(i=0;i<len;i++)
           {
             int bit= num&(1<<i);
             if(bit)
              basenum+=curr;
            curr*=base;
           }
          
          ull di=getDivisor(basenum);
          if(di==-1)
          {
             flag=false;
             break;
          }
          v.push_back(di);
         }

         if(flag)
         {
           req--;
           //cout<<num<<" ";
           printbase2(num);
           for(i=0;i<9;i++)
            printf(" %lld",v[i]);
          cout<<endl;
         } 
      }

   }
   
   

   
   

 }