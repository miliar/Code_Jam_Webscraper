#include<iostream>
#include<string>
#include<cstdio>
using namespace std;
int a[4][4];
void check(int tcase)
{
int winner=0;
int flag=0;
int xcount=0,ocount=0;
//checking for rows
for(int j=0;j<4;j++)
{
for(int i=0;i<4;i++)
{
if(a[j][i]=='X' || a[j][i]=='T')
xcount++;
else if(a[j][i]=='O' || a[j][i]=='O')
ocount++;
else if(a[j][i]=='.')
flag=1;
}
if(xcount==4)
{
cout<<"Case #"<<tcase<<":"<<" X won "<<endl;
winner=1;
}
else if(ocount==4)
{
cout<<"Case #"<<tcase<<":"<<" O won "<<endl;
winner=1;
}
xcount=0;
ocount=0;
}
//checking for coloumns...
if(winner==0)
for(int j=0;j<4;j++)
{
for(int i=0;i<4;i++)
{
if(a[i][j]=='X' || a[i][j]=='T')
xcount++;
else if(a[i][j]=='O' || a[i][j]=='O')
ocount++;
else if(a[i][j]=='.')
flag=1;
}
if(xcount==4)
{
cout<<"Case #"<<tcase<<":"<<" X won "<<endl;
winner=1;
}
else if(ocount==4)
{
cout<<"Case #"<<tcase<<":"<<" O won "<<endl;
winner=1;
}
xcount=0;
ocount=0;
}
//checking for first diagonal
if(winner==0)
{
for(int i=0;i<4;i++)
{
if(a[i][i]=='X' || a[i][i]=='T')
xcount++;
else if(a[i][i]=='O'|| a[i][i]=='T')
ocount++;
}
if(xcount==4)
{
cout<<"Case #"<<tcase<<":"<<" X won "<<endl;
winner=1;
}
if(ocount==4)
{
cout<<"Case #"<<tcase<<":"<<" O won "<<endl;
winner=1;
}
xcount=0;
ocount=0;
}
//checking for second diagonal
if(winner==0)
{
for(int i=0,j=3;i<4;i++,j--)
{
if(a[i][j]=='X' || a[i][j]=='T')
xcount++;
else if(a[i][j]=='O' || a[i][j]=='O')
ocount++;

}
if(xcount==4)
{
cout<<"Case #"<<tcase<<":"<<" X won "<<endl;
winner=1;
}
else if(ocount==4)
{
cout<<"Case #"<<tcase<<":"<<" O won "<<endl;
winner=1;
}
xcount=0;
ocount=0;
}
if(winner==0 && flag==0)
cout<<"Case #"<<tcase<<":"<<" Draw"<<endl;
if(winner==0 && flag==1)
cout<<"Case #"<<tcase<<":"<<" Game has not completed"<<endl;
}


int main()
{
int t;
string s;
string blank;
cin>>t;
int tcase=t;
while(t--)
{

for(int j=0;j<4;j++)
{
cin>>s;
for(int i=0;i<4;i++)
{
a[j][i]=s.at(i);
}
}
check(tcase-t);
getchar();
}
return 0;
}
