#include <iostream>
#include <cmath>
#include <iomanip>
#include <deque>

using namespace std;

int main()
{

    int t; cin >> t;

    for(int T = 1; T <= t; T++){

        string w; cin >> w;
        deque<char> D;

        D.push_back( w[0] );
        for(int i = 1; i < w.size(); i++){

            if( D.front() <= w[i]){
                D.push_front(w[i]);
            }else
                D.push_back(w[i]);
        }

        cout << "Case #" << T << ": ";

        while(!D.empty()){
            cout << D.front();
            D.pop_front();
        }

        cout << endl;
    }
    return 0;
}
