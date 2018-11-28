#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<set>
#include<algorithm>

using namespace std;

double k[1010], n[1010];

int main(){
	int t, count = 1, N;
	int w, d;
	int a, b;
	
	cin >> t;
	while(t--){
		cin >> N;
				
		for(int i = 0; i < N; i++){
			cin >> n[i];
		}
		for(int i = 0; i < N; i++){
			cin >> k[i];
		}
		
		sort(k, k+N);
		sort(n, n+N);
		
		w = d = 0;
		a = 0;
		b = N-1;
		while(a <= b){
			if(n[b] > k[N-1-a-(N-1-b)]){
				b--;
				d++;
			} else {
				a++;
			}
		}
		a = b = 0;
		while(a < N && b < N){
			while(b < N && k[b] < n[a]){
				w++; b++;
			}
			a++;
			b++;
		}
		
		cout << "Case #" << count++ << ": " << d << " " << w << endl;
	}
	
	return 0;
}

