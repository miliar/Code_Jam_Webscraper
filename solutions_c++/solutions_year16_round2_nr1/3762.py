#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cassert>
#include<string>

using namespace std;

class gdt{
public:
string c;
int res[10];
int m;
int ch[2000];
gdt(string s)
{
c=s;
m=1;
for(int i=0;i<=2000;i++)
ch[i]=0;
}

int se(char k)
{
for(int i=0;i<c.length();i++)
{
if(c[i]==k && ch[i]==0)
return i;
}
return -1;
}
void pricheck()
{
for(int i=0;i<c.length();i++)
{
if(c[i]=='Z')
{
res[m]=0;
m++;
ch[se('Z')]=1;
ch[se('E')]=1;
ch[se('R')]=1;
ch[se('O')]=1;
}
else if(c[i]=='X')
{
res[m]=6;
m++;
ch[se('S')]=1;
ch[se('I')]=1;
ch[se('X')]=1;
}
else if(c[i]=='W')
{
res[m]=2;
m++;
ch[se('T')]=1;
ch[se('W')]=1;
ch[se('O')]=1;
}
else if(c[i]=='G')
{
res[m]=8;
m++;
ch[se('E')]=1;
ch[se('I')]=1;
ch[se('G')]=1;
ch[se('H')]=1;
ch[se('T')]=1;
}
else if(c[i]=='U')
{
res[m]=4;
m++;
ch[se('F')]=1;
ch[se('O')]=1;
ch[se('U')]=1;
ch[se('R')]=1;
}
}
for(int i=0;i<c.length();i++)
{
if(c[i]=='F' && ch[i]==0)
{
res[m]=5;
m++;
ch[se('F')]=1;
ch[se('I')]=1;
ch[se('V')]=1;
ch[se('E')]=1;
}
else if(c[i]=='S' && ch[i]==0)
{
res[m]=7;
m++;
ch[se('S')]=1;
ch[se('E')]=1;
ch[se('V')]=1;
ch[se('E')]=1;
ch[se('N')]=1;
}
else if(c[i]=='T' && ch[i]==0)
{
res[m]=3;
m++;
ch[se('E')]=1;
ch[se('E')]=1;
ch[se('R')]=1;
ch[se('H')]=1;
ch[se('T')]=1;
}

else if(c[i]=='O' && ch[i]==0)
{
res[m]=1;
m++;
ch[se('E')]=1;
ch[se('N')]=1;
ch[se('O')]=1;
}

}
for(int j=0;j<c.length();j++)
{
if(c[j]=='I' && ch[j]==0)
{
res[m]=9;
m++;
ch[se('I')]=1;
ch[se('N')]=1;
ch[se('N')]=1;
ch[se('E')]=1;
}
}
}
void bubblesort()
{
for (int c = 1 ; c < m; c++)
  {
    for (int d = 1 ; d < m - c ; d++)
    {
      if (res[d] > res[d+1]) /* For decreasing order use < */
      {
       int  swap       = res[d];
        res[d]   = res[d+1];
        res[d+1] = swap;
      }
    }
  }
}

void disp()
{
for(int i=1;i<m;i++)
cout<<res[i];
}





};

int main()
{
FILE *fin=freopen("A-small-attempt1.in","r",stdin);
assert(fin!=NULL);
FILE *fout=freopen("A-small-attempt1.out","w",stdout);
int T;
cin>>T;
for(int t=1;t<=T;t++)
{
string code;
cin>>code;
gdt g(code);
g.pricheck();
g.bubblesort();
cout<<"Case #"<<t<<": ";
g.disp();
cout<<endl;
} 
return 0;
}
