#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	char c;
	int n,i,j,k,sm,N,f,x,s;
	int mat[10005];
	int max;
	ifstream ii("3.in");
	ofstream oo("o.txt");
	ii >> N;
	for (k=1; k<N+1; k++){
		ii >> n;
		for (i = 0; i < n ; i++){
			ii >> mat[i];
		}
		f = 0;
		s = 0;
		max = 0;
		for (i = 1; i < n; i++){
			if (mat[i] < mat[i - 1]){
				f += mat[i-1] - mat[i ];
				if (max < mat[i-1] - mat[i])max = mat[i-1] - mat[i];
			}

		}
		
		x = max;
		for (i = 0; i < n-1; i++){
			if (mat[i] - x > mat[i + 1]){ cout << "ERROR"; }
			if (mat[i] < x){
				s += mat[i];
				continue;
			}
			else{ s += x; }
		}
		oo << "Case #" << k << ": " << f << " " << s;;
		if (k == N)break;
		oo << "\n";


	}

	ii.close();
	oo.close();


}