#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;
int main()
{
	char a[4][4],w;
	long int t,i,j,k,c[10],cs,l;
	ifstream inp;
	
	ofstream oupt;
	inp.open("A-large.in");
	oupt.open("a-large.out");
    inp>>t;
    cout<<t;
  cs=0;
  while(t--)
  { cs++;
  	for(i=0;i<4;i++)
  	 {
  	  for(k=0;k<4;k++)
  	   {
  	   inp>>a[i][k];
  	   
        }
       }
  	memset(c,0,sizeof(c)); 
	for(i=0;i<4;i++)
	 {
	 	for(k=0;k<4;k++)
	 	{  c[i]=c[i]+a[i][k];
	 	   c[i+4]=c[i+4]+a[k][i];
	 	}
	 }
	 c[8]=a[0][0]+a[1][1]+a[2][2]+a[3][3];
	 c[9]=a[0][3]+a[1][2]+a[2][1]+a[3][0];
	 j=0;
	 for(i=0;i<10;i++)
	 {
	 	if(c[i]==352 || c[i]==348 || c[i]==316 ||c[i]==321)
	 	{l=c[i];
	 	 j=2;
	 	 break;
	 	} 
	 	if(c[i]<316)
	 	 j=1;
	 }
	 if(j==2)
	 {
	 	if(l==316 || l==321)
	 	{ w='O';
	 	}
	 	else
	 	w='X';
	 	oupt<<"Case #"<<cs<<": "<<w<<" won\n";
	 }
	 else
	 if(j==1)
	 {  oupt<<"Case #"<<cs<<": Game has not completed\n";
	 }
	 else
	 { 
	    oupt<<"Case #"<<cs<<": Draw\n";
	 }
	 
	     
  }
  inp.close();
  oupt.close();
  return 0;
}
