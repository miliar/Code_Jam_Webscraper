#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long
#define endl "\n"
#define mp make_pair
#define pb push_back
int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T,N,sum;
	cin >> T;
	int cnt=1;
	while(T--){
		cin >> N;
		if(N==0) {
			cout << "Case #" << cnt++ << ": ";
			cout << "INSOMNIA" << endl;
			continue;
		}
		bool isFound[10];
		rep(i,10) isFound[i]= false;
		for(int i=1; i< 101 ; i++ ){
			sum = N*i;			 
			 while(sum > 0 ){
			 	isFound[sum%10] = true;
			 	sum /= 10;
			 }
			 bool isCompleted = true;
			 rep(j,10){
			 	if(!isFound[j])
		 		{
		 			isCompleted = false;
		 			break;
		 		}
			 }
			 if(isCompleted){
			 	cout << "Case #" << cnt++ << ": ";
			 	cout << N*i << endl;
			 	break;
			 }			


		}
	}
	return 0;
}