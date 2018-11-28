#include <bits/stdc++.h>
using namespace std;

#define size(v) int(v.size())
#define MOD 1000003
#define INF 1e9
#define ulint unsigned long long int
#define lint long long int
#define mp make_pair
#define pb push_back
#define pop pop_back
#define st first
#define nd second
#define all(X) (X).begin(),(X).end()
#define E12 1000000000000

struct min_heap_comparator{
	bool operator()(const long& a,const long& b) const{
		return a>b;
	}
};
#define mh_min(X) make_heap(all(X), min_heap_comparator());
#define poph_min(X) {pop_heap(all(X), min_heap_comparator()); (X).pop();}
#define pushh_min(X, Y) {(X).pb(Y); push_heap(all(X), min_heap_comparator());}
#define sorth_min(X) sort_heap(all(X), min_heap_comparator());

#define mh_max(X) make_heap(all(X));
#define poph_max(X) {pop_heap(all(X)); (X).pop();}
#define pushh_max(X, Y) {(X).pb(Y); push_heap(all(X));}
#define sorth_max(X) sort_heap(all(X));

int x[] = {0, 1, 0, -1};
int y[] = {1, 0, -1, 0};

int main(void){
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t){
		int N;
		double V, X;
		cin >> N >> V >> X;
		vector<pair<double, double> > vet(N);
		for (int i = 0; i < N; ++i){
			cin >> vet[i].st >> vet[i].nd;
		}
		bool possivel = true;
		double saida;

		if (N == 1){
			if (vet[0].nd != X){
				possivel = false;
			} else {
				saida = V / vet[0].st;
			}
		} else {
			if (vet[0].nd == X){
				if (vet[1].nd == X){
					saida = V / (vet[0].st + vet[1].st);
				} else {
					saida = V / (vet[0].st);
				}
			} else if (vet[1].nd == X){
				saida = V / (vet[1].st);				
			} else if (vet[0].nd > X){
				if (vet[1].nd < X){
					double X1 = vet[0].nd;
					double X2 = vet[1].nd;
					double R1 = vet[0].st;
					double R2 = vet[1].st;
					double t2 = (X*V - X1*V)/((X2 - X1) * R2);
					double t1 = (V - t2*R2)/R1;
					//cout << t1 << " " << t2 << endl;
					saida = max(t1, t2);
				} else possivel = false;
			} else { // < X
				if (vet[1].nd > X){
					double X1 = vet[1].nd;
					double X2 = vet[0].nd;
					double R1 = vet[1].st;
					double R2 = vet[0].st;
					double t2 = (X*V - X1*V)/((X2 - X1) * R2);
					double t1 = (V - t2*R2)/R1;
					//cout << t1 << " " << t2 << endl;
					saida = max(t1, t2);
				} else possivel = false;
			}
		}

		if (possivel){
			//cout << "Case #" << t+1 << ": " << saida << endl;
			printf("Case #%d: %.9lf\n", t+1, saida);
		} else 
			cout << "Case #" << t+1 << ": IMPOSSIBLE" << endl;
	}
	return 0;
}
