/*

Ken's optimal strategy is to place the smallest block larger than chosenNaomi, 
if it exists, otherwise place smallest block

Ken's score is independent of Naomi's order of placing the blocks (Still have to prove completely)

Naomi's optimal strategy of playing deceitful war is to place her smallest block
and force ken to remove either smallest block (if beatable) or largest block (if not)

*/

#include <iostream>
#include <algorithm>
#include <set>
#include <sstream>

using namespace std;

typedef long long ll;

stringstream ss;

#define DEBUG(A) cerr << "\tDEBUG: " << #A << " = " << A << "\n"

const int MAXN = 1010;

float naomi[MAXN], ken[MAXN];
int N;

class game {
	public:
	int naomiscore;
	static const float EPSILON = 1e-7;
	set<float> n, k;
	game(float naomi[MAXN], float ken[MAXN], int N) {
		for ( int i = 0 ; i < N ; i++ ) {
			n.insert(naomi[i]);
			k.insert(ken[i]);
		}
		naomiscore = 0;
	}
	void playnaomi(float chosenaomi) {
		chosenaomi-=EPSILON;
		set<float>::iterator it;
		it = n.lower_bound(chosenaomi);
		n.erase(it);
	}
	void playken(float tellnaomi) {
		tellnaomi-=EPSILON;
		float kenmax = *(k.rbegin());
		set<float>::iterator it;
		if ( kenmax > tellnaomi ) {
			it = k.lower_bound(tellnaomi);
		} else {
			it = k.begin();
			naomiscore += 1;
		}
		k.erase(it);
	}
	void playwar() {
		while ( !n.empty() ) {
			float t = *(n.begin());
			playnaomi(t);
			playken(t);
		}
	}
	void playdeceitwar() {
		while ( !n.empty() ) {
			float t = *(n.begin());
			float u = *(k.begin());
			playnaomi(t);
			if ( t < u ) { // if your smallest cannot beat ken's smallest
				playken(*(k.rbegin())); // make ken remove his largest
			} else {
				playken(1); // make ken remove his smallest
			}
		}
	}
};

void testCase() {
	cin >> N;
	for ( int i = 0 ; i < N ; i++ ) {
		cin >> naomi[i];
	}
	for ( int i = 0 ; i < N ; i++ ) {
		cin >> ken[i];
	}
	game g1(naomi, ken, N);
	game g2(naomi, ken, N);
	g1.playdeceitwar();
	g2.playwar();
	ss << g1.naomiscore << ' ' << g2.naomiscore;
}

int main() {
	int t;
	cin >> t;
	for ( int i = 0 ; i < t ; i++ ) {
		ss << "Case #"<<(i+1)<<": ";
		testCase();
		ss << endl;
	}
	cout << ss.str();
	return 0;
}

