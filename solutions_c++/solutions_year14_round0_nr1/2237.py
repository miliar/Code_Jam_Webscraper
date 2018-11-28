// 1A_A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main(int argc, char* argv[])
{
    freopen ("A-small-attempt0.in", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int k = 0; k < T; ++k) {
        int first, second;
        cin >> first;
        std::set <int> firstV, secondV;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                int buf;
                cin >> buf;
                if (i == first - 1) {
                    firstV.insert (buf);
                }
            }
        }
        cin >> second;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                int buf;
                cin >> buf;
                if (i == second - 1) {
                    secondV.insert (buf);
                }
            }
        }
        vector <int> answer;
        for (std::set <int>::const_iterator iter = secondV.begin (); iter != secondV.end (); ++iter) {
            if (firstV.find (*iter) != firstV.end ()) {
                answer.push_back (*iter);
            }
        }
        cout << "Case #" << k + 1 << ": ";
        if (answer.size () == 1) {
            cout << answer.front () << endl;
        }
        else if (answer.size () == 0) {
            cout << "Volunteer cheated!\n";
        }
        else {
            cout << "Bad magician!\n";
        }
    }
	return 0;
}

