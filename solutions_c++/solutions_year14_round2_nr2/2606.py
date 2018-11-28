
// aymos (Somya Mehdiratta , IIIT Hyderabad)

#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<map>
#include<climits>
#include<stack>
#include<queue>
#include<algorithm>

using namespace std;

#define PB push_back
#define FOR(i,s,n) for(int i=(s),_n=(n);i<_n;i++)

typedef long long LL;

int min(int a,int b){
	if(a<b)
		return a;
	return b;
}
int main(int argc, char *argv[]){
	int t;
	cin>>t;
	int s = 1;
	while(s<=t){
		unsigned int a,b,k,ans=0;
		cin>>a>>b>>k;
		FOR(i,0,a)
			FOR(j,0,b)
				if(i!=j && (i&j)<k){
					//cout<<i<<" "<<j<<endl;
					++ans;
				}
		FOR(i,0,min(a,b))
			if( (i&i) < k){
			//	cout<<i<<" "<<i<<endl;
				++ans;
			}

		cout<<"Case #"<<s<<": "<<ans<<endl;
		++s;
	}
	return 0;
}
