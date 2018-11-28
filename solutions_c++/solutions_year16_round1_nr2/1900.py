#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int test;
	cin >> test;
	for (int t=0; t<test; t++) {
		int N;
		cin >> N;
		int ** p = new int*[2*N-1];
		for (int i=0; i < 2*N-1; i++) {
			p[i] = new int[N];
			for (int j=0; j<N; j++) {
				cin >> p[i][j];
			}
		}
		int ** m = new int*[N];
		for (int i=0; i < N; i++) {
			m[i] = new int[N];
		}
		int *ans = new int[N];
		int *heights = new int[2500];
		for (int i=0; i < 2500; i++) {
			heights[i] = 0;
		}
		for (int j=0; j<2*N-1; j++) {
			for (int k=0; k<N; k++) {
				heights[p[j][k]]++;
			}
		}
		cout << "Case #" << t+1 << ": ";
		for (int i=0; i<2500; i++) {
			if(heights[i]%2 == 1) cout << i << " ";
		}
		cout << endl;

	}

    return 0;
}
