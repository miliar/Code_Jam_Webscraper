#include<iostream>
using namespace std;
















int main()
{
    int z;
    cin>>z;
    int y;
    for(y=1;y<=z;y++)
    {
        cout<<"Case #"<<y<<": ";
char a[4][4];
int i,j;
int x[4]={0},o[4]={0},m[4]={0};
int x3[4]={0},o3[4]={0},m3[4]={0};
int x1=0,x2=0,o1=0,o2=0,m1=0,m2=0,f=0,f1=0;
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
cin>>a[i][j];
}
}

for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if(a[i][j]=='X')
{
x[i]++;
}
else if(a[i][j]=='O')
{
o[i]++;
}
else if(a[i][j]=='T')
{
m[i]++;
}
}
}

for(i=0;i<4;i++)
{
if(x[i]==4)
{
f=1;
cout<<"X won\n";
break;
}
if(x[i]==3 && m[i]==1)
{
f=1;
cout<<"X won\n";
break;
}
if(o[i]==4)
{
f=1;
cout<<"O won\n";
break;
}
if(o[i]==3 && m[i]==1)
{
f=1;
cout<<"O won\n";
break;
}
}


if(f==0)
{
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if(a[j][i]=='X')
{
x3[i]++;
}
else if(a[j][i]=='O')
{
o3[i]++;
}
else if(a[j][i]=='T')
{
m3[i]++;
}
}
}


for(i=0;i<4;i++)
{
if(x3[i]==4)
{
f=1;
cout<<"X won\n";
break;
}
if(x3[i]==3 && m3[i]==1)
{
f=1;
cout<<"X won\n";
break;
}
if(o3[i]==4)
{
f=1;
cout<<"O won\n";
break;
}
if(o3[i]==3 && m3[i]==1)
{
f=1;
cout<<"O won\n";
break;
}
}
}


if(f==0)
{
for(i=0;i<4;i++)
{
if(a[i][i]=='X')
{
x1++;
}
else if(a[i][i]=='O')
{
o1++;
}
else if(a[i][i]=='T')
{
m1++;
}
}

if(x1==4)
{
f=1;
cout<<"X won\n";
}
if(x1==3 && m1==1)
{
f=1;
cout<<"X won\n";
}
if(o1==4)
{
f=1;
cout<<"O won\n";
}
if(o1==3 && m1==1)
{
f=1;
cout<<"O won\n";
}
}

if(f==0)
{
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if(i+j==3)
{
if(a[i][j]=='X')
{
x2++;
}
else if(a[i][j]=='O')
{
o2++;
}
else if(a[i][j]=='T')
{
m2++;
}
}
}
}

if(x2==4)
{
f=1;
cout<<"X won\n";
}
if(x2==3 && m2==1)
{
f=1;
cout<<"X won\n";
}
if(o2==4)
{
f=1;
cout<<"O won\n";
}
if(o2==3 && m2==1)
{
f=1;
cout<<"O won\n";
}
}

if(f==0)
{
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if(a[i][j]=='.')
{
f1=1;
cout<<"Game has not completed\n";
break;
}
}
if(f1==1)
{
break;
}
}

if(f1==0)
{
cout<<"Draw\n";
}
}
}
}





