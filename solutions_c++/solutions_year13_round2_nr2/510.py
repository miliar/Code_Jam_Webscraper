#include <iostream>
#include <ctime>
#include <cstdlib>
#include <iomanip>
#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>

#define present(col, el) (col.find(el) != col.end())

using namespace std;

ifstream fin("input.in");
ofstream fout("output.out");

set<pair<int, int> > diamond;

void turn(int rotateLeft, bool &was) {
    /*cout << "???" << diamond.size() << endl;
    for (set<pair<int, int> >::iterator it = diamond.begin(); it != diamond.end(); ++it) {
        cout << it->first << ';' << it->second << ' ';
    }
    cout << endl;*/
    int x = 0, y = 6;
    was = false;

    while (true) {
        if (y == 0) {
            diamond.insert(make_pair(x, y));
            //cout << "??" << diamond.size() << endl;
            return ;
        }

        bool left  = present(diamond, make_pair(x - 1, y - 1));
        bool right = present(diamond, make_pair(x + 1, y - 1));
        bool down  = present(diamond, make_pair(x, y - 2));

        if (down) {
            if (left == false && right == false) {
                was = true;
                //cout << "FFFFFFFFUUUUUUUUUUUUUUUUUUUUUUUUUU~~~~~~~~~`\n";
                if (rotateLeft == true) {
                    x--;
                }
                else {
                    x++;
                }
            }
            else {
                if (left && right) {
                    diamond.insert(make_pair(x, y));
                  //  cout << "?" << diamond.size() << endl;
                    return ;
                }
                x = (left) ? x + 1: x - 1;
            }
        }
        else {
            if (left && right) {
                diamond.insert(make_pair(x, y));
                return ;
            }
            if (left || right) {
                x = (left) ? x + 1: x - 1;
            }
        }
        y--;
    }
}

vector<set<pair<int, int> > > diamonds;

void dfs(int curTurn) {
    bool was;
    for (int i = 0; i < curTurn; ++i) {
        vector<set<pair<int, int> > > diamonds2;
        for (int i = 0; i < diamonds.size(); ++i) {
            diamond = diamonds[i];
            turn(0, was);
            diamonds2.push_back(diamond);
            if (was == true) {
                //cout << "HI!" << endl;
                diamond = diamonds[i];
                turn(1, was);
                diamonds2.push_back(diamond);
            }
        }
        diamonds = diamonds2;
    }
}


int main() {
    srand(time(NULL));
    int x, y, was, all = 1, n, T;
    fin >> T;
    fout << setprecision(8);
    for (int t = 0; t < T; ++t) {
        double propobility = 1.0;
        int answer = 0;
        int numVar = 1;

        fin >> n >> x >> y;
        diamonds.clear();
        set<pair<int, int> > temp;
        temp.insert(make_pair(0, 0));
        diamonds.push_back(temp);

        dfs(n - 1);

        for (int i = 0; i < diamonds.size(); ++i) {
            if (present(diamonds[i], make_pair(x, y))) {
                answer ++;
            }
        }

        numVar = diamonds.size();
        cout << answer << ' ' << numVar << endl;
        propobility = answer * 1.0 / numVar;
        fout << "Case #" << t + 1 << ": " << (double)propobility << endl;
    }
    return 0;
}
