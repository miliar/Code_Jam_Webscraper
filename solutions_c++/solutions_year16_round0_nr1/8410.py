#include <bits/stdc++.h>

using namespace std;
int N, T, k, aux, f;
bool u[10];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("bla.out", "w", stdout);
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        memset(u, 0, sizeof(u));
        cin >> N;
        cout << "Case #" << t << ": ";
        if(N == 0) cout << "INSOMNIA\n";
            else
            {
                f = N; aux = 0; k = 0;
                while(k != 10){
                    aux++, f = aux * N;
                    //cout << f << "->";
                    while(f){
                        if(!u[f%10]) u[f%10] = 1, k++;
                        f /= 10;
                        }
                }
            cout << aux*N << "\n";
            }
    }
    return 0;
}

