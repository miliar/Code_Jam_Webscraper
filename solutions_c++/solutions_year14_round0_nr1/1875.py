#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int tc, ori_tc;
    cin >> tc;

    ori_tc = tc;

    while (tc) {
        int bef[4][4];
        int aft[4][4];

        int bef_row, aft_row;
        cin >> bef_row;
        for(int i = 0; i < 4; i ++)
            for(int j = 0; j < 4; j ++)
                cin >> bef[i][j];

        cin >> aft_row;
        for(int i = 0; i < 4; i ++)
            for(int j = 0; j < 4; j ++)
                cin >> aft[i][j];     

        bef_row --;
        aft_row --;

        vector<int> both;
        for(int i = 0; i < 4; i ++) {
            for(int j = 0; j < 4; j ++) {
                if(bef[bef_row][i] == aft[aft_row][j])
                    both.push_back(bef[bef_row][i]);
            }
        }
        cout << "Case #" << ori_tc - tc + 1 << ": ";
        if(both.size() == 1) {
            cout <<  both[0] << endl;
        }
        else if(both.size() == 0) {
            cout << "Volunteer cheated!" << endl;
        }
        else {
            cout << "Bad magician!" << endl;
        }
        tc --;
    }
}
