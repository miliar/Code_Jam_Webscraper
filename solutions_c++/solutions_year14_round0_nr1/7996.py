#include<iostream.h>
#include<conio.h>
#include<stdlib.h>
int a[4][4],b[4][4],c[100];        int m;
void input(int a[4][4])
{
for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
   	{cin>>a[i][j];
      }
      }

      void trans()
      {for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
		{cin>>b[i][j];
      }

}


void display(int c[4][4])
{for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
  {	cout<<c[i][j]<<" ";
   if(j==3)
   cout<<'\n';
   }
}



void output(int k,int d)
{ c[k-1]=d;}


void disop()
{for(int i=0;i<m;i++)
{if(c[i]>100)
    cout<<'\n'<<"case #"<<i+1<<":"<<" Bad Magician!"<<'\n';

    if(c[i]<100 && c[i]!=0)
    cout<<'\n'<<"case #"<<i+1<<":"<<" "<<c[i]<<'\n';
    if(c[i]==0)
    cout<<'\n'<<"case #"<<i+1<<":"<<" Volunteer cheated!"<<'\n';
    }

 }
void main()
{
      int r;int rr;
          //cout<<"Enter test cases";
          int pp;
          cin>>m;int k=1;


          while(k<=m){
          //cout<<"Enter row";
           cin>>r;
           pp=0;
          input(a);
        //cout<<"Enter row";
        cin>>rr;
        trans();


          int d=0;

   int i,j,kk;
   for(j=0;j<4;j++)
   {for( i=0;i<4;i++)
   {if(a[r-1][j]==b[rr-1][i])
     {d++;      kk=j;
     }
    }
    if(d==1)
    output(k,a[r-1][kk]);
   if(d==0)
   output(k,0);
   if(d>1)
   output(k,100+d);

    }


   k++;
    }
           disop();
    getch();
    }
