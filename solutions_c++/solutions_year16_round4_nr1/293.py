#include <bits/stdc++.h> 

using namespace std;

#define ll long long
#define type double

int n,k;

type p[210];

type pp[210];

int cnt_bit(int x){
	int res = 0;
	while(x){
		if(x&1){
			res++;
		}
		x>>=1;
	}
	return res;
}


int main(){
	int t;
	cin>>t;
	
	int cas = 0;
	while(t--){
		cas++;
		cin>>n>>k;
		
		for(int i=1;i<=n;i++){
			cin>>p[i];
		}
		
		int End = (1<<n);
		for(int i=1;i<End;i++){
			if(cnt_bit(i)!=k){
				continue;
			}
			
			int npos = 1;
			int pos = 1;
			for(int j=0;j<n;j++){
				if(i&(1<<j)){
					pp[pos++] = p[j+1];
				}
				npos++;
			}
			
		}
		
	}
	
	return 0;
}

/*
int min3(int a,int b,int c){
	return min(a,min(b,c));
}

int max3(int a,int b,int c){
	return max(a,max(b,c));
}

int main(){
	int t;
	cin>>t;
	
	while(t--){
		int n,r,p,s;
		cin>>n>>r>>p>>s;
		
		int MIN = min3(r,p,s);
		int MAX = max3(r,p,s);
		
		if(MIN+1<MAX){
			
		}
		
	}
	return 0;
}

*/
