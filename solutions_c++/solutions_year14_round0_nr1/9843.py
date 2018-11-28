#include"stdlib.h"
#include"iostream.h"
#include"conio.h"
#include"fstream.h"
void main()
{   int i,j,k,ic=0;
    int mi;
    int r1,r2,n,v=0,c=0;
    char ch,tch[10];
    int a1[4][4],b1[4][4];
    ifstream fin("a2.in");
    ofstream fout("a2.out");

    clrscr();
    ic=0;
    fin.get(ch);
    while(ch!=10 && !fin.eof())
    {  tch[ic++]=ch;
       tch[ic]=NULL;
       fin.get(ch);
    }

    n=atoi(tch);
    for(mi=1;mi<=n;mi++)
    {  fin.get(ch);
       ic=0;
       while(ch!=10 && !fin.eof())
       {  tch[ic++]=ch;
	  tch[ic]=NULL;
	  fin.get(ch);
       }

       r1=atoi(tch);
       for(i=0;i<4;i++)
       for(j=0;j<4;j++)
       {  ic=0;
	  fin.get(ch);
	  while(ch!=10 && ch!=' ' && !fin.eof())
	  {  tch[ic++]=ch;
	     tch[ic]=NULL;
	     fin.get(ch);
	  }
	  a1[i][j]=atoi(tch);

       }
       fin.get(ch);
       ic=0;
       while(ch!=10 && !fin.eof())
       {  tch[ic++]=ch;
	  tch[ic]=NULL;
	  fin.get(ch);
       }

       r2=atoi(tch);

       for(i=0;i<4;i++)
       for(j=0;j<4;j++)
       {  ic=0;
	  fin.get(ch);
	  while(ch!=10 && ch!=' ' && !fin.eof())
	  {  tch[ic++]=ch;
	     tch[ic]=NULL;
	     fin.get(ch);
	  }

	  b1[i][j]=atoi(tch);
       }
       c=0;
       for(i=0;i<4;i++)
       for(j=0;j<4;j++)
      {	if(a1[r1-1][i] == b1[r2-1][j])
	{  v=a1[r1-1][i];
	   c++;
	}
      }
       fout<<"Case #"<<mi<<": ";
       if(c==1) fout<<v;
       else if(c>1) fout<<"Bad magician!";
       else if(c==0) fout<<"Volunteer cheated!";
       if(mi!=100) fout<<"\n";
    }
    getch();
    fin.close();
    fout.close();

}






