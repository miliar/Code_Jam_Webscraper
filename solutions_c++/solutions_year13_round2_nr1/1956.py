#include <iostream>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>


using namespace std;

int main(void){
	int T;
	long long A;
	long long N;

	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);

	scanf("%d",&T);

	for(int t = 1; t <= T; t++){
		scanf("%lld %lld", &A,&N);
		vector<int> v;

		int ele;
		for(int i = 0; i < N; i++){
			scanf("%d",&ele);
			v.push_back(ele);
		}

		sort(v.begin(), v.end());

		long long addAns = 0;
		long long remAns = 0;
		long long ans = 0;

		bool flag = true;
		for(int i = 0; i < v.size(); i++){
			if(A == 1){
				remAns += (v.size()-i);
				addAns += (v.size()-i);
				break;
			}
			if(A > v[i]){
				A = A + v[i];
			}
			else{
				int oper = 0;
				while(A <= v[i]){
					A = A + A - 1;
					addAns++;
					oper++;
				}
				// eat v[i];
				A += v[i];
				if(flag && oper >= 2){
					remAns += (v.size()-i);
					flag = false;
					
				}
				else{
					if(flag)
						remAns = addAns;
				}
			}
		}
		
		ans = min(remAns, addAns);

		cout<<"Case #"<<t<<": "<<ans<<endl;

	}

	return 0;
}