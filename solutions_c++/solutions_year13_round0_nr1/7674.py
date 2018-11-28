#include <iostream>
#include <fstream>
#include <conio.h>
#include <string>
#include <stdio.h>
#include <stdio.h>
#include <conio.h>
#include <string>
#include <memory>
using namespace std;
char a[2000][5][10];
int testx[2000][4][4],testo[2000][4][4],flag[2000];
int main()
{
int T;
int i,j,k,resultx[2000],resulto[2000];
// declare variables

int xr1[2000],xr2[2000],xr3[2000],xr4[2000],xc1[2000],xc2[2000],xc3[2000],xc4[2000],xd1[2000],xd2[2000];
int or1[2000],or2[2000],or3[2000],or4[2000],oc1[2000],oc2[2000],oc3[2000],oc4[2000],od1[2000],od2[2000];

		 FILE *fpinput=fopen("C:/Users/suneesh jacob/Desktop/google/codejam/files/input.in", "r");
         FILE *fpoutput=fopen("C:/Users/suneesh jacob/Desktop/google/codejam/files/output.out", "w");

fscanf(fpinput,"%d",&T);
cout<<T<<endl;
for(i=0;i<T;i++)
{
flag[i]=0;
for(j=0;j<5;j++)
{
fgets(a[i][j],2000,fpinput);
for(k=0;k<4;k++)
{
if(a[i][j][k]=='.')
flag[i]=1;
}
/*
cout<<"matrix="<<a[i][j][0]<<"  "<<a[i][j][1]<<"  "<<a[i][j][2]<<"  "<<a[i][j][3]<<endl;
*/
}
}
//scan T matrices
/*
for(i=0;i<T;i++)
{
for(j=0;j<=4;j++)
{

cout<<"matrix"<<i<<j<<"="<<a[i][j]<<endl;

}
}
*/
for(i=0;i<T;i++)
{
for(j=1;j<=4;j++)
{
for(k=0;k<4;k++)
{
if(a[i][j][k]=='X'||a[i][j][k]=='T')
testx[i][j-1][k]=1;
if(a[i][j][k]=='O'||a[i][j][k]=='T')
testo[i][j-1][k]=1;
}
}
}
for(i=0;i<T;i++)
{
xr1[i]=testx[i][0][0]+testx[i][0][1]+testx[i][0][2]+testx[i][0][3];
xr2[i]=testx[i][1][0]+testx[i][1][1]+testx[i][1][2]+testx[i][1][3];
xr3[i]=testx[i][2][0]+testx[i][2][1]+testx[i][2][2]+testx[i][2][3];
xr4[i]=testx[i][3][0]+testx[i][3][1]+testx[i][3][2]+testx[i][3][3];

xc1[i]=testx[i][0][0]+testx[i][1][0]+testx[i][2][0]+testx[i][3][0];
xc2[i]=testx[i][0][1]+testx[i][1][1]+testx[i][2][1]+testx[i][3][1];
xc3[i]=testx[i][0][2]+testx[i][1][2]+testx[i][2][2]+testx[i][3][2];
xc4[i]=testx[i][0][3]+testx[i][1][3]+testx[i][2][3]+testx[i][3][3];

xd1[i]=testx[i][0][0]+testx[i][1][1]+testx[i][2][2]+testx[i][3][3];
xd2[i]=testx[i][3][0]+testx[i][2][1]+testx[i][1][2]+testx[i][0][3];


or1[i]=testo[i][0][0]+testo[i][0][1]+testo[i][0][2]+testo[i][0][3];
or2[i]=testo[i][1][0]+testo[i][1][1]+testo[i][1][2]+testo[i][1][3];
or3[i]=testo[i][2][0]+testo[i][2][1]+testo[i][2][2]+testo[i][2][3];
or4[i]=testo[i][3][0]+testo[i][3][1]+testo[i][3][2]+testo[i][3][3];

oc1[i]=testo[i][0][0]+testo[i][1][0]+testo[i][2][0]+testo[i][3][0];
oc2[i]=testo[i][0][1]+testo[i][1][1]+testo[i][2][1]+testo[i][3][1];
oc3[i]=testo[i][0][2]+testo[i][1][2]+testo[i][2][2]+testo[i][3][2];
oc4[i]=testo[i][0][3]+testo[i][1][3]+testo[i][2][3]+testo[i][3][3];

od1[i]=testo[i][0][0]+testo[i][1][1]+testo[i][2][2]+testo[i][3][3];
od2[i]=testo[i][3][0]+testo[i][2][1]+testo[i][1][2]+testo[i][0][3];

}
for(i=0;i<T;i++)
{
if(xr1[i]==4)
{
resultx[i]=1;
}else if(xr2[i]==4)
{
resultx[i]=1;
}else if(xr3[i]==4)
{
resultx[i]=1;
}else if(xr4[i]==4)
{
resultx[i]=1;
}else if(xc1[i]==4)
{
resultx[i]=1;
}else if(xc2[i]==4)
{
resultx[i]=1;
}else if(xc3[i]==4)
{
resultx[i]=1;
}else if(xc4[i]==4)
{
resultx[i]=1;
}else if(xd1[i]==4)
{
resultx[i]=1;
}else if(xd2[i]==4)
{
resultx[i]=1;
}


/*
for(int m=0;m<T;m++)
{
cout<<xr1[m]<<or1[m]<<endl;
cout<<xr2[m]<<or2[m]<<endl;
cout<<xr3[m]<<or3[m]<<endl;
cout<<xr4[m]<<or4[m]<<endl;
cout<<xc1[m]<<oc1[m]<<endl;
cout<<xc2[m]<<oc2[m]<<endl;
cout<<xc3[m]<<oc3[m]<<endl;
cout<<xc4[m]<<oc4[m]<<endl;
cout<<xd1[m]<<od1[m]<<endl;
cout<<xd2[m]<<od2[m]<<endl;
cout<<endl<<flag[m]<<endl<<endl;
}
*/


if(or1[i]==4)
{
resulto[i]=1;
}else if(or2[i]==4)
{
resulto[i]=1;
}else if(or3[i]==4)
{
resulto[i]=1;
}else if(or4[i]==4)
{
resulto[i]=1;
}else if(oc1[i]==4)
{
resulto[i]=1;
}else if(oc2[i]==4)
{
resulto[i]=1;
}else if(oc3[i]==4)
{
resulto[i]=1;
}else if(oc4[i]==4)
{
resulto[i]=1;
}else if(od1[i]==4)
{
resulto[i]=1;
}else if(od2[i]==4)
{
resulto[i]=1;
}

}

for(i=0;i<T;i++)
{
	int n=i+1;
if(resultx[i]==0 && resulto[i]==0)
{
if(flag[i]==1)
{
cout<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;cout<<resultx[i]<<endl<<resulto[i]<<endl;
fprintf(fpoutput,"Case #%d: Game has not completed\n",n);
}else
{
cout<<"Case #"<<i+1<<": "<<"Draw"<<endl;cout<<resultx[i]<<endl<<resulto[i]<<endl;
fprintf(fpoutput,"Case #%d: Draw\n",n);
}
}else if(resultx[i]==1 && resulto[i]==0)
{
cout<<"Case #"<<i+1<<": "<<"X won"<<endl;cout<<resultx[i]<<endl<<resulto[i]<<endl;
fprintf(fpoutput,"Case #%d: X won\n",n);
}else if(resultx[i]==0 && resulto[i]==1)
{
cout<<"Case #"<<i+1<<": "<<"O won"<<endl;cout<<resultx[i]<<endl<<resulto[i]<<endl;
fprintf(fpoutput,"Case #%d: O won\n",n);
}
}
cout<<"This editor is working"<<endl;
getch();
return 0;
}
