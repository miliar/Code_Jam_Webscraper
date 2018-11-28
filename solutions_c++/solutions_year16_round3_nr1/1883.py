#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int t;
	scanf("%d",&t);
	for(int i=1; i<=t; i++){
		printf("Case #%d: ",i);
		int n;
		scanf("%d",&n);
		vector<pair<int,char> > party;
		party.push_back(make_pair(0,'\0'));
		char s='A';
		for(int j=0; j<n; j++){
			int p;
			scanf("%d",&p);
			party.push_back(make_pair(p,s));
			s++;
		}
		sort(party.begin(),party.end());
		for(int j=n-1; j>=0; j--){
			int len=(n-j);
			int p=party[j].first;
			if(party[n].first>p){
				if(len>=3){
					for(int l=n; l>j+2; l--){
						int k=party[l].first-p;
						char c=party[l].second;
						for(int m=0; m<k; m++) printf("%c ",c);
					}
					int k=party[j+1].first-p;
					char c1=party[j+1].second, c2=party[j+2].second;
					for(int m=0; m<k; m++) printf("%c%c ",c1,c2);
				}
				else if(len==2){
					int k=party[j+1].first-p;
					char c1=party[j+1].second, c2=party[j+2].second;
					for(int m=0; m<k; m++) printf("%c%c ",c1,c2);
				}
				else if(len==1){
					int k=party[j+1].first-p;
					char c1=party[j+1].second;
					for(int m=0; m<k; m++) printf("%c ",c1);
				}
				for(int l=n; l>j; l--){
					party[l].first=p;
				}
			}
		}
		printf("\n");
	}
}
