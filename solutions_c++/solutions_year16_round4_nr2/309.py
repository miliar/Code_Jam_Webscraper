#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<cassert>
#define ALL(c) (c).begin(), (c).end()
using namespace std;
typedef long long ll;
typedef long double ld;

#include <unistd.h>
#include <wait.h>
bool __multithreading = true;
const int __limitofthreads = 8;
vector<pid_t> __ids;
char __str[128];
int __tests, __testsdone, __id;
void __inctests(){
	++__testsdone;
	sprintf(__str, "\033[1;1Htests %d/%d done.%c",__testsdone,__tests,10);
	cerr<<__str;
}

ld gg(vector<ld>&a){
	int k = a.size();
	/*string t = string(k/2,'0')+string (k/2, '1');
	ld pr = 0;
	do{
		ld pp = 1;
		for(int i=0;i<k;++i) if(t[i]=='1') pp*=a[i]; else pp*=1-a[i];
		pr+=pp;
	}while(next_permutation(ALL(t)));
	return pr;
	*/
	vector<map<int, ld>> d(k);
	d[0][1] = a[0];
	d[0][-1] = 1-a[0];
	for(int i=1;i<k;++i){
		for(int j=-(i+1);j<=i+1;++j){
			d[i][j] = a[i] * d[i-1][j-1] + (1-a[i])*d[i-1][j+1];
		}
	}
	ld res = d[k-1][0];
	return res;
}


ld f1(vector<ld> p, int n, int k){
	ld ans = -1;
	vector<ld> a(k);
	string s = string(n-k,'0')+string (k, '1');
	do{
		for(int i=0,j=0;i<n;++i) if(s[i]=='1') a[j++] = p[i];
		ans = max(ans, gg(a));
	}while(next_permutation(ALL(s)));
	return ans;
}

ld f2(vector<ld> p, int n, int k){
	ld ans = -1;
	sort(ALL(p));
	for(int i=0;i<=k;++i){
		vector<ld> a(p.begin(), p.begin()+i);
		for(int j=1;j<=k-i;++j) a.push_back(p[n-j]);
		ans = max(ans, gg(a));
	}
	return ans;
}

void solve(int test){
	///+++start read ALL data+++
	
	int n,k;
	cin>>n>>k;
	vector<ld> p(n);
	for(auto&x:p) cin>>x;
	
	///---end read data---
	if(__multithreading){
		if(__ids.size()>=__limitofthreads && wait(0)!=-1) __inctests();
		__id = fork();
		if(__id>0){
			__ids.push_back(__id);
			return ;
		}
		sprintf(__str, "thread%d.out", test);
		freopen(__str, "w", stdout);
	}
	///start solution and write output
	cout<<"Case #"<<test<<": ";
	ld ans = f2(p,n,k);
	cout.precision(10);
	cout<<fixed<<ans<<endl;
}

int main(){
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	
	cin>>__tests;
	for(int i=1;i<=__tests;++i){
		solve(i);
		if(__multithreading&&__id==0) return 0;
	}
	
	///combining outputs
	if(__multithreading){
		for(pid_t __id : __ids) if(waitpid(__id,0,0)!=-1) __inctests();
		int __bufsize = 1<<16;
		char *__buf = new char[__bufsize];
		for(int i=1;i<=__tests;++i){
			sprintf(__str, "thread%d.out", i);
			FILE *f = fopen(__str, "r");
			while(fgets(__buf, __bufsize, f)) printf("%s",__buf);
			fclose(f);
			remove(__str);
		}
		delete [] __buf;
	}
	
	return 0;
}
