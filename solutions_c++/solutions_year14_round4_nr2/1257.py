#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>

using namespace std;

int main(){
	int t; cin >> t;
	for(int tc =1; tc<=t; tc++){
		int ans = 1000000;
		int n; cin >> n;
		int c[n];
		int a[n], b[n];
		for(int i = 0; i < n; i++){
			cin >> a[i];
			b[i] = a[i];
		}
		sort(a, a+n);
		
		do{
			//valid
			int cnt = 0;
			for(int i = 1; i < n-1; i++){
				if(a[i-1] > a[i] && a[i] < a[i+1]) {
					cnt++;
				}
			}
			if(cnt > 0){
				continue;
			}
			for(int i = 0; i < n; i++){
				for(int j = 0; j < n; j++){
					if(b[i] == a[j]){
						c[i] = j;
					}
				}
			}
			int inv = 0;
  			
 
 			 for(int i = 0; i < n - 1; i++)
    				for(int j = i+1; j < n; j++)
      					if(c[i] > c[j])
        					inv++;
			ans = min(inv, ans);
		}while(next_permutation(a, a+n));
		cout << "Case #"<<tc << ": " << ans << endl;
	}
	return 0;
}
