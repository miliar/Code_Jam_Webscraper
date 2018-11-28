#include<bits/stdc++.h>
using namespace std;
char in[1000];
int main(){
	int t;
	cin >> t;
	for(int tc = 1;tc <= t;++tc){
		scanf(" %s", in);
		int N = strlen(in);
		int last = 0;
		for(int i = 1;i < N;++i){
			if(in[i] != in[last]){
				++last;
				in[last] = in[i];
			}
		}
		++last;
		int cntp = 0, cntn = 0;
		for(int i = 0;i < last;++i){
			if(in[i] == '+') ++cntp;
			else ++cntn;
		}
		printf("Case #%d: ", tc);
		if(last & 1){
			if(cntp == 0){
				printf("1\n");
			} else if(cntn == 0){
				printf("0\n");
			} else if(cntp > cntn){
				printf("%d\n", last - 1);
			} else{
				printf("%d\n", last);
			}
		} else{
			if(cntp == 0){
				printf("1\n");
			} else if(cntn == 0){
				printf("0\n");
			} else if(in[0] == '+'){
				printf("%d\n", last);
			} else {
				printf("%d\n", last - 1);
			}
		}
	}
	return 0;
}