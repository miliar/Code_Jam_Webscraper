#include <iostream>
#include <cstdio>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;
int n;
double x;
deque<double> a,b;
void solve(int test){
	printf("Case #%d: ", test+1);
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%lf",&x);
		a.push_back(x);		
	}
	for(int i=0; i<n; i++){
		scanf("%lf",&x);
		b.push_back(x);
	}
	sort(a.begin(),a.end());
	sort(b.begin(),b.end());	
	deque<double> a1 = a, b1=b;
	
	int r1=0,r2=0;
	for(int i=0; i<n; i++){
		if( a.back() > b.back()){			
			r2++;
			a.pop_back();
			b.pop_front();
		}else{
			a.pop_back();
			b.pop_back();
		}
	}
	for(int i=0; i<n; i++){
		if(a1.front() > b1.front() ) {
			r1++;
			a1.pop_front();
			b1.pop_front();
		}
		else{
			a1.pop_front();
			b1.pop_back();
		}
	}
	cout << r1 << " " << r2 << endl;
}
int ntest;
int main(){
	freopen("D-large.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&ntest);		
	for(int t=0; t<ntest; t++){
		solve(t);
	}
	return 0;
}
