#include <iostream>

using namespace std;



int main()
{
    std::ios::sync_with_stdio(false);
    int t,T;
    cin >> T;
    for (t=0; t<T; t++)
    {
        int K,C,S;
        cin >> K >> C>> S;
        cout <<"Case #"<<t+1<<": ";
        
        if (S==K) {
            for (int i=1; i<=K; i++) {
                cout << i << ' ';
            }
        }
        else{
            cout << "IMPOSSIBLE";
        }
        cout << endl;
    }
    return 0;
}

