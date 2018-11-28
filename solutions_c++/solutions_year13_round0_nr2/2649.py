#include<iostream>
#include<fstream>
using namespace std;

int n,m,a[101][101];
int row(int i)
{
    int t=a[i][0];
    for(int j=0;j<m;j++)
    if(a[i][j]!=t) return 0;
    return 1;
    }
int column(int j)
{
    int t=a[0][j];
    for(int i=0;i<n;i++)
    if(a[i][j]!=t) return 0;
    return 1;
    }
int main()
{
freopen("B-small-attempt0.in","r",stdin);
freopen("output.txt","w",stdout);

    int test,jkl=1;
    cin>>test;
    while(test--){
                  int trace=1;
                  cin>>n>>m;
                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  cin>>a[i][j];
                  int max=a[0][0];
                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  if(a[i][j]>max) max=a[i][j];
                  int to[101][101];
                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  to[i][j]=max;
                  for(int i=0;i<n;i++)
                  if(row(i)==1) {
                                int tem=a[i][0];
                                for(int j=0;j<m;j++)
                                to[i][j]=tem;
                                }
                  for(int j=0;j<m;j++)
                  {
                          if(column(j)==1) {
                                           int tem=a[0][j];
                                           for(int i=0;i<n;i++)
                                           to[i][j]=tem;
                                           }
                  }

                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  if(a[i][j]!=to[i][j]) {trace=0;break;}

                  if(trace==1) cout<<"Case #"<<jkl<<": YES"<<endl;
                  else cout<<"Case #"<<jkl<<": NO"<<endl;
                  jkl++;}
    return 0;
}
