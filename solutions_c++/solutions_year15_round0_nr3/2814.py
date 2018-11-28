#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

int mult[108][108] = {{},{0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'i','j','k'},
{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},
{0,'i',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,'k','j'},
{0,'j',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'k',1,'i'},
{0,'k',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'j','i',1}};

int sign[108][108] = {{},{0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1},
{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},
{0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,-1},
{0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,1},
{0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,-1}};

void buscar_finales_i(int L, ll X, const string& S, vector<pll>& V) {
	int i = 0, Val = 1, Sig = 1;
	ll j = 0;
	while (j < X) {
		Sig = Sig * sign[Val][S[i]];
		Val = mult[Val][S[i]];
		i++;
		if (i == L) {
			i = 0;
			j++;
		}
		if (Val == 'i' && Sig == 1)
			V.push_back(pll(i,j));
	}
}

void buscar_comienzos_k(int L, ll X, const string& S, vector<pll>& V) {
	int i = L - 1, Val = 1, Sig = 1;
	ll j = 0;
	while (j < X) {
		Sig = Sig * sign[S[i]][Val];
		Val = mult[S[i]][Val];
		if (Val == 'k' && Sig == 1)
			V.push_back(pll(i,X-j-1));
		i--;
		if (i < 0) {
			i = L - 1;
			j++;
		}
	}
}

pii multiplicar_rango(int L, ll X, const string& S, pll Ini, pll Fin) {
	int Val = 1, Sig = 1;
	while (Ini.second < Fin.second || (Ini.second == Fin.second && Ini.first < Fin.first)) {
		Sig = Sig * sign[Val][S[Ini.first]];
		Val = mult[Val][S[Ini.first]];
		Ini.first++;
		if (Ini.first == L) {
			Ini.first = 0;
			Ini.second++;
		}
	}
	return pii(Val, Sig);
}

int main() {
#ifdef TESTING
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T, L;
	ll X;
	string s;
	cin >> T;
	for (int caso = 1; caso <= T; caso++) {
		cin >> L >> X >> s;
		bool possible = false;

		vector<pll> EndI, StartK;
		buscar_finales_i(L, X, s, EndI);
		buscar_comienzos_k(L, X, s, StartK);

		vector<pll> Rangos(EndI.size() + StartK.size() + 2);
		vector<int> EndIRan(EndI.size()), StartKRan(StartK.size());
		vector<pii> AnsRango(EndI.size() + StartK.size() + 2);
		Rangos[0] = pll(0, 0);
		int rn = 1, i = 0, k = StartK.size() - 1;
		while (i < (int)EndI.size()) {
			if (k < 0 || EndI[i].second < StartK[k].second || (EndI[i].second == StartK[k].second && EndI[i].first < StartK[k].first)) {
				Rangos[rn] = EndI[i];
				EndIRan[i++] = rn;
			} else {
				Rangos[rn] = StartK[k];
				StartKRan[k--] = rn;
			}
			AnsRango[rn] = multiplicar_rango(L, X, s, Rangos[rn-1], Rangos[rn]);
			rn++;
		}
		while (k >= 0) {
			Rangos[rn] = StartK[k];
			StartKRan[k--] = rn;
			AnsRango[rn] = multiplicar_rango(L, X, s, Rangos[rn-1], Rangos[rn]);
			rn++;
		}
		Rangos[rn] = pll(L, X);
		AnsRango[rn] = multiplicar_rango(L, X, s, Rangos[rn-1], Rangos[rn]);
		rn++;

		for (i = 0; i < (int)EndIRan.size() && !possible; i++) {
			int Val = 1, Sig = 1, j = EndIRan[i] + 1;
			k = StartKRan.size() - 1;
			while (k >= 0 && StartKRan[k] < j) k--;
			while (k >= 0 && j < rn && !possible) {
				Sig = Sig * sign[Val][AnsRango[j].second];
				Val = mult[Val][AnsRango[j].first];
				if (j == StartKRan[k]) {
					possible = (Val == 'j' && Sig == 1);
					k++;
				}
				j++;
			}
		}

		cout << "Case #" << caso << ": " << (possible ? "YES" : "NO") << endl;
	}

	return 0;
}
