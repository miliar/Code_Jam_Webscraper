#include <cassert>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fr(i,m,n) for(typeof(m) i=m; i!=n; i++)
#define fa(i,c) fr(i,(c).begin(),(c).end())

vector<int> getbagofwords(map<string,int>& dict) {
    string line;
    getline(cin, line);
    istringstream is(line);
    string word;
    vector<int> ret;
    while(is>>word) {
        if(!dict.count(word)) {
            int sz = dict.size();
            dict[word] = sz;
        }
        ret.push_back(dict[word]);
    }
    return ret;
}

int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
		cout << "Case #" << ts << ": ";
        int N; cin >> N; string s; getline(cin,s);
        N-=2;
        map<string, int> dict;
        vector<int> line1, line2;
        line1 = getbagofwords(dict);
        line2 = getbagofwords(dict);


        vector<vector<int> > lines(N);
        fu(i,0,N) lines[i] = getbagofwords(dict);
        int D = dict.size();
        vector<int> english(D);
        vector<int> french(D);
        fu(i,0,line1.size()) english[line1[i]]++;
        fu(i,0,line2.size()) french[line2[i]]++;

        int best=2000000000;
        fu(msk,0,(1<<N)) {
            fu(i,0,N) {
                for(int j: lines[i]) {
                    ((msk&(1<<i)) ? english: french)[j]++;
                }
            }
            int cur=0;
            fu(i,0,D) cur += (english[i]&&french[i]);
            best = min(best, cur);
            //cout << cur << endl;
            fu(i,0,N) {
                for(int j: lines[i]) {
                    (msk&(1<<i) ? english: french)[j]--;
                }
            }
        }

        if(N==0) {
                int cur=0;
                fu(i,0,D) cur += (english[i]&&french[i]);
                best = min(best, cur);
        }

        cout << best << endl;
	}
}
