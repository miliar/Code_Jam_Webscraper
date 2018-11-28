#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>

using namespace std;

int T, tcase, N;
vector<pair<int,int> > pi;

int main()
{
    int p;
    cin >> T;
    tcase = 1;
    while (tcase<=T) {
        cin >> N;
        
        pi.clear();
        for (int i=0; i<N; ++i) {
            cin >> p;
            pi.push_back(pair<int,int>(p,i));
        }

        cout << "Case #" << tcase++ << ":";
        while (true) {
            sort(pi.begin(), pi.end(),
                    [](const pair<int,int>& l, const pair<int,int>& r){ return (l.first>r.first);});

            if (pi[0].first>1) {
                if (pi[1].first>1) {
                    cout << " " << (char)('A'+pi[0].second) << (char)('A'+pi[1].second);
                    pi[0].first -= 1;
                    pi[1].first -= 1;
                } else {
                    cout << " " << (char)('A'+pi[0].second) << (char)('A'+pi[0].second);
                    pi[0].first -= 2;
                }
            } else if (pi[0].first==1) {
                int cnt = count_if(pi.begin(), pi.end(), [](const pair<int,int>& i){return (i.first==1);});
                if (cnt==2 || cnt>3) {
                    cout << " " << (char)('A'+pi[0].second) << (char)('A'+pi[1].second);
                    pi[0].first -= 1;
                    pi[1].first -= 1;
                } else {
                    cout << " " << (char)('A'+pi[0].second);
                    pi[0].first -= 1;
                }
            } else {
                cout << endl;
                break;
            }
        }
    }
}
