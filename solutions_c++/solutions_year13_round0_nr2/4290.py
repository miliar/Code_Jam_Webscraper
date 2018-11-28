// mrozik

#include <iostream>
#include <vector>
using namespace std;

vector<vector<int> > expected;
vector<int> col, row;

int N, M;

int main() {
    
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        cin>>N>>M;
        
        expected = vector<vector<int> >(N, vector<int>(M));
        for (int i=0; i<N; i++)
            for (int j=0; j<M; j++)
                cin>>expected[i][j];
        col = vector<int>(M, 0);
        row = vector<int>(N, 0);
        
        for (int i=0; i<N; i++)
            for (int j=0; j<M; j++) {
                col[j] = max(col[j], expected[i][j]);
                row[i] = max(row[i], expected[i][j]);
            }
        
        try {
            for (int i=0; i<N; i++)
                for (int j=0; j<M; j++)
                    if (expected[i][j]<col[j] && expected[i][j]<row[i])
                        throw false;

            cout<<"Case #"<<t<<": YES"<<endl;
        }
        catch (bool) {
            cout<<"Case #"<<t<<": NO"<<endl;
        }
    }
    
    return 0;
}
