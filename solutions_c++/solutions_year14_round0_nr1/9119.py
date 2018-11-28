#include <iostream>
#include <stack>
using namespace std;

int main() {
    int T,idx,row,col,jawab1,jawab2,cards1[4][4],cards2[4][4];
    
    cin >> T;
    for (idx=1;idx<=T;idx++) {
        std::stack<int> answer;
        cin >> jawab1;
        for (row=0; row<4; row++) {
            for (col=0; col<4; col++) {
                cin >> cards1[row][col];
            }
        }
        cin >> jawab2;
        for (row=0; row<4; row++) {
            for (col=0; col<4; col++) {
                cin >> cards2[row][col];
            }
        }
        
        for (row=0; row<4; row++) {
            for (col=0; col<4; col++) {
                if (cards1[jawab1-1][row] == cards2[jawab2-1][col]) {
                    answer.push(cards1[jawab1-1][row]);
                }
            }
        }
        
        /*cout << jawab1 << " " << jawab2 << "\n";
        for (row=0; row<4; row++) {
            for (col=0; col<4; col++) {
                cout << cards1[row][col] << " ";
            }
            cout << "\n";
        }
        for (row=0; row<4; row++) {
            for (col=0; col<4; col++) {
                cout << cards2[row][col] << " ";
            }
            cout << "\n";
        }*/
                
        if (answer.size() == 0)
            cout << "Case #" << idx << ": Volunteer cheated!" << endl;
        else if (answer.size() == 1)
            cout << "Case #" << idx << ": " << answer.top() << endl;
        else if (answer.size() > 1)
            cout << "Case #" << idx << ": Bad magician!" << endl;
    }
}
