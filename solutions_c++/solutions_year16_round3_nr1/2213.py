#include <iostream>
#include <fstream>
#include <set>
#include <algorithm>
#include <functional>
#include <utility>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");
#define cin fin
#define cout fout

typedef pair<int, char> PIC;
const int MAXN = 26 + 5;
const int MAXP = 1000 + 5;

int T;
int n;
set<PIC, greater<PIC>> s;
int cnt;

int main()
{
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
        cnt = 0;

        cin >> n;
        for (int i = 0, temp; i < n; ++i)
        {
            cin >> temp;
            cnt += temp;
            if (temp != 0)
                s.insert(make_pair(temp, (char)('A' + i)));
        }
        cout << "Case #" << z << ":";
        for (PIC temp1, temp2; !s.empty(); )
        {
            cout << ' ';
            temp1 = *(s.begin());
            s.erase(temp1);
            cout << temp1.second;
            temp1.first -= 1;
            cnt -= 1;
            if (temp1.first != 0)
                s.insert(temp1);

            if (s.empty())
                break;

            temp2 = *(s.begin());
            s.erase(temp2);
            //cout << temp2.second;
            temp2.first -= 1;
            cnt -= 1;
            if (temp2.first != 0)
                s.insert(temp2);
            if (!s.empty() && cnt / (*(s.begin())).first < 2)
            {
                s.erase(temp2);
                temp2.first += 1;
                cnt += 1;
                s.insert(temp2);
            }
            else
                cout << temp2.second;
        }
        cout << endl;
    }
    return 0;
}

