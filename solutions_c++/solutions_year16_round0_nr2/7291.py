#include <cstdio>
#include <iostream>
#include <string>
#include <map>

using namespace std;

map<string, long long> my_map;

string reverse(string seq, int len) {
    string ret = seq.substr(0, len);

    for (int i = 0; i < len; i++) {
	if (ret[i] == '+') ret[i] = '-';
	else ret[i] = '+';
    }

    int sz = (int)seq.size();
    for (int i = len; i < sz; i++) ret += seq[i];
    // cout << "len: " << len << " ret : " << ret << endl;
    return ret;
}

long long go(string seq) {
    my_map[seq] = -1;
    long long &ret = my_map[seq];

    int sz = (int)seq.size();
    int cnt = 0;
    for (int i = 0; i < sz; i++) {
	if (seq[i] == '+') cnt++;
    }

    if (cnt == sz) {
	ret = 0;
    } else {
	for (int i = 1; i <= sz; i++) {
	    string next = reverse(seq, i);
	    long long next_ret;
	    if (my_map.find(next) == my_map.end()) {
		next_ret = go(next);
	    } else if (my_map[next] != -1) {
		next_ret = my_map[next];		
	    } else {
		continue;
	    }
	    // cout << "seq: " << seq << " next : " << next << " next_ret: " << next_ret << endl;
	    if (next_ret != -1) {
	    	if (ret == -1) ret = next_ret + 1;
	    	else ret = min(ret, next_ret+1);
	    }
	}
    }
    my_map[seq] = ret;

    return ret;
}

int main() {

    int TC;
    cin >> TC;

    for (int tc = 1; tc <= TC; tc++) {
	string seq;
	cin >> seq;

	printf("Case #%d: %lld\n", tc, go(seq));
	my_map.clear();
    }

    return 0;
}
