//Fair and square solution by QOI
//Hope this is it.
#include<iostream.h>
#include<conio.h>
#include<math.h>

int palindrome(int);
void main(int argc, char *argv[])
{
 clrscr();
     int n, num,cas,count,chk,chk2,l,u;
     float st;
     cin>>cas;
     for(int i=0;i<cas;i++)
     { cin>>l;
       cin>>u;
       count=0;
      for(int j=l;j<=u;j++)
      {
      n = j;
      chk=palindrome(n);
      if(chk==1)
      {

       st=sqrt(n);

      if(st-(int)st==0)
       {
	chk2=palindrome(sqrt(n));
	if(chk2==1)
	count++; }
      }

      }
      cout<<"Case #"<<i+1<<": "<<count<<endl;
    }


}

int palindrome(int n)
{  int num=n,digit,rev=0;
   do
     {
	 digit = num%10;
	 rev = (rev*10) + digit;
	 num = num/10;
     }while (num!=0);
	  if (n==rev)
	  {
	  return 1;}
	  else
	  return 0;
 };











