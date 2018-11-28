#include<iostream>
#include<fstream>
using namespace std;
fstream fcin ("input.txt");
fstream fcout ("output.txt");
int mapa[101][101],maxf[101],maxc[101];
int main(){
    int s,t,q,n,m,si;
    fcin >> t;
    s=t;
    while(t--){
         fcin >> n >> m;
         si=true;
         for(int i=0;i<101;i++) maxf[i]=maxc[i]=0;
         for(int i=0;i<n;i++){
             for(int j=0;j<m;j++){
                 fcin >> mapa[i][j];
                 maxf[i]=max(maxf[i],mapa[i][j]);
             }
         }
         for(int i=0;i<n;i++){
             for(int j=0;j<m;j++){
                 maxc[j]=max(maxc[j],mapa[i][j]);
             }
         }
         for(int i=0;i<n;i++){
             for(int j=0;j<m;j++){
                if(mapa[i][j]!=min(maxf[i],maxc[j])){
                    si=false;
                    break;
                }
             }
             if(!si) break;
         }
         fcout << "Case #" << s-t<< ": ";
         if(si) fcout << "YES\n";
         else fcout << "NO\n";
    }
}

