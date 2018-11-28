#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <deque>
using namespace std;
typedef long long ll;
typedef pair<double, double> dd;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

int main(){
	int T; cin >> T;
	for(int t=1;t<=T;t++){
		int n, J; cin >> n >> J;
		n -= 2;
		printf("Case #%d:\n", t);
		for(int k=0;k<(1<<n);k++){
			vi ans(12, -1);
			bool fail = false;
			//now we have binary number k
			vector<ll> nums(12, 0);
			vector<ll> muls(12); 
			for(int i=2;i<=10 && !fail;i++){
				muls[i] = i;
				nums[i] = 1;

				for(int j=n-1;j>=0;j--){
					if(((k>>j) & 1) == 1){ //set
						nums[i] += muls[i];
						//cout << nums[i] << endl;
					}
					muls[i] *= i;
				}
				nums[i] += muls[i];
				for(ll z=2;z*z<=nums[i];z++){
					if(nums[i]%z == 0){
						ans[i] = z;
						break;
					}
				}
				if(ans[i] == -1){
					fail = true;
					break;
				}
			}
			if(fail) continue;
			/*for(int i=2;i<=10;i++){
				cout << nums[i] <<" ";
			}cout<<endl;*/
			string digs ="";
			for(int j=0;j<n;j++){
				if(((k>>j) & 1) == 1){ //set
					digs += "1";
				} else digs += "0";
			}
			cout <<"1"<<digs<<"1";
			for(int i=2;i<=10;i++){
				printf(" %d", ans[i]);
			}
			printf("\n");
			J--;
			if(J == 0) break;
		}
	}

}
