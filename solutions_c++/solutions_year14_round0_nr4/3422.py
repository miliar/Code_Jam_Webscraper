// Submitted by Silithus @ Macau
#include <iostream>
#include <algorithm>

using namespace std;

void work(void)
{
	int N,i,n,k,ans1,ans2;
	double naomi[1000],ken[1000];
	
	cin >> N;
	for(i=0; i<N; i++) cin >> naomi[i];
	for(i=0; i<N; i++) cin >> ken[i];
	sort(naomi, naomi+N);
	sort(ken, ken+N);
	
	n = k = ans1 = 0;
	while( n<N && k< N ) {
		if( naomi[n] > ken[k] ) {
			n++; k++; ans1++;
		} else {
			n++;
		}
	}
	
	n = k = ans2 = 0;
	while( n < N ) {
		while( k < N ) {
			if( ken[k] > naomi[n] ) break;
			k++;
		}
		if( k < N ) { n++; k++; }
		else break;
	}
	ans2 = N-n;

	cout << ans1 << " " << ans2;
}

int main(void)
{
	int t,T;
	
	cin >> T;
	for(t=1; t<=T; t++) {
		cout << "Case #" << t << ": ";
		work();
		cout << endl;
	}
	
	return 0;
}
