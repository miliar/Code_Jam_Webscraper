#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{

    ifstream in("/home/akram/this.pc/Workspace/C++/google-jam/Problem-A_Standing-Ovation/input.in");
    ofstream out("/home/akram/this.pc/Workspace/C++/google-jam/Problem-A_Standing-Ovation/output.out");


    int T;
    int can_stand = 0;
    int friends = 0;
    int est_friends = 0;

    string s;
    int s_max;

    in >> T;
    cout << T << endl;
    int number = T + 1;

    for (; T > 0; --T) {
        can_stand = 0;
        friends = 0;

        in >> s_max;
        cout << s_max << endl;
        in >> s;
        cout << s << endl;

        for (int i = 0; i <= s_max; ++i) {
            if(i <= can_stand || s[i] == '0')
                can_stand += (s[i] - '0');
            else
                while(1) {
                    est_friends++;
                    if(i <= (can_stand + est_friends) ) {
                        can_stand += est_friends + (s[i] - '0');
                        friends += est_friends;
                        est_friends = 0;
                        break;
                    }
                }
        }
        out << "Case #" << (number - T) <<": " << friends << endl;
    }
    in.close();
    out.close();

    return 0;
}
