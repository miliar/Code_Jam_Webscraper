#include<iostream>
using namespace std;
int T,N,M,maks;
int tab[101][101];
int tab2[101][101];
bool zle;
int main(){
    cin>>T;
    for(int q=1;q<=T;q++){
            cin>>N>>M;
            zle=0;
            for(int i=0;i<N;i++){
                    for(int j=0;j<M;j++){
                            cin>>tab[i][j];
                            tab2[i][j]=101;
                            }
                    }
            //zetnij poziomo
            for(int i=0;i<N;i++){
                    maks=(-1);
                    for(int j=0;j<M;j++){
                            if(tab[i][j]>maks)maks=tab[i][j];
                            }
                    for(int j=0;j<M;j++){
                            if(tab2[i][j]>maks)tab2[i][j]=maks;
                            }
                    }
            //zetnij pionowo
            for(int i=0;i<M;i++){
                    maks=(-1);
                    for(int j=0;j<N;j++){
                            if(tab[j][i]>maks)maks=tab[j][i];
                            }
                    for(int j=0;j<N;j++){
                            if(tab2[j][i]>maks)tab2[j][i]=maks;
                            }
                    }
            for(int i=0;i<N;i++){
                    for(int j=0;j<M;j++){
                            if(tab[i][j]!=tab2[i][j]){
                                                      zle=1;
                                                      break;
                                                      }
                            }
                    }
            if(zle==0)cout<<"Case #"<<q<<": YES\n";
            else cout<<"Case #"<<q<<": NO\n";
            }
    return 0;
}
