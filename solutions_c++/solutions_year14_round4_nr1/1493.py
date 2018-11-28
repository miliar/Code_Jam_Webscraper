#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<utility>

using namespace std;

#define PB push_back
#define LE length()
#define SZ size()
#define MP make_pair
#define X first
#define Y second
int s[10005];
bool used[10005];
int main(){
	int kases; cin>>kases;
	for(int kase = 1; kase <= kases;kase++){
		int N,X; cin>>N>>X;
		for(int i=0;i<N;i++){
			cin>>s[i]; used[i] = false;
		}
		sort(s,s+N);
		int res = 0;
		for(int i=N-1;i>=0;i--){
			if(used[i])continue;
			res++; 
			int rem = X-s[i];
			for(int j=i-1;j>=0;j--){
				if(used[j])continue;
				if(s[j] <= rem){used[j] = true; break;}
			}
		}
		cout<<"Case #"<<kase<<": "<<res<<endl;
	}
}
