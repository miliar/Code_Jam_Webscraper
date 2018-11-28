#include<bits/stdc++.h>

using namespace std;

int arr[2000];

int main(){

	int T, n;
	
	freopen("Alarge.in", "r",stdin);
	freopen("Alarge.out","w",stdout);
	cin >> T;
	
	for(int tc = 1; tc <= T; tc ++){
		
		int ans1 = 0, ans2 = 0, up = 0, cont = 0;
		
		cin >> n;
		
		for(int i = 0; i < n; i ++)	cin >> arr[i];
		
		
		for(int i = 1; i < n; i ++){
			if(arr[i - 1] > arr[i])
				ans1 += abs(arr[i] - arr[i - 1]);
			
			up = max(up,arr[i - 1] - arr[i]);
		}
		
		//cout << "up is " << up << endl;
		for(int i = 0; i < n - 1; i ++){
			if( arr[i] <= up)
				ans2 += arr[i];
			else
				ans2 +=  up;
		}
		
		
		printf("Case #%d: %d %d\n", tc, ans1, ans2);
	}
	return 0;
}
