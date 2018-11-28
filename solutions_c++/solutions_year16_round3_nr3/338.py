#include <fstream>
#include <iostream>
#include <string>
#include <cmath>

#define BUFSIZE 1000

using namespace std;

int gjp[10][10], gjs[10][10], gps[10][10];
int was[10][10][10];
int used[1000][3];
int j, p, s, k;
int count;

int solve(int day, int last) {

    int result = day;
    for (int ji = 0; ji < j; ji++) {
        for (int pi = 0; pi < p; pi++) {
            for (int si = 0; si < s; si++) {
                int cur = 100*ji + 10*pi + si;
                if (cur > last && was[ji][pi][si] == 0 && gjp[ji][pi] < k && gjs[ji][si] < k && gps[pi][si] < k) {
                    gjp[ji][pi]++;
                    gjs[ji][si]++;
                    gps[pi][si]++;
                    was[ji][pi][si] = 1;
                    result = max(solve(day + 1, cur), result);
                    gjp[ji][pi]--;
                    gjs[ji][si]--;
                    gps[pi][si]--;
                    was[ji][pi][si] = 0;
                }
            }
        }
    }

    if (result == day && result > count) {

        int tcnt = 0;
        for (int ji = 0; ji < j; ji++) {
            for (int pi = 0; pi < p; pi++) {
                for (int si = 0; si < s; si++) {
                    if (was[ji][pi][si] == 1) {
                        used[tcnt][0] = ji+1;
                        used[tcnt][1] = pi+1;
                        used[tcnt][2] = si+1;
                        tcnt++;
                    }
                }
            }
        }
        count = result;

    }
    return result;

}

int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");

    int tests;
    char buf[BUFSIZE];

    //int j, p, s, k;
    int jp[10][10], js[10][10], ps[10][10];

    cin >> tests;
    cin.getline(buf, BUFSIZE);

    for (int t = 0; t < tests; t++) {

        cin >> j >> p >> s >> k;

        cout << "Case #" << t+1 << ": ";

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                jp[i][j] = 0;
                js[i][j] = 0;
                ps[i][j] = 0;
            }
        }

        count = 0;

        for (int ji = 0; ji < j; ji++) {
            for (int pi = 0; pi < p; pi++) {
                for (int si = 0; si < s; si++) {
                    if (jp[ji][pi] < k && js[ji][si] < k && ps[pi][si] < k) {
                        jp[ji][pi]++;
                        js[ji][si]++;
                        ps[pi][si]++;
                        used[count][0] = ji+1;
                        used[count][1] = pi+1;
                        used[count][2] = si+1;
                        count++;
                    }
                }
            }
        }


        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                for (int l = 0; l < 10; l++) {
                    was[i][j][l] = 0;
                }
                jp[i][j] = 0;
                js[i][j] = 0;
                ps[i][j] = 0;
            }
        }

        if (k < 3) {
            count = solve(0, -1);
        }

        cout << count << endl;
        for (int i = 0; i < count; i++) {
            cout << used[i][0] << " " << used[i][1] << " " << used[i][2] << endl;
        }

    }

    cin.close();
    cout.close();

    return 0;
}
