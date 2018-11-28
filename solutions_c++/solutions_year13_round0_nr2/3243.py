#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;
int a[102][102];
int main()
{
 int t,i,j,n,m,k,cas;
 bool f,tf;
 ifstream fin;
 ofstream fout;
 fin.open("in2.txt");
 fout.open("out2.txt");
 fin>>t;
 for(cas=1;cas<=t;cas++)
 {
                       // scanf("%d%d",&n,&m);
                       fin>>n>>m;
                        f=0;tf=0;
                        for(i=0;i<n;i++)
                        for(j=0;j<m;j++)
                        fin>>a[i][j];
                        for(i=0;i<n;i++)
                        {
                        for(j=0;j<m;j++)
                        {
                                        f=0;tf=0;
                                        for(k=0;k<n;k++)
                                        if(a[k][j]>a[i][j])
                                        {tf=1;break;}
                                        if(tf==1)
                                        for(k=0;k<m;k++)
                                        if(a[i][k]>a[i][j])
                                        {f=1;break;}
                                        if(f==1 && tf==1)
                                        break;
                        }
                        if(f==1 && tf==1)
                        break;
                        }
                        if(f==1 && tf==1)
                        fout<<"Case #"<<cas<<": NO\n";
                        else
                        fout<<"Case #"<<cas<<": YES\n";
 }
  fout.close();
  fin.close();                                      
return 0;
}
