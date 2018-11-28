#include<iostream>
#include<string>
#include<vector>
using namespace std;
vector<vector<int> > vov;
string isp(int N, int M) {
    int i,j,h,f1,f2,k;
    for(i=0; i<N; i++) {
        for(j=0; j<M; j++) {
            f1=f2=0;
            h=vov[i][j];
            for(k=0; k<N; k++) {
                if(vov[k][j]>h) {
                    f1=1;
                    break;
                }
            }
            for(k=0; k<M; k++) {
                if(vov[i][k]>h) {
                    f2=1;
                    break;
                }
            }
            if(f1 && f2) {
                return "NO";
            }
        }
    }
    return "YES";
}
                
            
int main() {
    int T,N,M,i,j,k;
    cin>>T;
    for(i=1; i<=T; i++) {
        cin>>N>>M;
        vov=vector<vector<int> > (N, vector<int>(M,0));
        for(j=0; j<N; j++) {
            for(k=0; k<M; k++) {
                cin>>vov[j][k];
            }
        }
        cout<<"Case #"<<i<<": "<<isp(N,M)<<endl;
    }
    return 0;
}
