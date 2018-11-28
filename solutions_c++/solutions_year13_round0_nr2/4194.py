#include<iostream>
#include<vector>

using namespace std;

int main(void){
    int T;
    cin>>T;
    for(int tcase = 1; tcase <= T; ++tcase){
        int N,M;
        cin>>N>>M;
        int L[N][M];
        for(int i=0;i<N;++i){
            for(int j=0;j<M;++j){
                cin>>L[i][j];
            }
        }
        
        bool ok = true;
        for(int k=0; k<N && ok; ++k){
            for(int l=0; l<M && ok; ++l){
                int val = L[k][l];
                bool row, column;
                row=column=true;
                for(int i=0;i<N;++i){
                    if(L[i][l] > val) column = false;
                }
                for(int i=0;i<M;++i){
                    if(L[k][i] > val) row = false;
                }
                ok &= column || row;
            }
        }
        
        cout<<"Case #"<<tcase<<": "<<((ok)?"YES":"NO")<<endl;
    }
}
