#include<conio.h>
#include<fstream.h>
#include<math.h>

void palindrome(int &res,int a,int b)
{
 int count=0,rev=0,sq=0,c,d;
 for(int i=1;i<=(b+a)/2;i++)
 {
  rev=0;
  sq=0;
  c=i;
  while(c>0)
  {
   rev=(rev*10)+(c%10);
   c=(c/10);
  }
  if(rev==i)
  {
   c=pow(rev,2);
   d=c;
   while(c>0)
   {
    sq=(sq*10)+(c%10);
    c=(c/10);
   }
   if(d==sq)
   {
    if(d>=a && d<=b)
     count+=1;
   }
  }
 }
 res=count;
}

void main()
{
 clrscr();
 ifstream Ifile("CSMALL.IN",ios::in);
 ofstream Ofile("RESULT3.TXT",ios::out);
 int T,A,B,i=0;
 Ifile>>T;
 int *result;
 result=new int[T];
 while(Ifile)
 {
  Ifile>>A>>B;
  palindrome(result[i],A,B);
  i+=1;
 }
 Ifile.close();
 for(i=0;i<T;i++)
 {
  Ofile<<"\nCase #"<<i+1<<": "<<result[i];
  cout<<"\nCase #"<<i+1<<": "<<result[i];
 }
 Ofile.close();
 delete [] result;
}