#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;

const int N = 25;

int n;
char str[10000];
vector<int> row[N], E, F;
set<int> pre_eng, pre_frc, pre_ans, pre_st;
map<string, int> hash;
int cnt;

vector<int> parse(char *str) {
    stringstream sin(str);
    vector<int> ret;
    string s;
    while(sin >> s) {
        int c;
        if(hash.count(s)) c = hash[s];
        else c = hash[s] = cnt++;
        ret.push_back(c);
    }
    return ret;
}
void show(vector<int> vec) {
    for(int i = 0; i < vec.size(); ++i) {
        cout << vec[i] << ' ';
    }
    cout << endl;
}
int main() {
    int _, cas = 1;
	for(scanf("%d", &_); _--; ) {
        printf("Case #%d:", cas++);
        scanf("%d\n", &n);
        
        pre_st.clear();
        pre_eng.clear();
        pre_frc.clear();
        pre_ans.clear();
        hash.clear();
        cnt = 0;
        
        gets(str);
        E = parse(str);
        for(int k = 0; k < E.size(); ++k) pre_eng.insert(E[k]), pre_st.insert(E[k]);
        // show(E);
        
        gets(str);
        F = parse(str);
        for(int k = 0; k < F.size(); ++k) pre_frc.insert(F[k]), pre_st.insert(F[k]);
        show(F);
        
        
        for(set<int>::iterator it = pre_st.begin(); it != pre_st.end(); ++it) {
            if(pre_eng.count(*it) && pre_frc.count(*it)) pre_ans.insert(*it);
        }
        
        n -= 2;
        for(int i = 0; i < n; ++i) {
            gets(str);
            row[i] = parse(str);
            // show(row[i]);
        }
        
        int mask = 1 << n;
        int ans = ~0U >> 1;
        
        for(int i = 0; i < mask; ++i) {
            set<int> eng, frc, st;
            
            
            for(int j = 0; j < n; ++j) {
                if(i >> j & 1) {
                    for(int k = 0; k < row[j].size(); ++k) eng.insert(row[j][k]), st.insert(row[j][k]);
                }
                else {
                    for(int k = 0; k < row[j].size(); ++k) frc.insert(row[j][k]), st.insert(row[j][k]);
                }
            }
            
            int cur = 0;
            for(set<int>::iterator it = st.begin(); it != st.end(); ++it) {
                if((eng.count(*it) || pre_eng.count(*it)) && (frc.count(*it) || pre_frc.count(*it))) {
                    if(!pre_ans.count(*it)) cur++;
                }
            }
            
            ans = min(ans, cur + (int)pre_ans.size());
        }
        printf("%d\n", ans);
	}
	return 0;
}
