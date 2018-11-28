#include<stdio.h>
#include<conio.h>
#include<iostream.h>
#include<fstream.h>
int tictac(char **a);
void main()
{
   int i,t,j,k,s;
   char **a;
   a=new char*[4];
   for(i=0;i<4;i++)
       a[i]=new char[4];
   clrscr();
   fstream f1,f2;
   f1.open("INPUT.txt",ios::in);
   f2.open("OUTPUT.txt",ios::out);
   f1>>t;
   cout<<t;
   for(k=0;k<t;k++)
      {	for(i=0;i<4;i++)
	   {
		for(j=0;j<4;j++)
		   {
			f1>>a[i][j];
			cout<<a[i][j];
		   }
	   }
	   s=tictac(a);
	   if(s==1)
	      f2<<"Case #"<<k+1<<": X won\n";
	   if(s==2)
	      f2<<"Case #"<<k+1<<": O won\n";
	   if(s==3)
	      f2<<"Case #"<<k+1<<": Game has not completed\n";
	   if(s==4)
	      f2<<"Case #"<<k+1<<": Draw\n";

      }

    getch();
}
 int tictac(char **a)
 {
 int i=0,j,count[10]={0},q[100]={0},flag=0;
 int state;
 while(i<4)
 {
 count[0]=0;
 for(j=0;j<4;j++)
  {
   if(a[i][j]=='X'||a[i][j]=='T')
   {
   state=1;

   count[0]++;
   }
  }
  if(count[0]==4)
  {
  state=1;
  q[0]=1;
  }
  i++;
}


  j=0;
  while(j<4)
  {
    count[1]=0;
 for(i=0;i<4;i++)
  {
   if(a[i][j]=='X'||a[i][j]=='T')
   {
   count[1]++;
   }
  }
  if(count[1]==4)
  {
  state=1;
 // cout<<"\nx won";
  q[1]=1;
  }
  j++;
}

  j=0;i=0;
  while(i<4)
  {
    if(a[i][j]=='X'||a[i][j]=='T')
    {
     count[2]++;
    }
    i++;
    j++;
  }

  if(count[2]==4)
  {
  state=1;
 // cout<<"\nx won";
  q[2]=1;
  }

  j=0;i=3;
  while(i<4&&i>=0)
  {
    if(a[i][j]=='X'||a[i][j]=='T')
    {
     count[3]++;
    }
    i--;
    j++;
  }
  if(count[3]==4)
  {
  state=1;
  cout<<"\nx won";
  q[3]=1;
  }

  i=0;
 while(i<4)
 {
 count[4]=0;
 for(j=0;j<4;j++)
  {
   if(a[i][j]=='O'||a[i][j]=='T')
   {
   count[4]++;
   }
  }

  if(count[4]==4)
  {
  state=2;
  cout<<"\no won";
  q[4]=1;
  }
  i++;
}
  j=0;
while(j<4)
{
  count[5]=0;
  for(i=0;i<4;i++)
  {
   if(a[i][j]=='O'||a[i][j]=='T')
   {
   count[5]++;
   }
  }
  if(count[5]==4)
  {
  state=2;
  cout<<"\no won";
  q[5]=1;
  }
  j++;
}

  j=0;i=0;
  while(i<4)
  {
    if(a[i][j]=='O'||a[i][j]=='T')
    {
     count[6]++;
    }
    i++;
    j++;
  }
  if(count[6]==4)
  {
  state=2;
  cout<<"\no won";
  q[6]=1;
  }
  j=0;i=3;
  count[7]=0;
  while(i<4&&i>=0)
  {
    if(a[i][j]=='O'||a[i][j]=='T')
    {
     count[7]++;

    }
    i--;
    j++;
  }

  if(count[7]==4)
  {
  state=2;
  cout<<"\no won";
  q[7]=1;
  }

   for(i=0;i<4;i++)
   {
    for(j=0;j<4;j++)
    {
       if(a[i][j]=='.')
       {
	count[8]++;
       }
    }
   }

   for(i=0;i<9;i++)
   {
    if(q[i]==1)
    {
      flag=1;
    }
   }
   if(flag!=1&&count[8]>=1)
   {
    state=3;
    cout<<"\ngame has not completed ";
   }
   for(i=0;i<9;i++)
   {
    if(q[i]==1)
    {
      flag=1;
    }
   }
   if(flag!=1&&count[8]==0)
   {
    state=4;
    cout<<"\ndraw";
   }
   return(state);
}

