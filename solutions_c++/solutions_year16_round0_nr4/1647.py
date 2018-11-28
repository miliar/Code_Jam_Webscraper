#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

int main()
{

    int t;
    cin >> t;

    for (int c=1; c<=t; ++c)
    {
        int K, C, S;
        cin >> K;
        cin >> C;
        cin >> S;

        cout << "Case #" << c << ":";
        for(int i =1; i<=K; i++){
            cout << " " << i;
        }
        cout << endl;
    }
    return 0;
}
