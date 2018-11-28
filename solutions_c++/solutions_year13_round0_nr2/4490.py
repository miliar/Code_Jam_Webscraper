#include<iostream>
#include<cstring>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
    int t,k,i,j,n,m,flg;
    int a[101][101];
    int r[101];
    int c[101];
    ifstream fin;
    ofstream fout;
    fin.open("B-large.in");
    fout.open("ans.txt");
    fin>>t;
    for(k=1;k<=t;k++){
                      memset(r,-1,sizeof(r));
                      memset(c,-1,sizeof(c));
                      flg=1;
                      fin>>n>>m;
                      for(i=0;i<n;i++){
                                       for(j=0;j<m;j++){
                                                        fin>>a[i][j];
                                                        r[i]=max(r[i],a[i][j]);
                                                        c[j]=max(c[j],a[i][j]);
                                        }
                     }
                     for(i=0;i<n;i++){
                                       for(j=0;j<m;j++)
                                         if(!((a[i][j]==r[i]) || (a[i][j]==c[j])))flg=0;
                     }
                     if(flg==0)fout<<"Case #"<<k<<": NO"<<endl;
                     else    fout<<"Case #"<<k<<": YES"<<endl;
  }
 return 0;
}            
