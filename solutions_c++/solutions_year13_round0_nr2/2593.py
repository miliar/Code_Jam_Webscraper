#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
    int T,N,M;
    cin>>T;
    for(int t=1;t<=T;t++){
        cin>>N>>M;
        int map[N][M];
        bool ans[N][M];
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                cin>>map[i][j];
                ans[i][j]=0;
            }
        }
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                int o=0;
                for(int n=0;n<N;n++){
                    if(map[n][j]>map[i][j]){
                        o=1;
                        break;
                    }
                }
                if(o==0){
                    ans[i][j]=1;
                }
                o=0;
                for(int n=0;n<M;n++){
                    if(map[i][n]>map[i][j]){
                        o=1;
                        break;
                    }
                }
                if(o==0){
                    ans[i][j]=1;
                }
            }
        }
        int a=1;
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(ans[i][j]==0){
                    a=0;
                    break;
                }
            }
            if(a==0){
                break;
            }
        }
        if(a==0){
            cout<<"Case #"<<t<<": NO\n";
        }
        else{
            cout<<"Case #"<<t<<": YES\n";
        }
    }
    return 0;
}
