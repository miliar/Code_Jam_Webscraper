#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <deque>
#include <string>
#include <string.h>
#include <vector>
#include <stack>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <time.h>
#include <bitset>
#include <list>

using namespace std;

typedef long long LL;
typedef pair<int,int> pii;
typedef pair<pii,pii> ppi;
typedef pair<LL,LL> pll;
typedef pair<string,string> pss;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vii;
typedef vector<LL> vl;
typedef vector<vl> vvl;
typedef vector<string> vstr;
typedef vector<char> vc;

double EPS = 1e-9;
int INF = 2000000000;
long long INFF = 8000000000000000000LL;
double PI = acos(-1);
int dirx[8] = {-1,0,0,1,-1,-1,1,1};
int diry[8] = {0,1,-1,0,-1,1,-1,1};

#define FOR(a,b,c) for (int (a)=(b);(a)<(c);++(a))
#define FORN(a,b,c) for (int (a)=(b);(a)<=(c);++(a))
#define FORD(a,b,c) for (int (a)=(b);(a)>=(c);--(a))
#define FORSQ(a,b,c) for (int (a)=(b);(a)*(a)<=(c);++(a))
#define FORL(a,b,c) for (LL (a)=(b);(a)<=(c);++(a))
#define FORLSQ(a,b,c) for (int (a)=(b);(LL)(a)*(LL)(a)<=(c);++(a))
#define FORC(a,b,c) for (char (a)=(b);(a)<=(c);++(a))
#define REP(i,n) FOR(i,0,n)
#define REPN(i,n) FORN(i,1,n)
#define REPD(i,n) FORD(i,n,1)
#define MAX(a,b) a = max(a,b)
#define MIN(a,b) a = min(a,b)
#define SQR(x) ((x) * (x))
#define RESET(a,b) memset(a,b,sizeof(a))
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define ALL(v) v.begin(),v.end()
#define ALLA(arr,sz) arr,arr+sz
#define SIZE(v) (int)v.size()
#define SORT(v) sort(ALL(v))
#define REVERSE(v) reverse(ALL(v))
#define SORTA(arr,sz) sort(ALLA(arr,sz))
#define REVERSEA(arr,sz) reverse(ALLA(arr,sz))
#define PERMUTE next_permutation
#define TC(t) while(t--)
#define READ(n,data) {scanf("%d",&n); REPN(i,n) scanf("%d",&data[i]);}

inline string IntToString(int a){
    char x[100];
    sprintf(x,"%d",a); string s = x;
    return s;
}

inline int StringToInt(string a){
    char x[100]; int res;
    strcpy(x,a.c_str()); sscanf(x,"%d",&res);
    return res;
}

inline string GetString(void){
	char x[1000005];
	scanf("%s",x); string s = x;
	return s;
}

inline string uppercase(string s){
	int n = SIZE(s);
	REP(i,n) if (s[i] >= 'a' && s[i] <= 'z') s[i] = s[i] - 'a' + 'A';
	return s;
}

inline string lowercase(string s){
	int n = SIZE(s);
	REP(i,n) if (s[i] >= 'A' && s[i] <= 'Z') s[i] = s[i] - 'A' + 'a';
	return s;
}

inline void OPEN (string s) {
    freopen ((s + ".in").c_str (), "r", stdin);
    freopen ((s + ".out").c_str (), "w", stdout);
}

int main() {

  int T;

  cin >> T;

  for (int i = 1; i <= T; i++) {
    int N, min = 0;
    string S[101];
    string shortest[101];
    int position[101];
    bool isValid = true;
    /** Reading Inputs */
    for (int j = 0; j < 101; j++) position[j] = 0;
    cin >> N;

    for (int j = 0; j < N; j++) cin >> S[j];

    /** Process */
    for (int j = 0; j < N; j++) {
        shortest[j] = S[j][0];
        for (int k = 1; k < S[j].length(); k++) {
            if (S[j][k] != S[j][k-1]) shortest[j] = shortest[j] + S[j][k];
        }
    }

    for (int j = 1; j < N; j++) if (shortest[j] != shortest[j-1]) isValid = false;

    if (isValid) {
        string sho = shortest[0];
        for (int j = 0; j < sho.length(); j++) {
            int temp_min = 100000000;
            char temp_char = sho[j]; // current character
            for (int counter = 1; counter <= 100; counter++) {
                int local_sum = 0;
                for (int k = 0; k < N; k++) {
                    // check over all strings
                    int counta = 0;
                    int prev_location = position[k];
                    while (true) {
                        if (prev_location == S[k].length()) break; // all checked
                        if (S[k][prev_location] == temp_char) {
                            counta++;
                            prev_location++;
                        } else break;
                    }
                    if (counter == 100) position[k] = prev_location;
                    int temp_cal = counter - counta;
                    if (temp_cal < 0) temp_cal = temp_cal * -1;
                    local_sum += temp_cal;
                }
                if (temp_min > local_sum) temp_min = local_sum;
            }
            min += temp_min;
        }
    }

    /** Output */
    cout << "Case #" << i << ": ";
    if (isValid) cout << min;
    else cout << "Fegla Won";
    cout << endl;

  }

  return 0;
}
/** Created by freedomofkeima */
