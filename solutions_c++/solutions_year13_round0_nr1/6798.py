#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
void main()
{
int n,i,j,x=0,o=0,x1=0,o1=0;
char a[4][4];
string s1="X won";
string s2="Draw";
string s3="Game has not completed";
string s4="O won";
cin>>n;
for(i=0;i<n;i++)
{
for(j=0;j<4;j++)
{
for(k=0;k<4;k++)
{
cin>>a[j][k];
}
}
c=0;
for(j=0;j<4;j++)
{
x=o=x1=o1=x2=o2=0;
for(k=0;k<4;k++)
{
if(a[j][k]=='X'||a[j][k]=='T')
x++;
if(a[j][k]=='O'||a[j][k]=='T')
o++;
if(x==4)
{
c++;
cout<<"Case #"<<j+1<<":"<<" "<<s1;
}
if(o==4)
{
c++;
cout<<"Case #"<<j+1<<":"<<" "<<s4;
}
if(a[k][j]=='X'||a[k][j]=='T')
x1++;
if(a[k][j]=='O'||a[k][j]=='T')
o1++;
if(x1==4)
{
c++;
cout<<"Case #"<<j+1<<":"<<" "<<s1;
}
if(o1==4)
{
c++;
cout<<"Case #"<<j+1<<":"<<" "<<s4;
}
if(a[k][k]=='X'||a[k][k]=='T')
x2++;
if(a[k][k]=='O'||a[k][k]=='T')
o2++;
if(x2==4)
{
c++;
cout<<"Case #"<<j+1<<":"<<" "<<s1;
}
if(o2==4)
{
c++;
cout<<"Case #"<<j+1<<":"<<" "<<s4;
}
if(c==0&&a[j][k]=='.')
{
c++;
cout<<"Case #"<<j+1<<":"<<" "<<s3;
}

}
}
if(c==0)
cout<"Case #"<<j+1<<":"<<" "<<s2;
}
