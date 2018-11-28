#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> ii;
typedef pair<ld, ld> dd;
typedef pair<ll, ll> llll;
typedef vector<ll> vi;
typedef vector<ii> vii;
typedef vector<ll> vll;
typedef vector<llll> vllll;
typedef vector<vi> vvi;
typedef vector<ld> vd;
typedef vector<dd> vdd;
#define INF 1000000000
#define EPS 1e-9
#define rep(i, a, b) for (int i = int(a); i < int(b); i++)
#define contains(x, y) ((x).find(y)!=end(x))
#define mk make_pair
#define pb push_back
#define fst first
#define snd second
#define sz(a) ll((a).size())
#define endl "\n"

vi his;

vvi words;
vi numb;
int t;

int foundNumber(){

	for(int i = 0; i < his.size(); i++){
		if(his[i] != 0) return 0;
	}

	return 1;
}

void printNumber(){
	printf("Case #%d: ", t);
	for(int i = 0; i < numb.size(); i++) printf("%lld", numb[i]);
	printf("\n");
}

int hasWord(int pos){


	for(int i = 0; i < his.size(); i++){
		if(his[i] < words[pos][i]) return 0;
	}

	return 1;
}

void removeWord(int pos){
	for(int i = 0; i < his.size(); i++){
		his[i] -= words[pos][i];
	}
}

void addWord(int pos){
	for(int i = 0; i < his.size(); i++){
		his[i] += words[pos][i];
	}
}

int tryrec(int pos){

	if(pos >= words.size()){

		if(foundNumber()){
			printNumber();
			return 1;
		}
		return 0;
	}

	int found = 0;
	if(hasWord(pos)){
		removeWord(pos);
		numb.pb(pos);
		found = tryrec(pos);
		numb.pop_back();
		addWord(pos);
	}

	if(!found){
		found = tryrec(pos+1);
	}

	return found;
}

vi createHis(string s){

	vi his(30, 0);

	for(int i = 0; i < s.size(); i++){
		his[s[i]-'A']++;
	}

	return his;
}

void run(){

	ll T;
	cin >> T;

	words.pb(createHis("ZERO"));
	words.pb(createHis("ONE"));
	words.pb(createHis("TWO"));
	words.pb(createHis("THREE"));
	words.pb(createHis("FOUR"));
	words.pb(createHis("FIVE"));
	words.pb(createHis("SIX"));
	words.pb(createHis("SEVEN"));
	words.pb(createHis("EIGHT"));
	words.pb(createHis("NINE"));


	for(t = 1; t <= T; t++){
	
		his = vi(30, 0);

		string s;
		cin >> s;

		for(int i = 0; i < s.size(); i++){
			his[s[i]-'A']++;
		}

		tryrec(0);
		

				
	}
	

}

int main() {
	cout << fixed << setprecision(16);

	run();

	return 0;
}
