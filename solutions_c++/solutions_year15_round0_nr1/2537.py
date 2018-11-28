#include <cstdio>
#include <iostream>
using namespace std;
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc = 1; tc<=t ;++tc){
		int n,sum=0,need=0;
		string ins;
		cin>>n>>ins;

		for(int i=0;i<=n;++i){
			if(sum < i){
				need += i-sum;
				sum=i;
			}
			sum+=ins[i]-'0';
		}

		printf("Case #%d: %d\n",tc,need);
	}
	return 0;
}