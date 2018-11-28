#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
  //freopen("A-large.in","rt",stdin);
  //freopen("sushilOutput.cpp","wt",stdout);
  long long t,j;cin>>t;
  for(j=1;j<=t;j++)
  {
    long long n,count=0,i=1,sum=0,num,k;
    cin>>n;
    long long ar[]={0,0,0,0,0,0,0,0,0,0};
    if(n==0){cout<<"case #"<<j<<": INSOMNIA"<<endl;}
    else
    {while(1)
     {
      num=i*n;
      long long digit;
      while(num!=0)
       {
         digit=num%10;
         num=num/10;
         if(digit==9)ar[9]=1;
         else if(digit==8)ar[8]=1;
         else if(digit==7)ar[7]=1;
         else if(digit==6)ar[6]=1;
         else if(digit==5)ar[5]=1;
         else if(digit==4)ar[4]=1;
         else if(digit==3)ar[3]=1;
         else if(digit==2)ar[2]=1;else if(digit==1)ar[1]=1;
         else ar[0]=1;
       }
       sum = ar[0]+ar[1]+ar[2]+ar[3]+ar[4]+ar[5]+ar[6]+ar[7]+ar[8]+ar[9];
       if(sum==10){cout<<"case #"<<j<<": "<<i*n<<endl;break;}
       else{i++;}
     }
    }
  }
 }
