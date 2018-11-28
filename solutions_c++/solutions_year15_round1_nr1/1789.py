#include <iostream>

using namespace std;

int m[10000];
int min1, min2, N, larger;
int main(){
	int T;
	cin >> T;
	for(int caso =1; caso< T+1; caso++){
		cin >> N;
		min1 = min2 = larger = 0 ;
		cin >> m[0];
		for(int i=1; i<N; i++){
			cin >> m[i];
			if(m[i-1] > m[i]){
				min1+= m[i-1] - m[i];
				if(m[i-1] - m[i] > larger)
					larger = m[i-1] - m[i];
			}
		}
		for(int i=0; i<N-1; i++){
			if(m[i] < larger)
				min2+=m[i];
			else
				min2+=larger;
		}

		cout << "Case #" << caso << ": " << min1 << " " << min2 << endl;
	}
}