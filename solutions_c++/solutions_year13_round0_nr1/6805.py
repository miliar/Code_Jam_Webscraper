#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;

    cin >> n;
    for (int j = 1; j <= n; j++) {
        string inp[10];
        bool flag = false;

        for (int i = 0; i < 4; i++) {
            string tmp;
            cin >> tmp;

            inp[i] = tmp;

            inp[4].append(tmp, 0, 1);
            inp[5].append(tmp, 1, 1);
            inp[6].append(tmp, 2, 1);
            inp[7].append(tmp, 3, 1);
            inp[8].append(tmp, i, 1);
            inp[9].append(tmp, 3 - i, 1);
        }

        string::size_type index;
        for (int i = 0; i < 10; i++) {
            if ((index = inp[i].find("T")) != string::npos) {
                if (inp[i].find("X") == string::npos)
                    inp[i].replace(index, 1, "O");
                else
                    inp[i].replace(index, 1, "X");  
            }


            if (inp[i] == "XXXX") {
                cout << "Case #" << j << ": X won" << endl;
                flag = true;
                break;
            }
            else if (inp[i] == "OOOO") {
                cout << "Case #" << j << ": O won" << endl;
                flag = true;
                break;
            }
        }

        if (!flag) {
            for (int i = 0; i < 4; i++) 
                if (inp[i].find(".") != string::npos) {
                    flag = true;
                    break;
                }

            if (flag)
                cout << "Case #" << j << ": Game has not completed" << endl;
            else 
                cout << "Case #" << j << ": Draw" << endl;
        }
    }

    return 0;
}
