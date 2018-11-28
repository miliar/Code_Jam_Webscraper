#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <cstdlib>
#include <queue>
#include <set>
#include <iomanip>

#define long long
#define mp make_pair

using namespace std;

const int mod=1000002013;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin >>test;
	for (int te=1; te<=test; ++te){
		long n,p;
		cin >>n >>p;
		long s=0,t=(1<<n);
		while (t-s>1){
			long m=(t+s)/2;
			long z=0;
			long ost=m;
			while (ost>0){
				++z;
				ost=(ost-1)/2;
			}
			long place=(1<<n)-(1<<(n-z))+1;
			if (place<=p)
				s=m;
			else
				t=m;
		}
		long ans1=s;
		s=0;
		t=(1<<n);
		while (t-s>1){
			long m=(t+s)/2;
			long z=0;
			long ost=(1<<n)-m-1;
			while (ost>0){
				++z;
				ost=(ost-1)/2;
			}
			long place=(1<<(n-z));
			if (place<=p)
				s=m;
			else
				t=m;
		}
		long ans2=s;
		cout <<"Case #" <<te <<": " <<ans1 <<" " <<ans2 <<endl;
	}
	return 0;
}