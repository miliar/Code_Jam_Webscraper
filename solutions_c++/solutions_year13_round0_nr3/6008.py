#include<stdio.h>
#include<conio.h>
#include<iostream.h>
#include<math.h>
#include<fstream.h>
int fair(int p,int q);

void main()
{
  fstream f1,f2;
  int k,p,q,count,t;
  clrscr();
  f1.open("INPUTF.txt",ios::in);
  f2.open("OUTPUTF.txt",ios::out);
  f1>>t;
  cout<<t;
  for(k=0;k<t;k++)
  {
   f1>>p>>q;
   cout<<p<<"\n"<<q<<"\n";
   count=fair(p,q);
   f2<<"Case #"<<k+1<<": "<<count<<"\n";
  }

  getch();
}
  int fair(int p,int q)
  {
   int l=0;
   int i,j,n,a[1000],e[1000],f[1000],c=0,count=0,r[1000]={0};
   int b[1000],r1[1000]={0};

   for(i=p;i<=q;i++)
   {
	 a[l]=i;
	 b[l]=sqrt(i);
	 l++;
   }
   l=0;
   for(i=p;i<=q;i++)
   {
	e[l]=a[l];
	f[l]=b[l];
	cout<<e[l]<<endl<<f[l]<<endl;
	l++;
   }
   c=q-p;

   for(i=0;i<=c;i++)
   {
   while(a[i]!=0)
   {
      r[i]=r[i]*10;
      r[i]=r[i]+a[i]%10;
      a[i]=a[i]/10;

   }
   cout<<r[i]<<endl;
   if(e[i]==r[i])
   {
     cout<<e[i]<<"  is palindrome   ::";
   }
   while(b[i]!=0)
   {
      r1[i]=r1[i]*10;
      r1[i]=r1[i]+b[i]%10;
      b[i]=b[i]/10;

   }
   cout<<endl<<r1[i]<<endl;
   if(r1[i]==f[i])
   {
     cout<<f[i]<<"  is palindrome   ::";
   }

   if(e[i]==r[i]&&f[i]==r1[i]&&e[i]==pow(f[i],2))
   {
     count=count+1;
     cout<<endl<<"the fair and square no. is:";
     cout<<e[i];
   }

}
cout<<endl<<"count is:"<<count;
printf("\n");
return(count);

}