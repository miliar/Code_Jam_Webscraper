#include <iostream>

using namespace std;

int grid[2501];

void initGrid(){
    for(int i = 1; i <= 2500; i++)
            grid[i] = 0;
}

int main()
{
    int t, n, cont, g, k;
    cin >> t;
    for(int i = 1; i <= t; i++){
        cin >> n;
        initGrid();
        cout << "Case #" << i << ": ";
        for(int j = 1; j <= n*(2*n-1); j++){
            cin >> g;
            grid[g]++;
        }
        cont = 1;
        k = 1;
        while(cont <= n){
            if(grid[k] % 2 != 0){
                cout << k;
                if(cont < n)
                    cout << " ";
                cont++;
            }
            k++;
        }
        cout << endl;
    }
    return 0;
}
