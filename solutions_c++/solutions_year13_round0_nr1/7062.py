#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;

char grid[4][4];
char row[4][4];
char col[4][4];
char diag[2][4];
int tx,ty;

int compare(char p[4], char q[4])
{
    int r = 1;
for(int i=0; i<4;i++)
{
 if(p[i]!=q[i])
         r=0;

}        
return r;
}

int chkx()
{
int ans=0;

for(int i=0;i<4;i++)
{
if((compare(row[i],"XXXX")==1)||(compare(col[i],"XXXX")==1))
ans=1;     
}

if(compare(diag[0],"XXXX")==1)
ans=1;


if(compare(diag[1],"XXXX")==1)
ans=1;

return ans;     
}

int chko()
{
int ans=0;

for(int i=0;i<4;i++)
{
if((compare(row[i],"OOOO")==1)||(compare(col[i],"OOOO")==1))
ans=1;     
}


if(compare(diag[0],"OOOO")==1)
ans=1;

if(compare(diag[1],"OOOO")==1)
ans=1;

return ans;     
}
     
int main()
{   
ofstream cout("output.txt");

int isdot;

int x=0,o=0,d=0,g=0;

int t;

cin>>t;

int c=1;

while(c<=t)
{
isdot=0;
tx = 5;
ty = 5;
x=0;
o=0;
g=0;
d=0;

for(int i=0;i<4;i++)
{
        for(int j=0;j<4;j++)
        {
                        cin>>grid[i][j];
                        
                        if(grid[i][j]=='.')
                        isdot=1;        
                        else if(grid[i][j]=='T')
                        {
                        tx=i;
                        ty=j;
                        }   
        
        }
}

if((tx<4)&&(ty<4))
grid[tx][ty]='X';

row[0][0]=grid[0][0];
row[0][1]=grid[0][1];
row[0][2]=grid[0][2];
row[0][3]=grid[0][3];

row[1][0]=grid[1][0];
row[1][1]=grid[1][1];
row[1][2]=grid[1][2];
row[1][3]=grid[1][3];

row[2][0]=grid[2][0];
row[2][1]=grid[2][1];
row[2][2]=grid[2][2];
row[2][3]=grid[2][3];

row[3][0]=grid[3][0];
row[3][1]=grid[3][1];
row[3][2]=grid[3][2];
row[3][3]=grid[3][3];

col[0][0]=grid[0][0];
col[0][1]=grid[1][0];
col[0][2]=grid[2][0];
col[0][3]=grid[3][0];

col[1][0]=grid[0][1];
col[1][1]=grid[1][1];
col[1][2]=grid[2][1];
col[1][3]=grid[3][1];

col[2][0]=grid[0][2];
col[2][1]=grid[1][2];
col[2][2]=grid[2][2];
col[2][3]=grid[3][2];

col[3][0]=grid[0][3];
col[3][1]=grid[1][3];
col[3][2]=grid[2][3];
col[3][3]=grid[3][3];

diag[0][0]=grid[0][0];
diag[0][1]=grid[1][1];
diag[0][2]=grid[2][2];
diag[0][3]=grid[3][3];

diag[1][0]=grid[0][3];
diag[1][1]=grid[1][2];
diag[1][2]=grid[2][1];
diag[1][3]=grid[3][0];

x=chkx();

if((tx<4)&&(ty<4))
grid[tx][ty]='O';

row[0][0]=grid[0][0];
row[0][1]=grid[0][1];
row[0][2]=grid[0][2];
row[0][3]=grid[0][3];

row[1][0]=grid[1][0];
row[1][1]=grid[1][1];
row[1][2]=grid[1][2];
row[1][3]=grid[1][3];

row[2][0]=grid[2][0];
row[2][1]=grid[2][1];
row[2][2]=grid[2][2];
row[2][3]=grid[2][3];

row[3][0]=grid[3][0];
row[3][1]=grid[3][1];
row[3][2]=grid[3][2];
row[3][3]=grid[3][3];

col[0][0]=grid[0][0];
col[0][1]=grid[1][0];
col[0][2]=grid[2][0];
col[0][3]=grid[3][0];

col[1][0]=grid[0][1];
col[1][1]=grid[1][1];
col[1][2]=grid[2][1];
col[1][3]=grid[3][1];

col[2][0]=grid[0][2];
col[2][1]=grid[1][2];
col[2][2]=grid[2][2];
col[2][3]=grid[3][2];

col[3][0]=grid[0][3];
col[3][1]=grid[1][3];
col[3][2]=grid[2][3];
col[3][3]=grid[3][3];

diag[0][0]=grid[0][0];
diag[0][1]=grid[1][1];
diag[0][2]=grid[2][2];
diag[0][3]=grid[3][3];

diag[1][0]=grid[0][3];
diag[1][1]=grid[1][2];
diag[1][2]=grid[2][1];
diag[1][3]=grid[3][0];

if(x==0)
o=chko();

if((x==0)&&(o==0))
{
        if(isdot==1)        
        g=1;
}

if((x==0)&&(o==0)&&(g==0))
d=1;

if(x==1)
cout<<"Case #"<<c<<": X won"<<endl;

if(o==1)
cout<<"Case #"<<c<<": O won"<<endl;

if(g==1)
cout<<"Case #"<<c<<": Game has not completed"<<endl;

if(d==1)
cout<<"Case #"<<c<<": Draw"<<endl;
           
c++;
}


}
