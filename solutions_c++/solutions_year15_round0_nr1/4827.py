#include <iostream>
#include <stdio.h>

using namespace std;
int main() {
	int T;
	cin>>T;
	for(int t_i=0; t_i<T; ++t_i) {
		int max_shy;
		cin>>max_shy;
		string aud_shy;
		cin>>aud_shy;
		// printf("Case[%d] max_shy[%d] aud_shy[%s] aud_shy_1[%d]\n",t_i, max_shy,aud_shy.c_str(),aud_shy[1]-'0');
		int add = 0;
		int stand = 0;
		for(int aud_i=0; aud_i<max_shy+1; ++aud_i) {
			int mem_i = aud_shy[aud_i] - '0';
			if(!mem_i)
				continue;
			if(stand >= aud_i) {
				stand+=mem_i;
			} else {
				int req = aud_i - stand;
				stand += req;
				stand += mem_i;
				add +=req;
			}
		}
		printf("Case #%d: %d\n",(t_i+1), add);
	}
	return 0;
}