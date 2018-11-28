#include <iostream>
#include <string>
#include <cstring>
using namespace std;
int num[101];
int work(int r, int j){
	if(r == 0){
		if(num[r]==j)
			return 0;
		else
			return 1;
	}else{
		if(num[r]==j)
			return work(r-1,j);
		else
			return 1+work(r-1,1-j);
	}
}
int main(){
	int t;
	string in;
	while(cin >> t){
		int i = 1;
		while(t--){
			cin >> in;
			int len = in.size();
			memset(num,0,sizeof(num));
			for(int i = 0; i < len; i++){
				if(in[i]=='-')num[i]=0;
				else num[i]=1;
			}
			int ans = work(len-1,1);
			cout<<"Case #"<<i<<": "<<ans<<endl;
			i++;
		}
	}
}