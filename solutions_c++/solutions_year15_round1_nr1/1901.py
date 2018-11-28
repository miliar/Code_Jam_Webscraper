#include <bits/stdc++.h>

using namespace std;

int A[10000+500];

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int casos;
    cin>>casos;
    for(int cas=1;cas<=casos;cas++){
        int N;
        cin>>N;
        for(int i=0;i<N;i++) cin>>A[i];
        int maxdif=0, sumdif=0, prim=0;
        for(int i=1;i<N;i++){
            if(A[i]<A[i-1]){
                maxdif=max(A[i-1]-A[i], maxdif);
                sumdif+=A[i-1]-A[i];
            }
        }
        for(int i=0;i<N-1;i++){
            prim+=min(maxdif, A[i]);
        }
        cout<<"Case #"<<cas<<": "<<sumdif<<" "<<prim<<endl;
    }
}
