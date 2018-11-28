#include<bits/stdc++.h>
using namespace std;

int digit[10] = {0};

bool allDigits(){
	for(int i=0;i<=9;i++){
		if(digit[i]==0) return false;
	}
	return true;
}

int calc(int n){
	int i=1;
	int temp = n, prod = n,ans,cnt=0;
	while(!allDigits() && cnt<1000000){
		prod = i*temp;
		ans = prod;
		i++;
		while(prod){
			int d = prod%10;
			prod/=10;
			digit[d] = 1;
		}
		cnt++;
	}
	if(!allDigits()){
		return -1;
	}
	else
		return ans;
}
void init(){
	for(int i=0;i<=9;i++){
		digit[i]=0;
	}
}

int main(){
	int T,val=1;
	cin>>T;
	while(T){
		int n,ans;
		cin>>n;
		ans=calc(n);
		if(ans==-1)
			printf("Case #%d: INSOMNIA\n",val);
		else printf("Case #%d: %d\n",val,ans);
		init();
		val++;
		T--;
	}
	return 0;
}
