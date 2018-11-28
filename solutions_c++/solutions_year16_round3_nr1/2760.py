#include <bits/stdc++.h>
using namespace std;

const int MAX = 26;
int test, n, a[MAX], sum;

int main(){
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    cin >> test;
    for (int ii = 1; ii <= test; ++ii){
        cin >> n;
        sum = 0;
        if (ii == 19){
         int tmp = 0;
        }
        for (int i = 0; i < n; ++i){
            cin >> a[i];
            sum += a[i];
        }

        cout << "Case #" << ii << ":";
        if (sum == 2){
            cout << " ";
            for (int i = 0; i < n; ++i)
            if (a[i] > 0)
                cout << char(i + 'A');
            cout << endl;
            continue;
        }

        while (1){
            int pos1 = 0, pos2 = -1;
            for (int i = 1; i < n; ++i)
            if (a[i] > a[pos1])
                pos1 = i;

            for (int i = 0; i < n; ++i)
            if (i != pos1 && (pos2 == -1 || a[pos2] < a[i]))
                pos2 = i;

            if (a[pos1] == a[pos2] && a[pos1] + a[pos2] == sum){
                for (int j = 1; j <= a[pos1]; ++j)
                    cout << " " << char(pos1 + 'A') << char(pos2 + 'A');
                break;
            }

            cout << " " << char(pos1 + 'A');
            --a[pos1];
            --sum;
        }

        cout << endl;
    }
    return 0;
}
