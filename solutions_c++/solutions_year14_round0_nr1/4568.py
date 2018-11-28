#include <fstream>

using namespace std;

int main()
{
    ifstream cin("A.in");
    ofstream cout("A.out");
    const string output[] = {"Bad magician!", "Volunteer cheated!" };
    int T;
    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        cout << "Case #" << testCase << ": ";
        int answer[22];
        int grid[2][4][4];
        for (int k = 0; k < 2; k++) {
            cin >> answer[k];
            answer[k]--;
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    cin >> grid[k][i][j];
                }
            }
        }
        
        int intersectionCard = 0;
        int card = -1;
        for (int i = 0; i < 4; i++) {  
            for (int j = 0; j < 4; j++) {
                if (grid[0][answer[0]][i] == grid[1][answer[1]][j]) {
                    card = grid[0][answer[0]][i];
                    intersectionCard++;
                }
            }
        }
        
        if (intersectionCard == 0) {
            cout << output[1] << "\n";
        } else
        if (intersectionCard == 1) {
            cout << card << "\n"; 
        } else {
            cout << output[0] << "\n";
        }
    }
    return 0;
}
