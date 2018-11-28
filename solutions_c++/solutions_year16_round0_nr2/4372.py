#include <bits/stdc++.h>

using namespace std;


int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;

    int wcase = 0;
    string str;
    bool chng;
    int moves;
    while(t--)
    {
        wcase++;
        cin >> str;
        chng = true;
        moves = 0;
        for(int i = str.size()-1; i >= 0; i--)
        {
            if((str[i] =='-') == chng){
                moves++;
                chng = !chng;
            }
        }
        cout << "Case #" << wcase << ": ";
        cout << moves << "\n";
    }
}
