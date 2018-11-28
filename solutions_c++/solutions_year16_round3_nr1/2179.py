#include<bits/stdc++.h>

using namespace std;

int main(){
	int ppl[26] = {0},t,hold;
	cin>>t;
	hold = t;
	while(t){
		if(t<=0)return 0;
		t--;
		int sum =0,n;
		cin>>n;
		for(int i =0; i< n; i++){
			cin>>ppl[i];
			sum+=ppl[i];
		}
		cout<<"Case #"<<hold-t<<":"<<' ';
		while(sum){
			int max = 0;
			for(int i =0; i< n; i++){
				if(ppl[max]<ppl[i])
					max =i;
			}
			if(ppl[max]==sum/2 && sum%2==0){
				int max2 = 0;
				if(max2==max) max2++;
				for(int i =0; i< n; i++){
					if(i==max)continue;
					else{
						if(ppl[max2] < ppl[i])max2 = i;
					}
				}
				if(ppl[max2] == ppl[max]){cout<<(char)('A' + max2)<<(char)('A'+max)<<' ';sum-=2;ppl[max]--;ppl[max2]--;}
				else{ cout<<(char)('A' + max)<<' ';sum-=1;ppl[max]--;}
			}
			else{
				cout<<(char)('A' + max)<<' ';
				sum-=1;
				ppl[max]--;
			}
		}
		cout<<endl;
	}
	return 0;
}

