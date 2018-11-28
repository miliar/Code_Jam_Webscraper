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
		int N;
		cin >> N;
		int A[N];
		for(int i=0;i<N;i++){
			cin >> A[i];
		}

		int best = 1000000000;
		for(int i = 0;i<N;i++){
			int M = i;
			int inv = 0;
			for(int j=0;j<=M;j++){
				for(int k=j+1;k<=M;k++){
					if(A[j]>A[k]) {
						inv++;
					}
				}
			}
			
			for(int j=M+1;j<N;j++){
				for(int k=j+1;k<N;k++){
					if(A[j]<A[k]) {
						inv++;
					}
				}
			}
			
			if(inv < best) best = inv;
		}

		int bst = 1000000000;
		
		for(int i=0;i<(1<<N);i++){
			int left = 0;
			int ans = 0;
			vector<int> a1;
			vector<int> a2;
			for(int j=0;j<N;j++){
				if(i&(1<<j)){
					ans += j - left;
					a1.push_back(A[j]);
					left++;
				} else {
					a2.push_back(A[j]);
				}
			}
			for(int j=0;j<a1.size();j++){
				for(int k=j+1;k<a1.size();k++){
					if(a1[j] > a1[k]) ans++;
				}
			}
			
			for(int j=0;j<a2.size();j++){
				for(int k=j+1;k<a2.size();k++){
					if(a2[j] < a2[k]) ans++;
				}
			}
			
			if(ans < bst) bst = ans;
		}
		cout<<"Case #"<<t+1<<": "<<bst<<endl;
	}
}
