#include<iostream>
#include<cmath>
#include<algorithm>
#define L 1000000007

using namespace std;
//ifstream cin("test.in");
//ofstream cout("test.out");

int n, m, h, k, r, x, T, t, f, z, i, j;
string s;
int a[1000], b[10], v[11];

void Add(){
	int i, j, f;
	for(i=1; i<=k; ++i)
		a[i]+=b[i];
	for(i=1; i<m; ++i){
		a[i+1]+=(a[i]/10);
		a[i]%=10;
	}
	if(a[m]>=10){
		a[m+1]=a[m]/10;
		a[m]%=10;
		++m;
	}
}

bool Check(){
	int i, j;
	for(i=1; i<=m; ++i)
		++v[a[i]];
	
//	for(i=0; i<=9; ++i) cout<<v[i]<<" "; cout<<"\n";
	
	for(i=0; i<=9; ++i)
		if(v[i]==0) return 0;
		
	return 1;
}

int main(){
	cin>>T; 
	for(t=0; t<T; ++t){
		for(i=0; i<=9; ++i)
			v[i]=0;
		cin>>n;
		if(n==0) cout<<"Case #"<<t+1<<": INSOMNIA\n"; else{
		x=n;
		k=0;
		while(x){
			b[++k]=x%10;
			x=x/10;
		}
		m=k;
		for(i=1; i<=m; ++i) a[i]=0;
		do{
			Add();
		//	for(i=m; i>0; --i) cout<<a[i]; cout<<"\n";		
		
		}while(!Check());
		cout<<"Case #"<<t+1<<": ";
		for(i=m; i>0; --i) cout<<a[i]; cout<<"\n";
		
		}
	}
	
	return 0;
}
