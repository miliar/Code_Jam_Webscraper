#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>

void main()
{
 clrscr();

 ifstream fi("cin.in");
 ofstream fo("COUT.IN");

 long double t;
 char ch;

 fi>>t;
 fi.get(ch);

 for(int i=1;i<=t;i++)
 {
  int n;
  fi>>n;
  fi.get(ch);

  int p[4];

  for(int z=0;z<n;z++)
  fi>>p[z];
  fi.get(ch);

  fo<<"Case #"<<i<<":";

  char cha[3]={'A','B','C'},tmp;

  int size=n,temp;
  for(int x=0;x<n;x++)
  {
   for(int j=0;j<(size-1)-x;j++)
   {
    if(p[j]>p[j+1])
    {
     temp=p[j];
     p[j]=p[j+1];
     p[j+1]=temp;

     tmp=cha[j];
     cha[j]=cha[j+1];
     cha[j+1]=tmp;
    }
   }
  }


  if (n==2)
  {
	cout<<"\n"<<p[0]<<" "<<p[1]<<" "<<cha[0]<<cha[1];

	while(p[1]>p[0])
	{
	 p[1]=p[1]-1;
	 fo<<"  "<<cha[1];
	}
	while(p[0]>=1)
	{
	 p[1]=p[1]-1;
	 p[0]=p[0]-1;
	 fo<<" "<<cha[1]<<cha[0];
	}
	fo<<"\n";
  }

  if(n==3)
  {


	cout<<"\n"<<p[0]<<" "<<p[1]<<" "<<p[2]<<" "<<cha[0]<<cha[1]<<cha[2];

	while(p[2]>p[1])
	{
	 p[2]=p[2]-1;
	 fo<<" "<<cha[2];
	}
	while(p[1]>p[0])
	{
	 p[2]--;
	 p[1]--;
	 fo<<" "<<cha[2]<<cha[1];
	}

	for(z=0;z<p[2];z++)
	fo<<" "<<cha[0]<<" "<<cha[1]<<cha[2];
	fo<<"\n";
  }







  cout<<i<<"\n";
 }

 cout<<"\nDone";

 fi.close();
 fo.close();

 getch();
}


/* int tot=0;
  for(z=0;z<n;z++)
  tot=tot+p[z];
  float half=tot/2;
 */