#include <iostream>
#include <algorithm>
using namespace std;
const int MAX_N = 1005;

double Nao_blk[MAX_N];
double Ken_blk[MAX_N];

int main()
{
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i) {
		int n;
		cin >> n;
		for(int j = 0; j < n; ++j) {
			cin >> Nao_blk[j];
		}
		for(int j = 0; j < n; ++j) {
			cin >> Ken_blk[j];
		}
		sort(Nao_blk, Nao_blk+n);
		sort(Ken_blk, Ken_blk+n);
		int score_war = 0;
		int score_d_war = 0;
		int f_nao = 0;
		int f_ken = 0;
		for(int j = 0; j < n; ++j) {
			if(Nao_blk[f_nao] < Ken_blk[f_ken]) {
				++f_nao;
			} else {
				++f_nao;
				++f_ken;
				++score_d_war;
			}
		}
		int	b_nao = n-1;
		int b_ken = n-1;
		for(int j = 0; j < n; ++j) {
			if(Nao_blk[b_nao] > Ken_blk[b_ken]) {
				--b_nao;
				++score_war;
			} else {
				--b_nao;
				--b_ken;
			}
		}
		cout << "Case #" << i+1 << ": " << score_d_war << " " << score_war << endl;
	}
	return 0;
}