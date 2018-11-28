#include<fstream>
#include<iostream>
#include<cmath>
#include<algorithm>

using namespace std;

long long gen(int base, int num)
 { int  temp;
   long long sum=0,a=1;
   while(num>0)
   { temp=num&1;
      if(temp) sum+=(temp*a);
      a*=base;
      num>>=1;
   }
   return sum;
 }

int isprime(long long num)
{ if(num%2==0) return 2;
  
  int i,cut=sqrt(1.0*num);
  for(i=3;i<=cut+1;i+=2)
   { if(num%i==0) return i;
   }
  return -1;
}

string binary(int num)
{ string s;
  int temp;
  while(num>0)
  { temp=num&1;
    s+=('0'+temp);
    num>>=1;
  }
  reverse(s.begin(),s.end());
  return s;
}

int main()
{ int i,j,temp,n,N,a,t;
  long long start,end,res,re[11];
  int count=0;
  
  ofstream output;
  output.open("output4.txt");
  
  ifstream input;
  input.open("C-small-attempt0.in");
  
  input>>n>>a>>N;
 // a=6; N=10;
  int out[11];
  start=pow(2,a-1)+1,end=pow(2,a-2)-1;
  output<<"Case #1:\n";
   for(i=0;i<=end;i++)
    { temp=start+(i<<1); 
	  cout<<temp<<"-"<<binary(temp)<<endl; 
      for(j=2;j<11;j++) out[j]=0;
      for(j=2;j<11;j++) re[j]=0;
      
      for(j=2;j<=10;j++)
       { res=gen(j,temp); re[j]=res;
         t=isprime(res);
         if(t!=-1) out[j]=t;
         else break;
       }
     /* if(j==11)
       { cout<<binary(temp)<<" ";
       
         for(j=2;j<=10;j++)
          { cout<<re[j]<<" ";
          }
          cout<<endl;
          
         for(j=2;j<=10;j++)
          { cout<<out[j]<<" ";
          }
          cout<<endl;
          
          
          count++;
       } */
       
       
        if(j==11)
       { output<<binary(temp)<<" ";
         for(j=2;j<=10;j++)
          { output<<out[j]<<" ";
          }
          output<<endl;
          count++;
       } 
       
       if(count==N) break;
    }
  
 
   return 0;
}
