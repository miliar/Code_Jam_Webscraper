#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int find1(vector<int> &A){
	int k=0;

	for (int i=0; i<A.size(); ++i){
		if (A[i] > A[k]){
			k = i;
		}
	}

	return k;
}

int find2(vector<int> &A, int &k1){
	int k=0;
	if(k1 == 0){
		k = 1;
	}

	for (int i=0; i<A.size(); ++i){
		if (A[i] > A[k] && i != k1){
			k = i;
		}
	}

	return k;
}

int main(){
	int t; cin>>t;

	for (int i=1; i<=t; ++i){

		int n; string S; cin>>n;
		vector<int> A(n,0);

		int sum=0, l=0;

		for(int j=0; j<n; ++j){
			cin>>A[j];
			sum += A[j];
		}
		l = sum/2;

		int k1, k2;

		while(sum != 0){
			k1 = find1(A);
			k2 = find2(A, k1);

			if((sum-1)/2 >= A[k2]){
				S = S + char(65+k1) + " ";
				A[k1] -= 1;
				sum--;
			}
			else if(l-1 <= A[k2]){
				S = S + char(65+k1);
				A[k1] -= 1;
				sum--;
				if (A[k2] > 0){
					S = S + char(65+k2);
					A[k2] -= 1;
					sum--;
				}
				S = S + " ";
			}
			else{
				if(A[k1] >= 2){
					S = S +char(65+k1) + char(65+k1) + " ";
					A[k1] -= 2;
					sum -= 2;
				}
				else{
					S = S + char(65+k1) + " ";
					A[k1] -= 1;
					sum -= 1;
				}
			}
			// cout<<S<<endl<<sum<<endl;
			l = sum/2;
		}


		cout<<"Case #"<<i<<": "<<S<<endl;
	}

	return 0;
}