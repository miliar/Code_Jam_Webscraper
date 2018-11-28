#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int main(int argc, char *argv[]) {
	
	int N;
	cin>>N;
	
	int s_max,partial,ans;
	string s_k;
	
	vector<int> v;
	
	for(int i = 1; i <= N ; i++){
		ans = 0; partial = 0;
		cin>>s_max;
		cin>>s_k;
		for(int j = 0; j <= s_max ; j++){
			int x = (int)(s_k[j]-48);
			if(x==0)
				continue;
			else
				if(j>partial){
					ans+=j-partial;
					partial+=j-partial;
				}
				partial+=x;
		}
		printf("Case #%d: %d\n",i,ans);
	}
	
	return 0;
}

