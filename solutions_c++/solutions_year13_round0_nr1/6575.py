#include <iostream>
#include <cstdio>
using namespace std;
int main()
{ int t;
          cin >> t;
	FILE* p;
	p = fopen("output.txt","w");
	for (int x=1;x<=t;x++)
	{ int  a[4][4];
	  char temp,win='0';
	  bool complete=true;
		for (int i=0;i<4;i++)
		{ for (int j=0;j<4;j++)
			{  cin >> temp;
			   if (temp == 'X') a[i][j]=1;
			   else if (temp == 'O') a[i][j]=-1;
			   else if (temp == 'T') a[i][j]=100;
			   else if (temp == '.') a[i][j]=0,complete=false;
			  	     
			}
		}
	  for (int i=0;i<4;i++)
	  { if (a[i][0]+a[i][1]+a[i][2]+a[i][3]==4 || a[i][0]+a[i][1]+a[i][2]+a[i][3]==103)
		  { win = 'X';break;}
	   else if (a[i][0]+a[i][1]+a[i][2]+a[i][3]==-4 || a[i][0]+a[i][1]+a[i][2]+a[i][3]==97)
		  { win = 'O';break;}
	   else if (a[0][i]+a[1][i]+a[2][i]+a[3][i]==-4 || a[0][i]+a[1][i]+a[2][i]+a[3][i]==97)
		 { win = 'O';break;}
	   else if (a[0][i]+a[1][i]+a[2][i]+a[3][i]==4 || a[0][i]+a[1][i]+a[2][i]+a[3][i]==103)
		 { win = 'X';break;}
	  }
	  if (win == '0')
	  { if (a[0][0]+a[1][1]+a[2][2]+a[3][3]==4 || a[0][0]+a[1][1]+a[2][2]+a[3][3]==103)
		  win = 'X';
	    else if (a[0][3]+a[1][2]+a[2][1]+a[3][0]==4 || a[0][3]+a[1][2]+a[2][1]+a[3][0]==103)
		  win = 'X';
	    else if (a[0][0]+a[1][1]+a[2][2]+a[3][3]==-4 || a[0][0]+a[1][1]+a[2][2]+a[3][3]==97)
		  win = 'O';
	    else if (a[0][3]+a[1][2]+a[2][1]+a[3][0]== -4 || a[0][3]+a[1][2]+a[2][1]+a[3][0]==97)
		  win = 'O';
	  }
	  fprintf (p,"Case #%d: ",x);
	  if (win !='0')
		  fprintf(p,"%c won\n",win);
	  else if ( complete == true)
		  fprintf(p,"Draw\n");
	  else 
		  fprintf(p,"Game has not completed\n");
	 }
      return 0;
}      
