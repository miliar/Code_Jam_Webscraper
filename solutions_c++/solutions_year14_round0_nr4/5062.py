#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
	int n = 0;
	cin>>n;
	for(int i=1; i <= n; ++i){
		int a; double t=0;
		int res1 = 0 , res2 = 0;
		cin>>a;
		vector <double> N(a);
		vector <double> K(a);
		vector <double> K1(a);
		for(int j=0; j < a; ++j){
			cin>> t;
			N[j]=t;
		}
		for(int j=0; j < a; ++j){
			cin>> t;
			K[j]=t;
		}
		sort(N.begin(),N.end());
		sort(K.begin(),K.end());
		K1=K;
		for(int j = 0; j < a; ++j)
			for(int k = 0; k < a; ++k)
				if (N[j] > K[k]){
					res1 += 1;
					K[k]=10;
					break;
				}
		for(int j = 0; j < a; ++j)
			for(int k = 0; k < a; ++k)
				if (K1[j]>N[k]){
					res2 += 1;
					N[k]=10;
					break;
				}
		cout<<"Case #"<<i<<": "<<res1<<' '<<a-res2<<endl;
			
	}
		
}