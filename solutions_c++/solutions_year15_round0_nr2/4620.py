#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

#define pb push_back

using namespace std;

const int MAXN=11;

int T,N,res;

inline void f( int t , vector<int> vec ){
	
	if( t==res )
		return;
	
	/*cout << t << " -----> ";
	for( int i=1 ; i<MAXN ; i++ )
		for( int j=1 ; j<=vec[i] ; j++ )
			cout << i << ' ';
	cout << "------>" << res << endl;*/
	
	bool fl=1;
	
	for( int i=1 ; i<MAXN ; i++ )
		if( vec[i] ){
			fl=0;
			break;
		}
	
	if(fl){
		res=min(res,t);
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
			/*vec2[i/2]++;
			vec2[i-(i/2)]++;
			vec2[i]--;
			fl=1;*/
			for( int j=1 ; j<=i/2 ; j++ ){
				vec2[j]++;
				vec2[i-j]++;
				vec2[i]--;
				f(t+1,vec2);
				vec2[j]--;
				vec2[i-j]--;
				vec2[i]++;
			}
			//~ cout << "asdasdads " << i << endl;
			fl=1;
			break;
		}
	
	/*for( int i=0 ; i<MAXN ; i++ )
		cout << vec2[i] << ' ';
	cout << endl;*/
	
	if(fl)
		return;
	else if( vec[3] )
		res=min(res,t+3);
	else if( vec[2] )
		res=min(res,t+2);
	else if( vec[1] )
		res=min(res,t+1);
	else
		res=min(res,t);
}

int main(){
	
	scanf("%d",&T);
	
	vector<int> vec;
	
	for( int Case=1 ; Case<=T ; Case++ ){
		
		scanf("%d",&N);
		
		vec.clear();
		for( int i=0 ; i<MAXN ; i++ )
			vec.pb(0);
		
		for( int k,i=1 ; i<=N ; i++ ){
			scanf("%d",&k);
			res=max(res,k);
			vec[k]++;
		}
		
		/*for( int i=0 ; i<MAXN ; i++ )
			cout << vec[i] << ' ';
		cout << endl;*/
		
		f(0,vec);
		printf("Case #%d: %d\n",Case,res);
	}
	
	return 0;
}