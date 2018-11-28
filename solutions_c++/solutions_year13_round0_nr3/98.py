//g++ -Ofast -lgmpxx -lgmp C.cpp
#include<iostream>
#include<vector>
#include<gmpxx.h>
#include<algorithm>
using namespace std;
typedef vector<int> vi;
int c(int x,int L){
	return min(L-1-x,x);
}
int main(){
	vector<vi> q,tmp;
	vector<mpz_class> all;
	q.push_back(vi(1,1));
	q.push_back(vi(1,2));
	for(int i=1;i<=3;++i)all.push_back(i*i);
	all.push_back(11*11);
	all.push_back(22*22);
	for(int L=3;L<=51;L++){
		int u=L>>1;
		tmp.clear();
		for(int i=0;i<q.size();++i)
		for(int x=0;x<=1+(L&1);++x){
			vi &v=q[i];
			v.push_back(x);
			int l= L*2-1;bool ok=true;
			for(int i=0;i<l && ok;++i){
				int t=0;
				for(int j=max(0,i-L+1);j<=i&&j<L;++j)
					t+=v[c(j,L)]*v[c(i-j,L)];
				ok &= (t<10);
			}
			if(ok){
				if(L%2==0)tmp.push_back(v);
				mpz_class t=0;
				for(int i=0;i<L;++i)t=t*10+v[c(i,L)];
				all.push_back(t*t);
			}
			v.pop_back();
		}
		if(L%2==0)tmp.swap(q);
	}
	int Tc=1,T;
	for(cin >> T;Tc<=T;++Tc){
		mpz_class a,b;
		cin >> a >> b;
		int x=0;
		if(a<=b)x=upper_bound(all.begin(),all.end(),b)
				-lower_bound(all.begin(),all.end(),a);
		cout << "Case #"<<Tc<<": " << x << endl;
	}
}
