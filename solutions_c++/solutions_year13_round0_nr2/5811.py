#include<fstream>
#include<iostream>
#include<string.h>
using namespace std;
int b[11][11];
int a[11][11];
int n,m;
 ifstream fin("B-small.in");
    ofstream fout("B-small.out");
bool check(){
     bool y=true;
     for(int i=0;i!=n;i++){
             for(int j=0;j!=m;j++){
                     //fout<<b[i][j]<<" ";
                     if(a[i][j]!=b[i][j]){y=false;return false;}
                     }
             
             //fout<<endl;
             
             }
     //fout<<endl;
     return y;
     }
bool findd(int x){
     bool y=false;
     if(x>(m+n)) return check();
     int tmp[11][11];
     memcpy(tmp,b,sizeof(b));
     if(x<=m){
             for(int i=0;i!=n;i++){
                     b[i][x-1]=1;
                     }
             y=findd(x+1)||y;
             memcpy(b,tmp,sizeof(b));
             }
     else{
          for(int i=0;i!=m;i++){
                     b[x-m-1][i]=1;
                     }
          y=findd(x+1)||y;
          memcpy(b,tmp,sizeof(b));
          }
     y=findd(x+1)||y;
     return y;
     }
int main(){
   
    int t;
    fin>>t;
    for(int i=1;i<=t;i++){
          
          fin>>n>>m;
          for(int k=0;k!=n;k++){
                  for(int j=0;j!=m;j++) fin>>a[k][j];
                  }
          for(int j=0;j!=11;j++)
           for(int k=0;k!=11;k++)
            b[j][k]=2;
          if(findd(1))  
          fout<<"Case #"<<i<<": "<<"YES"<<endl;
          else fout<<"Case #"<<i<<": "<<"NO"<<endl;
          }
    }
