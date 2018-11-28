#include <string>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <list>

using namespace std;

const double PI = 2 * acos(0);
const double eps = 1e-9;

#define SMALL
//#define LARGE
int main() {
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large-practice.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif

	int n, N;

    int res = -1;

	cin >> N;
    string trash;
    getline(cin, trash);

    for (int nn = 1; nn<N+1; ++nn) {
        res = -1;
        vector<int> input;

        string temp, s;

        cin >> n;

        for (int i=0; i<n; ++i){
            getline(cin, trash);
        }

        getline(cin, temp);
        stringstream ss(temp);
        while (ss >> s) {
            input.push_back(stoi(s));
        }
        for (int i=0; i<4-n; ++i){
            getline(cin, trash);
        }

        cin >> n;

        for (int i=0; i<n; ++i){
            getline(cin, trash);
        }

        getline(cin, temp);
        stringstream ss2(temp);
        while (ss2 >> s) {
            input.push_back(stoi(s));
        }
        for (int i=0; i<4-n; ++i){
            getline(cin, trash);
        }






        sort(input.begin(), input.end());
        for (int i=1; i<input.size(); ++i) {
            if (input[i] == input[i-1]) {
                if (res == -1)
                    res = input[i];
                else {
                    res = -2;
                    break;
                }
            }
        }




        cout<<"Case #" << nn << ": ";
        if (res != -1 && res != -2)
            cout << res;
        else if (res == -1)
            cout << "Volunteer cheated!";
        else
            cout << "Bad magician!";
        cout << endl;
    }
    return 0;
}
