#include <conio.h>
#include <iostream>

using namespace std;

int numero (char w)
{
   if(w=='0')
      return 0;
   if(w=='1')
      return 1;
   if(w=='2')
      return 2;
   if(w=='3')
      return 3;
   if(w=='4')
      return 4;
   if(w=='5')
      return 5;
   if(w=='6')
      return 6;
   if(w=='7')
      return 7;
   if(w=='8')
      return 8;
   if(w=='9')
      return 9;
}

char letra (int w)
{
   if(w==0)
      return '0';
   if(w==1)
      return '1';
   if(w==2)
      return '2';
   if(w==3)
      return '3';
   if(w==4)
      return '4';
   if(w==5)
      return '5';
   if(w==6)
      return '6';
   if(w==7)
      return '7';
   if(w==8)
      return '8';
   if(w==9)
      return '9';
}

int main(void)
{
   freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);
   int n,a,sum,aum;
   char x[1000];
   cin>>n;
   for(int i=1;i<=n;i++)
   {
      sum=0;
      aum=0;
      cin>>a;
      cin>>x;
      for(int j=0;j<=a;j++)
      {
         if(sum>=j)
         {
            sum=sum+numero(x[j]);
         }
         else
         {
            aum=aum+1;
            sum=sum+1;
            j--;
         }
      }
      cout<<"Case #"<<i<<": "<<aum<<endl;
   }
   //system("PAUSE");
   return 0;
}
