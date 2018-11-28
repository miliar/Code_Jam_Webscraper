#include <iostream>
#include <cstdio>

using namespace std;

int main (){
	FILE* ifile = freopen("A-large.in", "r", stdin);
	FILE* ofile = freopen("ofile.txt", "w", stdout);
	int t;
	cin >> t;
	for (int z=1; z<=t; z++){
		int n;
		cin >> n;
		int A[10];
		for (int i=0 ; i<=9; i++){
			A[i] = 0;
		}
		if (n==0){
			cout << "Case #" << z << ": INSOMNIA" << endl;
		}
		else {
			int read = n;
			while (!(A[0]&&A[1]&&A[2]&&A[3]&&A[4]&&A[5]&&A[6]&&A[7]&&A[8]&&A[9])){
				int it = read;
				while (it > 0){
					int temp = it % 10;
					if (!A[temp]){
					A[temp] = 1;}
					it = it / 10;
				}
				read = read + n;
				
			}
			cout << "Case #" << z <<": " << read-n << endl;
		}
		
		
		
	}
	return 0;
	
}
