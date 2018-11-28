#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int tc=0;tc<t;tc++){
		long long N;
		cin>>N;
		long long bit=0;
		
		if(N==0){
			printf("Case #%d: INSOMNIA\n",tc+1);
			continue;	
		}
		
		long long temp=N,i=1;
		while(bit!=1023){
			long long digit = temp%10;
			bit |= 1<<digit;
			temp = temp/10;
			if(temp == 0){
                i++;
                if(bit==1023)break;
				temp = i*N;
			}
		}
		if(temp)i++;
		printf("Case #%d: %lld\n",tc+1,(i-1)*N);
	}
	return 0;
}