//~ gedemenli

#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>

#define pb push_back

using namespace std;

const int MAXN=11;

int K,N,ans;

inline void f( int t , vector<int> vec ){
	
	if( t==ans )
		return;
	
	bool fl=1;
	
	for( int i=1 ; i<MAXN ; i++ )
		if( vec[i] ){
			fl=0;
			break;
		}
	
	if(fl){
		ans=min(ans,t);
		return;
	}
	
	vector<int> vec2;
	
	for( int i=1 ; i<MAXN ; i++ )
		vec2.pb(vec[i]);
	
	vec2.pb(0);
	f(t+1,vec2);
	
	vec2.clear();
	
	for( int i=0 ; i<MAXN ; i++ )
		vec2.pb(vec[i]);
	
	fl=0;
	
	for( int i=MAXN-1 ; i>3 ; i-- )
		if( vec2[i] ){
			for( int j=1 ; j<=i/2 ; j++ ){
				vec2[j]++;
				vec2[i-j]++;
				vec2[i]--;
				f(t+1,vec2);
				vec2[j]--;
				vec2[i-j]--;
				vec2[i]++;
			}
			fl=1;
			break;
		}
	
	
	if(fl)
		return;
	else if( vec[3] )
		ans=min(ans,t+3);
	else if( vec[2] )
		ans=min(ans,t+2);
	else if( vec[1] )
		ans=min(ans,t+1);
	else
		ans=min(ans,t);
}

int main(){
	
	scanf("%d",&K);
	
	vector<int> vec;
	
	for( int C=1 ; C<=K ; C++ ){
		
		scanf("%d",&N);
		//~ cout << N << endl;
		
		vec.clear();
		for( int i=0 ; i<MAXN ; i++ )
			vec.pb(0);
		
		for( int k,i=0 ; i<N ; i++ ){
			scanf("%d",&k);
			ans=max(ans,k);
			vec[k]++;
		}
		
		f(0,vec);
		printf("Case #%d: %d\n",C,ans);
	}
	
	return 0;
}