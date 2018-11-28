#include <iostream>

using namespace std;

int  main()
{
 long t,ankur=1;
 cin>>t;
 while(t--)
 {
  long long n,raja=1;
  cin>>n;
  if(n==0)
  { 
    cout<<"Case #"<<ankur++<<": "<<"INSOMNIA"<<endl;
  }
  else
  {
   long a[10];
   for(long i=0;i<=9;i++)
   {
    a[i]=0;
   }

   bool flag = true;

   do
   {
    long long m = n*raja++; 
    
   
    //cout<<m<<endl;
    while(m)
    {
     //cout<<n<<" "<<m<<" "<<m%10<<endl;
     a[m%10]++;
     m/=10;
    }

    flag = true;

    for(long i=0;i<10;i++)
    {
      if(a[i]==0)
      flag = false;
      
    }
 
   
   }while(flag==false);     
     
      for(long long i=0;i<10;i++)
       cout<<a[i]<<" ";
     raja = raja - 1;
   cout<<"Case #"<<ankur++<<": "<<n*raja<<endl;


  }

 }

 return 0;
}
