#include <iostream>

using namespace std;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin>>T;
	int digit[10];
	int i,j;
	for(int t=0;t<T;t++){
		string str;
		cin >> str;
		int ind = 0;
		int n = str.length()-1;
		while(n>=0 && str[n]=='+')n--;
		n++;
		int flip = 0;
		while(ind < n){
			char cur = str[ind];
			while(ind < n && str[ind] == cur)ind++;
			if(ind >= n){
				if(str[ind-1] != '+'){
					flip++;
				}
				break;
			}
			flip++;
		}
		printf("Case #%d: %d\n", t+1, flip);
	}

}