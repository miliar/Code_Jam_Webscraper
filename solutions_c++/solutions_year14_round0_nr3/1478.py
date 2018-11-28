#include<iostream>
#include<algorithm>
#include<vector>
#include<iomanip>
using namespace std;
#define ll long long
#define ld long double
#define vi vector<int>
#define pb push_back
#define pii pair<int,int>
#define mp make_pair
#define st first
#define nd second
#define mini(a,b) a=min(a,(b))
#define maxi(a,b) a=max(a,(b))
#define RE(i,n) for(int i=0,_n=(n);i<_n;++i)
#define RI(i,n) for(int i=1,_n=(n);i<=_n;++i)
const int inf=1e9+5, nax=1e6+5;

bool F(int H, int W, int ile)
{
	if(ile == 1) {
		RI(i,H) {
			RI(j,W) {
				if(i==1 && j==1) cout << "c";
				else cout << "*";
			}
			cout << "\n";
		}
		return true;
	}
	for(int w = 2; w <= W; ++w)
		for(int h = 2; h <= H; ++h) {
			int duzo = h * w;
			int malo = duzo - (h-2) * (w-2);
			if(malo <= ile && ile <= duzo) {
				int brak = ile - malo;
				RI(i, W) {
					if(i==1) cout << "c";
					else if(i<=w) cout << ".";
					else cout << "*";
				}
				cout << "\n";
				RI(i, W) {
					if(i<=w) cout << ".";
					else cout << "*";
				}
				cout << "\n";
				for(int i = 3; i <= h; ++i) {
					cout << "..";
					for(int kol = 3; kol <= W; ++kol) {
						if(kol <= w && brak > 0) {
							brak--;
							cout << ".";
						}
						else cout << "*";
					}
					cout << "\n";
				}
				for(int i = h+1; i <= H; ++i) {
					RI(j, W) cout << "*";
					cout << "\n";
				}
				return true;
			}
		}
	return false;
}

int main()
{
	ios_base::sync_with_stdio(0);
	
	int z;
	cin >> z;
	RI(test, z) {
		cout << "Case #" << test << ":\n";
		int H, W, ile;
		cin >> H >> W >> ile;
		ile = H*W - ile;
		if(min(H, W) == 1) {
			if(H==1) {
				RI(i, W) {
					if(i==1) cout << "c";
					else if(i<=ile) cout << ".";
					else cout << "*";
				}
				cout << "\n";
			}
			else {
				RI(i, H) {
					if(i==1) cout << "c";
					else if(i<=ile) cout << ".";
					else cout << "*";
					cout << "\n";
				}
			}
		}
		else if(!F(H, W, ile)) 
			cout << "Impossible\n";
	}
	return 0;
}
