#include <iostream>
#include <string>
#include <sstream>

#define INF 1000000000
#define MAX_N 21
#define MAX_W 1005
#define PA pair<string, int>

using namespace std;

int tests, n, answer, cnt, en, j, k;
int tmp, t;
PA in[MAX_N * MAX_W];

int main() {
    cin >> tests;
    for (int test = 0 ; test < tests ; test ++) {
        cin >> n;
	en = 0;
	string s;
	getline(cin,s);
	for (int i = 0 ; i < n ; i ++) {
	    getline(cin,s);
	    //cout << "YYYYY" << s << "XXXX" << endl;

	    istringstream iss(s);
	    string w;
	    while(iss >> w) {
		in[en] = PA(w, i);
		en ++;
	    }
	}
	sort(in, in + en);
	answer = INF;
	for (int i = 2 ; i < (1<<n) ; i +=4) {
	    cnt = 0;
	    j = 0;
	    while (j < en) {
		tmp = -1;
		while (true) {
		    t = (i & (1<<in[j].second));
		    if (t != 0) {
			t = 1;
		    }
		    //printf("XX %d %d %d %d\n", j, t, i, in[j].second);
		    if (tmp == -1) {
			tmp = t;
		    } else if (tmp != t) {
			tmp = 3;
		    }
		    j ++;
		    //printf("AA %d \n", j);
		    if (j == en or in[j - 1].first != in[j].first) {
			//printf("BB\n");
			break;
		    }
		}
		if (tmp == 3) {
		    cnt ++;
		}
	    }
	    if (cnt < answer) {
		answer = cnt;
	    }
	}
	cout << "Case #" << test + 1 << ": " << answer << endl;
    }
    return 0;
}
