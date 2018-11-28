#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <ctime>
#include <bitset>
#include <sstream>

#define SYNC ios::sync_with_stdio(false);
#define gc getchar
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define debug if (deb) cout

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<int, pair<int, int> > piii;
typedef vector<int> vi;
typedef vector<pii> vii;
typedef vector<pll> vll;

const int my[8] = {1, 0,-1, 0, 1, 1,-1,-1};
const int mx[8] = {0, 1, 0,-1, 1,-1, 1,-1};
const long long mod7=100000007;
const long inf=0x3f3f3f3f;
const double eps=1e-8;
const double pi=acos(-1.0);

inline int inp() {
    int x=0,f=1;char ch=gc();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=gc();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=gc();}
    return x*f;
}

bool deb = true;
/*
Z cari 0
X cari 6
U cari 4
W cari 2
R cari 3
O cari 1
F cari 5
V cari 7
T cari 8
N cari 9
"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
*/

char a[1000];
int t, cnt[1005], tt;
string jawab;

void kurang(string a) {
	for (int i = 0; i < a.length(); i++) {
		cnt[(int)a[i]]--;
	}
}

int main() {
	scanf("%d", &t);
	gets(a);
	for (int q = 1; q <= t; q++) {
		memset(cnt, 0 ,sizeof(cnt));
		jawab = "";
		gets(a);
		tt = strlen(a);
		for (int i = 0; i < tt; i++) {
			cnt[(int)a[i]]++;
		}
		//0
		while(cnt[(int)'Z']) {
			jawab += '0';
			kurang("ZERO");
		}
		while(cnt[(int)'X']) {
			jawab += '6';
			kurang("SIX");
		}
		while(cnt[(int)'U']) {
			jawab += '4';
			kurang("FOUR");
		}
		while(cnt[(int)'W']) {
			jawab += '2';
			kurang("TWO");
		}
		while(cnt[(int)'R']) {
			jawab += '3';
			kurang("THREE");
		}
		while(cnt[(int)'O']) {
			jawab += '1';
			kurang("ONE");
		}
		while(cnt[(int)'F']) {
			jawab += '5';
			kurang("FIVE");
		}
		while(cnt[(int)'V']) {
			jawab += '7';
			kurang("SEVEN");
		}
		while(cnt[(int)'T']) {
			jawab += '8';
			kurang("EIGHT");
		}
		while(cnt[(int)'N']) {
			jawab += '9';
			kurang("NINE");
		}

		sort(jawab.begin(), jawab.end());
		printf("Case #%d: ", q);
		cout << jawab << endl;
	}
}
