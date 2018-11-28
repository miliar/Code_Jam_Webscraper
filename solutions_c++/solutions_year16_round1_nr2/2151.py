/*
 * @author:metastableB
 * B_rank_and_file.cpp
 * 
 */

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <climits>
#include <ctime>

/* BEGIN Timer */
#define CLOCK clock()
#define BEGIN_CLOCK clock_t _bx_ = clock();
#define END_CLOCK clock_t _ex_ = clock();
#define TOTAL_C (double)(_ex_ - _bx_)
#define TOTAL_T (TOTAL_C/CLOCKS_PER_SEC)
#define PRINT_CLOCK (printf("%2.3f\n",TOTAL_T));
/* END Timer */
#define ULL unsigned long long
#define LL long long

int arr[100];
int height[2501];

using namespace std;
int main() {
	int T;
	cin >>T;
	int cse = 1;
	while(cse <= T){
		int N,i = 0,t;
		cin >> N;
		// for each line
		while(i < 2*N - 1){
			// for each digit in line increase its count
			int j =0;
			while(j < N){
				cin >> t;
				// number of soldiers with height t
				height[t]++;
				j++;
			}
			i++;
		}
		// we have incremented the height counter, no collect odd;
		int x = 0, y = 0;
		while(x < N){
			if(height[y]%2 == 1){arr[x] = y; x++;}
			height[y] = 0;
			y++;
		}
		cout << "Case #" <<cse <<": ";
		sort(arr,arr+ N);
		for(int z = 0; z < N ;z++){
			cout << arr[z]<<" ";
			arr[z] = 0;
		}
		cout << "\n";
		cse++;
	}
    return 0;
}
