#include<iostream>
#include<algorithm>

using namespace std;

struct party {
	int N;
	char c;
};

bool foo(party a, party b) {
	return a.N > b.N;
}

int main()
{
	int t; cin >> t;
	for(int i = 1; i <= t; i++) {
		int n; cin >> n;
		party P[n];int sum = 0;
		cout << "Case #" << i << ": ";
		for (int j = 0; j <n; j++)	{cin >> P[j].N;
			P[j].c = 'A'+j;
			sum += P[j].N;
		}
		sort(P,P+n,foo);
		while (sum!=0) {
			if (P[1].N <= (sum-2)/2) {
				P[0].N-=2;
				sum -= 2;
				cout << P[0].c << P[0].c << " ";
			}
			else if (n>2 && P[2].N > (sum-2)/2) {
				P[0].N--;
				sum--;
				cout << P[0].c << " ";
			}
			else {
				P[0].N--;
				P[1].N--;
				sum -= 2;
				cout << P[0].c << P[1].c << " ";
			}
			sort(P,P+n,foo);
		}
		cout << endl;
	}
}
