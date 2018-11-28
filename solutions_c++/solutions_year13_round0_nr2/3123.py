#include<iostream>
#include<fstream>
using namespace std;

int a[120][120];
int n,m;

bool pan(int x,int y)
{
 bool temp1=true;
 bool temp2=true;
     for(int i=1;i<=n;i++)
        if(a[i][y]>a[x][y]) temp1=false;
     for(int j=1;j<=m;j++)
        if(a[x][j]>a[x][y]) temp2=false;
 if((!temp1)&&(!temp2)) return false;
   else return true;
}

int main()
{
    ifstream inf("B-large.in");
    ofstream outf("B-large.out");
    int k;
    inf>>k;
 for(int b=1;b<=k;b++)
 {
 string answer="YES";
 inf>>n>>m;
 for(int i=1;i<=n;i++)
  for(int j=1;j<=m;j++)
    inf>>a[i][j];
 
for(int i=1;i<=n;i++)
  for(int j=1;j<=m;j++)
    if(!pan(i,j)) answer="NO";
  outf<<"Case #"<<b<<": "<<answer;
  outf<<endl;
}
 inf.close();
 outf.close();
 return 0;
}
