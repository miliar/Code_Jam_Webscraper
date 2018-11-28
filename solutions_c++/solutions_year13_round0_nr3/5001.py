#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main(void){

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int arr[5] = {1, 4, 9, 121, 484};
	
	int T, A, B;
	scanf("%d", &T);

	for(int t = 0; t < T; t++){
		scanf("%d %d", &A, &B);

		int ans = 0;
		for(int i = 0; i < 5; i++){
			if(arr[i] >= A && arr[i] <= B)
				ans++;
		}

		cout<<"Case #"<<t+1<<": "<<ans<<endl;
	}

	return 0;
}