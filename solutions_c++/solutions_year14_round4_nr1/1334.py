#include <set>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
	int T;
	cin >> T;

	for(int t=0;t<T;t++){
		int N,X;
		cin >> N >> X;
		int A[N];
		for(int i=0;i<N;i++){
			cin >> A[i];
		}

		sort(A,A+N,greater<int>());
		int used[N];
		for(int i=0;i<N;i++)
			used[i] = 0;
		int ans = 0;
		for(int i=0;i<N;i++){
			if(used[i]==1) continue;
			used[i] = 1;
			for(int j=i+1;j<N;j++){
				if(used[j]==0 && A[i] + A[j] <= X){
					used[j] = 1;
					break;
				}
			}
			ans++;
		}
		cout<<"Case #"<<t+1<<": "<<ans<<endl;
	}
}
