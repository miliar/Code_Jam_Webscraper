#include<iostream>
using namespace std;

char a[4][4];

bool ckrow(int r,char x)
{
for(int i=0;i<4;i++)
if(a[r][i]!=x && a[r][i]!='T')
return false;
return true;
}

bool ckcol(int c,char x)
{
for(int i=0;i<4;i++)
if(a[i][c]!=x && a[i][c]!='T')
return false;
return true;
}

bool ckdiag(char x)
{
bool ck1=true,ck2=true;
int ind1,ind2;
ind1=0;
ind2=0;
for(int i=0;i<4;i++)
{
if(a[ind1][ind2]!=x && a[ind1][ind2]!='T')
{ck1=false;break;}
ind1++;
ind2++;
}
ind1=0;
ind2=3;
for(int i=0;i<4;i++)
{
if(a[ind1][ind2]!=x && a[ind1][ind2]!='T')
{ck2=false;break;}
ind1++;
ind2--;
}
if(ck1 || ck2)
return true;
return false;
}

int main()
{
int t;
cin>>t;
bool x,o,dot;
for(int i=0;i<t;i++)
{
dot=false;
for(int j=0;j<4;j++)
for(int k=0;k<4;k++)
{
cin>>a[j][k];
if(a[j][k]=='.')
dot=true;
}
x=false;
o=false;
for(int j=0;j<4;j++)
{
if(ckrow(j,'X'))
{x=true;break;}
else if(ckrow(j,'O'))
{o=true;break;}
}
if(x)
{cout<<"Case #"<<i+1<<": "<<"X won"<<endl;continue;}
else if(o)
{cout<<"Case #"<<i+1<<": "<<"O won"<<endl;continue;}
for(int j=0;j<4;j++)
{
if(ckcol(j,'X'))
{x=true;break;}
else if(ckcol(j,'O'))
{o=true;break;}
}
if(x)
{cout<<"Case #"<<i+1<<": "<<"X won"<<endl;continue;}
else if(o)
{cout<<"Case #"<<i+1<<": "<<"O won"<<endl;continue;}
if(ckdiag('X'))
{cout<<"Case #"<<i+1<<": "<<"X won"<<endl;continue;}
else if(ckdiag('O'))
{cout<<"Case #"<<i+1<<": "<<"O won"<<endl;continue;}
if(dot)
cout<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
else
cout<<"Case #"<<i+1<<": "<<"Draw"<<endl;
}
return 0;
}
