# include <bits/stdc++.h>
using namespace std;

long long P2[70];

int graph[55][55];

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large-output.txt", "w", stdout);
    long long ul = 2e18, prod = 1, m, sz = 2;
    P2[0] = P2[1] = 0;
    while(prod <= ul){
        P2[sz++] = prod;
        prod <<= 1;
    }
    int cases, caseno=0, b, completeNodes;
    cin >> cases;
    while(cases--){
        cin >> b >> m;
        for (int i=1; P2[i]<=m; i++) completeNodes = i;
        cout << "Case #" << ++caseno << ":";
        if (completeNodes > b || (completeNodes==b && (P2[completeNodes]!=m))) cout << " IMPOSSIBLE\n";
        else{
            cout << " POSSIBLE\n";
            memset(graph, 0, sizeof(graph));
            for (int i=1; i<=completeNodes; i++){
                for (int j=i+1; j<=completeNodes; j++) graph[i][j] = 1;
            }
            m -= P2[completeNodes];
            for (int i=completeNodes-1; i && m; i--){
                if (P2[i] <= m){
                    m -= P2[i];
                    graph[i][completeNodes+1] = 1;
                }
            }
            for (int i=completeNodes; i<b; i++) graph[i][i+1] = 1;
            for (int i=1; i<=b; i++){
                for (int j=1; j<=b; j++) cout << graph[i][j];
                cout << endl;
            }
        }
    }
    return 0;
}
