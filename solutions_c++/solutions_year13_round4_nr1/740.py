#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <list>
#include <string>
#include <algorithm>
#include <set>
#include <cmath>
#include <vector>
#include <map>
#include <iterator>
#include <sstream>
#include <fstream>
#include <list>
#include <set>
#include <stack>
#include <bitset>
#include <ctime>
 
#pragma comment(linker, "/STACK:256000000")
 
#define EPS 1e-7
 
const long double PI = 3.1415926535897932384626433832795;
 
using namespace std;
 
int aabs(int a){
	if (a<0) return -a;
	return a;
}

struct p{
	long long i;
	long long k;
	long long pp;
};

bool cmp(p a, p b){
	return a.i<b.i || a.i==b.i && a.pp<b.pp; 
}

long long solveOne(){
	long long n,m;
	cin>>n>>m;
	p a[2013];
	long long ans2=0;
	long long mm=1000002013;
	for (int i=0;i<m;i++){
		long long t1,t2,t3;
		cin>>t1>>t2>>t3;
		ans2=(ans2+((t2-t1)*(t2-t1-1)/2)%mm*t3)%mm;
		a[2*i].i=t1;
		a[2*i].k=t3;
		a[2*i].pp=0;
		a[2*i+1].i=t2;
		a[2*i+1].k=t3;
		a[2*i+1].pp=1;
	}
	sort(a,a+2*m,cmp);
	long long ans1=0;
	map<long long,long long> t;
	for (int i=0;i<2*m;i++){
		if (!a[i].pp){
			t[a[i].i]+=a[i].k;
		}
		else{
			while (a[i].k>0){
				map<long long,long long>::iterator it = t.end(); it--;
				if (it->second>a[i].k){
					(*it).second-=a[i].k;
					long long d=a[i].i-it->first;
					ans1=(ans1+a[i].k*(d*(d-1)/2%mm))%mm;
					a[i].k=0;
				}
				else{
					long long d=a[i].i-it->first;
					ans1=(ans1+it->second*(d*(d-1)/2%mm))%mm;
					a[i].k-=it->second;
					t.erase(it);
				}
			}
		}
	}
	long long ans=((ans1-ans2)%mm+mm)%mm;
	return ans;
}

void solveAll(){
	int t;
	cin>>t;
	for (int i=1;i<=t;i++){
		cout<<"Case #"<<i<<": "<<solveOne()<<"\n";
		//cout<<"Case #"<<i<<": "; solveOne(); cout<<"\n";
	}
}

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	cout.setf(ios::fixed);
	cout.precision(6);
	solveAll();
	return 0;
}