#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t;
    cin >> t;
    for(int x = 1; x <= t; x++){
            int n, m;
            cin >> n >> m;
            int a[n][m];
            int max = -1;
            for(int i = 0; i < n; i++)
                    for(int j = 0; j < m; j++){
                            cin >> a[i][j];
                            if(a[i][j] > max) max = a[i][j];
                    }
            if(max == 1) cout << "Case #" << x << ": YES" << endl;
            else{
                 bool solution = true;
            for(int i = 0; i < n; i++)
                    for(int j = 0; j < m; j++)
                            if(a[i][j] < max){
                                       bool row = true;
                                       bool column = true;
                                       for(int k = 0; k < n; k++) if(a[k][j] != a[i][j]) column = false;
                                       for(int k = 0; k < m; k++) if(a[i][k] != a[i][j]) row = false;
                                       if(!row && !column) solution = false;
                            }
                            
                            if(solution) cout << "Case #" << x << ": YES" << endl;
                            else cout << "Case #" << x << ": NO" << endl;
            }
    }
    return EXIT_SUCCESS;
}
