#include <iostream>
using namespace std;
int a[100][100];
int r[100],c[100];
bool test(int n, int m){
    memset(r,-1,sizeof r);
    memset(c,-1,sizeof c);
    for (int height = 0; height <=100; ++height){
        for (int i = 0; i < n; ++i){
            if (r[i]==-1){
                for (int j = 0; j < m; ++j){
                    if (!((a[i][j] < height && c[j]==a[i][j])||
                        (a[i][j] == height))){
                        break;
                    } else if (j==m-1){
                        r[i] = height;
                    }
                }
            }
        }
        for (int j = 0; j < m; ++j){
            if (c[j]==-1){
                for (int i = 0; i < n; ++i){
                    if (!((a[i][j] < height && r[i]==a[i][j])||
                        (a[i][j] == height))){
                        break;
                    } else if (i ==n-1 ){
                        c[j] = height;
                    }
                }
            }
        }
    }
    bool ans = true;
    for (int i = 0; i < n; ++i){
        if (r[i]==-1) ans = false;
    }
    for (int j = 0; j < m; ++j){
        if (c[j]==-1) ans = false;
    }
    return ans;
}
int main(){
    int t;
    cin >> t;
    for (int tcount = 1; tcount<=t;++tcount){
        int n,m;
        cin >> n >>m;
        for (int i = 0; i < n; ++i){
            for (int j = 0; j < m; ++j){
                cin >> a[i][j];
            }
        }
        bool ans = test(n,m);
        cout << "Case #" << tcount<<": " << (ans?"YES":"NO") << endl;
    }
}
