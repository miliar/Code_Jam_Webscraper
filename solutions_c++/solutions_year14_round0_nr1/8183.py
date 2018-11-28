#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int tests, ans[2];
int a, b, c, d;
vector< vector<int> > chosen(2, vector<int>(4, 0));

int main(int argc, char const* argv[]){
    cin >> tests;

    int num_case = 1;
    for (int i = 0; i < tests; i++) {
        for (int j = 0; j < 2; j++) {
            cin >> ans[j];
            for (int k = 0; k < 4; k++) {
                cin >> a >> b >> c >> d;

                if (ans[j]-1 == k){
                    chosen[j][0] = a;
                    chosen[j][1] = b;
                    chosen[j][2] = c;
                    chosen[j][3] = d;
                }
            }
        }

        int equal_val = 0;
        int equal_qtd = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (chosen[0][i] == chosen[1][j] && chosen[0][i] != 0){
                    equal_val = chosen[0][i];
                    equal_qtd++;
                }
            }
        }

        if (equal_qtd > 1){
            cout << "Case #" << num_case << ": Bad magician!" << endl;
        }
        else if (equal_qtd == 1){
            cout << "Case #" << num_case << ": " << equal_val << endl;
        }
        else {
            cout << "Case #" << num_case << ": Volunteer cheated!" << endl;
        }

        num_case++;
    }

    return 0;
}
