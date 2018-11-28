#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(i=a;i<b;i++)
int main(){
	freopen("inp.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i,j,idx = 1;
	cin >> t;
	while(t--){
		double naomi[1002];
		double ken[1002];
		int n;
		cin >> n;
		rep(i,0,n){
			cin >> naomi[i];
		}
		rep(i,0,n){
			cin >> ken[i];
		}
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		int w=0,k=0,dwar = 0;
	for (i = n-1, j = n-1; i >= 0; i--) {
   		 if (naomi[i] > ken[j] && j >= k) {
    		w++;
    		k++;
    	}		 	
		else {
    		j--;
    	}
    }
     
    for (i = n-1, j = n-1; i >= 0; i--) {
    	if (naomi[i] < ken[0]) {
    		break;
    }
    	if (j < 0) {
    		break;
    	}
    	if (naomi[i] > ken[j]) {
    		dwar++;
    		j--;
    		} else {
    while (ken[j] > naomi[i] && j >= 0) {
    	j--;
    }
    	if (j >= 0) {
    		dwar++;
    		j--;
    	}
    }
    }
		cout << "Case #"<<idx<<":"<<" " <<dwar<<" "<<w<<"\n";
		idx++;
		
	}
	return 0 ;
}
