#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(int ac, char** av) {
    int T;
    cin >> T;
    for (int cs=1; cs<=T; ++cs) {
        int N, M;
        cin >> N >> M;
        vector<int> rm(N);
        vector<int> cm(M);
        
        vector<vector<int> > lawn(N, vector<int>(M));

        for (int row=0; row<N; ++row)
            for (int col=0; col<M; ++col) {
                int h;
                cin >> h;
                lawn[row][col] = h;
                if (rm[row]<h)rm[row]=h;
                if (cm[col]<h)cm[col]=h;
            }

        for (int row=0; row<N; ++row)
            for (int col=0; col<M; ++col)
                if (lawn[row][col] != min(rm[row], cm[col])) {
                    cout << "Case #" << cs << ": NO\n";
                    goto next_case;
                }

        cout << "Case #" << cs << ": YES\n";
      next_case:
        ;
    }
}
