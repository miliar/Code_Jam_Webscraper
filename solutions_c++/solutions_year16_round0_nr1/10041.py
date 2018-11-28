//Irvin Gonzalez
//jam


#include <iostream>
#include <vector>

using namespace std;

void solve() {
	int N;
	cin >> N;
	if(N == 0) {
		cout << "INSOMNIA";
		return; }
	int a[10];
	for(int i =0; i < 10; ++i) {
		a[i] = 0; }
	int seen = 0; 
	int i = 2;
	int x = N;
	while(1){ 
		int M = x;
		while(M != 0) {			
			if(a[M%10] == 0) {
				++seen;
				++a[M%10];
				if(seen == 10) {
					cout << x;
					return; } }
			M = M/10;}
		x = i * N;
		++i; }
} 
		
			
				
			
		

	

int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		
		solve();
		cout <<endl; } }
