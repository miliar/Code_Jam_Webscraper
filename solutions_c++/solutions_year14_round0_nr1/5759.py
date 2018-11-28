#include <iostream>
#include <algorithm>
#define maxn 4
using namespace std;

int a[maxn][maxn];
int b[maxn][maxn];

void solve(int aa, int bb, int num){
    int at[maxn], bt[maxn];
    int i, j, k = 0;
    int res = 0;
    for(i = 0;i < maxn;i++){
        for(j = 0;j < maxn;j++){
            if(a[aa-1][i] == b[bb-1][j]){
                k++;
                res = a[aa-1][i];
            }
        }
    }
    cout << "Case #" << num <<": ";
    if(k==1){
        cout << res << endl;
    }else if(k == 0){
        cout << "Volunteer cheated!" << endl;
    }else if(k > 1){
        cout << "Bad magician!" << endl;
    }
}

int main()
{
    int t;
    int aa, bb;
    int i, j;
    cin >> t;
    int tt = 0;
    while(t--){

        cin >> aa;
        for(i = 0;i < maxn;i++){
            for(j = 0;j < maxn;j++){
                cin >> a[i][j];
            }
        }
        cin >> bb;
        for(i = 0;i < maxn;i++){
            for(j = 0;j < maxn;j++){
                cin >> b[i][j];
            }
        }
        solve(aa, bb, ++tt);
    }
    return 0;
}
