#include<iostream>
#include<vector>

using namespace std;

int main()
{
    int T; cin >> T;

    for(int t = 0; t < T; ++t) {
        vector<int> count(17);

        for(int c = 0; c < 2; ++c) {
            int ans;
            vector< vector<int> > board(4, vector<int>(4));
            cin >> ans;
            for(int i = 0; i < 4; ++i)
                for(int j = 0; j < 4; ++j)
                    cin >> board[i][j];

            for(int i = 0; i < 4; ++i)
                ++count[board[ans-1][i]];
        }

        int c = 0;
        int pos = 0;
        for(int i = 0; i < count.size(); ++i) {
            if(count[i] == 2) {
                pos = i;
                ++c;
            }
        }

        cout << "Case #" << t+1 << ": ";
        if(c == 0)
            cout << "Volunteer cheated!" << endl;
        else if(c == 1)
            cout << pos << endl;
        else
            cout << "Bad magician!" << endl;
    }

    return 0;
}
