
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <stack>
#include <queue>
#include <cctype>
#include <complex>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <cassert>
#include <iomanip>

using namespace std;

#define dump(x)  cout << " "<< #x << " = " << (x) << endl;
#define pb push_back
#define all(x) (x).begin(),(x).end()
typedef long long ll;
typedef complex<int> P;
typedef pair<int,int> pii;
const double EPS = 1e-10;
const double PI  = acos(-1.0);



bool solve(int case_num){
	vector<int> ans;
	int n;
	cin>> n;
	vector<int> a(4);
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			int in;
			cin>> in;
			if(i == n-1){
				a[j] = in;
			}
		}
	}
	cin>> n;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			int in;
			cin>> in;
			if(i == n-1){
				for(int k=0;k<4;k++){
					if(in == a[k]) ans.pb(in);
				}
			}
		}
	}
	
	cout<< "Case #"<< case_num<< ": ";
	if(ans.size() == 1){
		cout<< ans[0]<< endl;
	}else if(ans.size() == 0){
		cout<< "Volunteer cheated!"<< endl;
	}else{
		cout<< "Bad magician!"<< endl;
	}
	return true;
}

int main(){
	cout.setf(ios::fixed);
	cout.precision(10);
	
	int n;
	cin>> n;
	for(int i=0;i<n;i++){
		solve(i+1);
	}
	return 0;
}

 