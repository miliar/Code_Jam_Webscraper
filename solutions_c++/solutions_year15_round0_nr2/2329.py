#include <iostream>
#include <algorithm>
#include <cstdio>
#include <set>
#include <functional>

using namespace std;

int T;
int D;
int P[1003];
bool cmp(int a,int b){
	return a>b;
}

int test2(int a, int b){
	for(int i=0;i<D;++i){
		if(P[i]<=b)
			return 1;
		a-=(P[i]+b-1)/b-1;
		if(a<0)
			return 0;
	}
	return 1;
}

int test(int a){
	int res=0;
	for(int i=0;i<a;++i){
		res|=test2(i, a-i);
	}
	return res;
}

int getRes(int l,int r){
	int m;
	while(l<r){
		m=(l+r)/2;
		if(test(m))
			r=m;
		else
			l=m+1;
	}
	return l;
}

int main(){
	cin>>T;
	for(int cs=0; cs<T; ++cs){
		cin>>D;
		int res=1003;
		for(int i=0;i<D;++i){
			cin>>P[i];
		}
		std::sort(P, P+D, cmp);

		int l=1;
		int r=P[0];
		cout<<"Case #"<<(cs+1)<<": "<<getRes(1, 1003)<<endl;
	}
	return 0;
}


