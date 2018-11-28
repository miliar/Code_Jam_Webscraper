#include<iostream>
#include<deque>
#include<algorithm>
#include<vector>
using namespace std;

const int MAXN = 2507;
int A[MAXN];

int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin>>T;
    for(int tt=1; tt<=T; tt++) {
        cout<<"Case #"<<tt<<": ";
        int N, n;
        cin>>N;
        for(int i=1; i<=MAXN; i++)
            A[i]=0;
        for(int i=1; i<=N*2-1; i++)
            for(int j=1; j<=N; j++) {
                cin>>n;
                A[n]++;
            }
        vector<int> V;
        for(int i=1; i<=MAXN; i++)
            //cout<<A[i]<<" ";
            if( A[i] != 0 && A[i]%2 == 1)
                V.push_back(i);
        sort(V.begin(), V.end());
        for(int i=0; i<V.size(); i++)
           cout<<V[i]<<" ";
        cout<<endl;
    }
    return 0;
}
