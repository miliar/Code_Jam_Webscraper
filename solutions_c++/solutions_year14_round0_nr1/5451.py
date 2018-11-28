#include <cstdio>
#include <iostream>

using namespace std;

int a[5][5], b[5][5], p, q, ans, cnt;

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> q;
        for(int i = 1; i <= 4; i++)
        for(int j = 1; j <= 4; j++)
            cin >> a[i][j];
        cin >> p;
        for(int i = 1; i <= 4; i++)
        for(int j = 1; j <= 4; j++)
            cin >> b[i][j];

        ans = 0;
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++){
                //cout << a[q][i] << " " << b[p][j] << endl;
                if(a[q][i] == b[p][j]){
                    ans++;
                    cnt = a[q][i];
                }
            }
        cout << "Case #" << t << ": ";
        if(ans == 1)
            cout << cnt << endl;
        else if(ans == 0)
            cout << "Volunteer cheated!" << endl;
        else
            cout << "Bad magician!" << endl;
    }

    return 0;
}
