#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

void solve(int Ti)
{
	int N;
	cin >> N;
	vector<double> ken(N, 0);
	vector<double> nao(N, 0);
	for( int i = 0; i < N; i++ ) {
		cin >> nao[i];
	}
	for( int i = 0; i < N; i++ ) {
		cin >> ken[i];
	}
	sort(nao.begin(), nao.end());
	sort(ken.begin(), ken.end());
	int deceitful = 0;
	int j = 0;
	for( int i = 0; i < N; i++ ) {
		if( nao[i] > ken[i-j] ) {
			deceitful++; // told nao = max(ken)+0.000001, choose nao = min(nao), choose ken = min(ken), win = nao
		} else if( nao[i] < ken[i - j] ) {
			// told nao = max(ken)-0.000001, choose nao = min(nao), choose ken = max(ken), win = ken
			j++;
		}
	}
	int lawful = 0;
	j = 0;
	for( int i = 0; i < N; i++ ) {
		if( i + j >= N ) {
			lawful++;
		} else if( nao[i] > ken[i + j] ) {
			j++;
			i--;
		} else if( nao[i] < ken[i + j] ) {
			//
		}
	}
	cout << deceitful << " " << lawful;
}




int main(int argc, char* argv[])
{
	if (argc == 3) {
		freopen(argv[1], "r", stdin);
		freopen(argv[2], "w", stdout);
	}
	int T;
	cin >> T;
	cout.precision(15);
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve(i);
		cout << endl;
	}

	return 0;
}