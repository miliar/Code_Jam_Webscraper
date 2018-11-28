#include <iostream>
#include <algorithm>
#include <cmath>
#include <climits>

using namespace std;

int main(){
	long long T,D,m=1,arr[1001],n=0,ans = LLONG_MAX;
	cin >> T;
	while(T--){
		n = 0;
		ans = LLONG_MAX;
		cin >> D;
		for (int i = 1; i <= D; ++i)
		{
			cin >> arr[i];
		}
		long long max = *max_element(arr+1,arr+(D+1));
		for(int j =1 ; j<=max;j++){
			n = 0;
			for (int k = 1; k <=D; ++k)
			{
				n += (ceil(arr[k]/(1.0*j))-1);
				//cout << arr[k];
			}
			//cout << n;
			n += j;
			//cout << n << endl;
			ans = min(ans,n);
		}
		cout <<"Case #"<< m<<": "<<ans << endl;
		m++;
	}
}