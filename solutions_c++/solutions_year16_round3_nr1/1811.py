#include<iostream>
using namespace std;
int tab[26], sum = 0, maks, cnt;
	int n, t;
int main(){
	
	cin>>t;
	for(int i = 0; i < t; i++){
		cin>>n;
		cout<<"Case #"<<i+1<<": ";
		for(int j = 0; j < n ; j++){
			cin>>tab[j];
			sum+=tab[j];
		}
		while(sum > 0){
			maks = 0;
			cnt = 0;
			for(int i = 0 ; i < 26; i++){
				if(tab[i] > maks){
					maks = tab[i];
					cnt = 1;
				}
				else{
					if(tab[i] == maks){
						cnt++;
					}
				}
			}
			if(cnt == 1){
				int actCnt = 0;
				for(int j = 0; j < 26;j++){
					if(tab[j] == maks){
						tab[j]-=2;
						sum-=2;
						actCnt+=2;
						cout<<(char)('A'+j)<<(char)('A'+j);
					}
					if(actCnt == 2)break;
				}
			}
			else if(cnt == 2){
				int actCnt = 0;
				for(int j = 0; j < 26;j++){
					if(tab[j] == maks){
						tab[j]--;
						sum--;
						actCnt++;
						cout<<(char)('A'+j);
					}
					if(actCnt == 2)break;
				}
			}
			else{
				if(maks <= (sum-2)/2){
					int actCnt = 0;
					for(int j = 0; j < 26;j++){
						if(tab[j] == maks){
							tab[j]--;
							sum--;
							actCnt++;
							cout<<(char)('A'+j);
						}
						if(actCnt == 2)break;
					}
				}
				else{
					int actCnt = 0;
					for(int j = 0; j < 26;j++){
						if(tab[j] == maks){
							tab[j]--;
							sum--;
							actCnt++;
							cout<<(char)('A'+j);
						}
						if(actCnt == 1)break;
					}
				}
			}
			cout<<" ";
		}
		cout<<endl;
		
	}
	return 0;
}

