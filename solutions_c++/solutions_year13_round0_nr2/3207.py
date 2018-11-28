#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<sstream>
#include<complex.h>
#include<fstream>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
using namespace std;
int main()
{
ifstream file;
ofstream file1;
file.open("inp.txt");
file1.open("out.txt");
int t;
string s;
getline(file,s);
istringstream instr(s);
instr>>t;
for(int k=0;k<t;k++)
{
bool flag=0;
int n,m;
getline(file,s);
istringstream instr2(s);
instr2>>n>>m;
vector< vector<int> >input;
vector<int>max1;
max1.resize(m);
fill(max1.begin(),max1.begin()+m,-10);
for(int i=0;i<n;i++)
{
getline(file,s);
istringstream instr1(s);
vector<int>inp;
int x;
int max=-10;
for(int j=0;j<m;j++)
{
instr1>>x;
if(x>=max1[j])
max1[j]=x;
inp.push_back(x);
if(x>=max)
max=x;
}
inp.push_back(max);
input.push_back(inp);
}
input.push_back(max1);
for(int i=0;i<n;i++)
{
for(int j=0;j<m;j++)
{
if(input[i][j]!=input[i][m]&&input[i][j]!=input[n][j])
{
file1<<"Case #"<<k+1<<": NO"<<"\n";
goto label;
}
}
}
file1<<"Case #"<<k+1<<": YES"<<"\n";
label:;
}
return 0;
}
