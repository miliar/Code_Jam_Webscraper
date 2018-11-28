#include<iostream>
#include<fstream>
#include<vector>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
int a1[5][5],a2[5][5];
ifstream in("test");
ofstream out("opt");
int n;
in>>n;

int t1,t2;

for(int i=0;i<n;i++)
{out<<"Case #"<<i+1<<": ";
int t1,t2;
in>>t1;

for(int r=1;r<=4;r++)
for(int c=1;c<=4;c++)
{in>>a1[r][c];}

vector <int> v1;vector <int> v2;
vector <int>::iterator it;
v1.push_back(a1[t1][1]);
v1.push_back(a1[t1][2]);
v1.push_back(a1[t1][3]);
v1.push_back(a1[t1][4]);
in>>t2;

for(int r=1;r<=4;r++)
for(int c=1;c<=4;c++)
{in>>a2[r][c];}
for(int j=1;j<=4;j++)
{
it=find(v1.begin(),v1.end(),a2[t2][j]);
if(it!=v1.end())
{v2.push_back(a2[t2][j]);}
}
if(v2.size()==0)
out<<"Volunteer cheated!"<<endl;
else if(v2.size()==1)
out<<v2[0]<<endl;
else
out<<"Bad magician!"<<endl;

}

return 1;
}
