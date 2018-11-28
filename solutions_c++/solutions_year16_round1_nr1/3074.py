#include <iostream>
#include <climits>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        string S, ret = "";
        cin >> S;

        ret = S.at(0);

        for (int j = 1 ; j < S.size(); j++) {
            if (S.at(j) >= ret.at(0))
                ret = S.at(j) + ret;
            else
                ret = ret + S.at(j); 
        }
        cout << "Case #" << (i+1) << ": " << ret << endl;
    }
    return 0;
}