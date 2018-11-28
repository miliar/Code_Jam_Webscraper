#include<iostream>
#include<math.h>
using namespace std;

int number[1<<5];
bool primes[1<<20];

long long int interpreter(int base)
{
   long long int ans=0,i;
   for(i=1;i<=16;i++)
   {
      ans*=base;
      ans+=number[i];
   }
   //cout<<ans<<endl;
   return ans;
}

int main()
{
   freopen ("C-small.in", "r", stdin);
   freopen ("C-small.out", "w" , stdout);
   long long int n,t,tt,i[1<<5],j,a[1<<4],c,cc,fl,ans[1<<5],l;
   string s;
   for(i[1]=1;i[1]<=1000000;i[1]++)
   {
       primes[i[1]]=1;
   }
   primes[1]=0;
   primes[2]=1;
   for(i[1]=2;i[1]<=10000;i[1]++)
   {
      if(primes[i[1]]==1)
      {
         //cout<<i[1]<<endl;
         for(j=i[1]+i[1];j<=1000000;j+=i[1])
         {
            primes[j]=0;
         }
      }
   }
   //cin>>t;
   t=1;
   n=50;
   l=16;
   number[1]=1;
   number[16]=1;
   
   //cin>>n;
   //cout<<primes[n]<<endl;
   
   cout<<"Case #"<<1<<": "<<endl;
   while(n>0)
   {
      //system("pause");
      for(number[2]=0;number[2]<=1;number[2]++)
      for(number[3]=0;number[3]<=1;number[3]++)
      for(number[4]=0;number[4]<=1;number[4]++)
      for(number[5]=0;number[5]<=1;number[5]++)
      for(number[6]=0;number[6]<=1;number[6]++)
      for(number[7]=0;number[7]<=1;number[7]++)
      for(number[8]=0;number[8]<=1;number[8]++)
      for(number[9]=0;number[9]<=1;number[9]++)
      for(number[10]=0;number[10]<=1;number[10]++)
      for(number[11]=0;number[11]<=1;number[11]++)
      for(number[12]=0;number[12]<=1;number[12]++)
      for(number[13]=0;number[13]<=1;number[13]++)
      for(number[14]=0;number[14]<=1;number[14]++)
      for(number[15]=0;number[15]<=1;number[15]++)
      {
         fl=0;
         /*cout<<endl;
         for(j=1;j<=16;j++)
         {
            cout<<number[j];
         }
         cout<<" ";*/
         fl=0;
         for(j=2;j<=10;j++)
         {
            long long int aaa=interpreter(j);
            //cout<<aaa<<endl;
            //system("pause");
            /*if(primes[aaa]==0)
            {*/
               //cout<<aaa<<endl;
               int fl2=0;
               for(int k=2;k<=sqrt(aaa);k++)
               {
                  if(aaa%k==0)
                  {
                     ans[j]=k;
                     //cout<<k<<" ";
                     fl2=1;
                     break;
                  }
               }
               if(fl2==0)
               {
                  fl=1;
                  //cout<<endl;
                  break;
               }
            /*}*/
            /*else
            {
               fl=1;
               break;
            }*/
         }
         if(fl==0)
         {
            for(j=1;j<=16;j++)
            {
               cout<<number[j];
            }
            cout<<" ";
            for(j=2;j<=10;j++)
            {
               cout<<ans[j]<<" ";
            }
            cout<<endl;
            n--;
            //system("pause");
            if(n==0)
            {
               //system("pause");
               return 0;
            }
         }
      }
      
   }
   /*for(tt=1;tt<=t;tt++)
   {
      cnumbern>>s;
      s+="+";
      //n=tt;
      c=0;
      for(number=s.length()-1;number>=1;number--)
      {
         numberf(s[number]!=s[number-1])
         {
            c++;
         }
      }
      cout<<"Case #"<<tt<<": "<<c<<endl;
   }*/
   //system("pause");
   return 0;
}
