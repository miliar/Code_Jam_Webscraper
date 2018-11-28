#include <bits/stdc++.h>
using namespace std;

#define TRACE(x) cout << #x << " = " << x << endl

const int INF = 1000000000;

int N; // number of sentences
vector<string> sentences;

map<string, int> wrdmap;
int nwords;
int wordmask[100000];

void processWords() {
	nwords = 0;
	for (int i = 0; i < N; i++) {
		stringstream input(sentences[i]);
		string wrd;
		while (input >> wrd) {
			int k;
			if (wrdmap.find(wrd) != wrdmap.end()) {
				k = wrdmap[wrd];
			} else {
				k = nwords;
				wrdmap[wrd] = k;
				nwords++;
				wordmask[k] = 0;
			}
			//TRACE(wrd);
			wordmask[k] |= (1<<i);
		}
	}
}

int solve() {
	int ans = 0;
	
	//TRACE(N);
	//TRACE(wrdmap.size());
	
	if (N == 2) {
		// ans is *at least* overlap between first and second bits
		for (int j = 0; j < nwords; j++) {
			if ((wordmask[j] & 3) == 3)
				ans++;
		}
		return ans;
	}
	
	// otherwise, need more
	ans = INF;
	for (int ss = 0; ss < (1<<(N-2)); ss++) {
		int eng = (ss<<2) + 1; // first english, second french
		int frc = ((1<<N) - 1) ^ eng;
		// all 1 bits are english, 0 bits are french
		int cnt = 0;
		
		for (int j = 0; j < nwords; j++) {
			if ((wordmask[j] & eng) && (wordmask[j] & frc))
				cnt++;
		}
		ans = min(ans, cnt); 
	}
	
	assert(ans < INF);
	
	return ans;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> N;
		string s;
		getline(cin, s); //empty
		sentences.clear();
		wrdmap.clear();
		
		for (int i = 0; i < N; i++) {
			getline(cin, s);
			//TRACE(s);
			sentences.push_back(s);
		}
		
		processWords();
		
		int res = solve();
		
		cout << "Case #" << icase << ": " << res << endl;
	}
	return 0;
}

