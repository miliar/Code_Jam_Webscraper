#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int main(){
int t;
cin>>t;
for(int p=0;p<t;p++){
	
	int n;
	float temp;
	cin>>n;
	vector<float> naomi(n,0);
	vector<float> kent(n,0);
	set<float> kenset;
	for(int i=0;i<n;i++) cin>>naomi[i];
	for(int i=0;i<n;i++) cin>>kent[i];
	for(int i=0;i<n;i++) kenset.insert(kent[i]);

	sort(naomi.begin(),naomi.begin()+n);
	sort(kent.begin(),kent.begin()+n);

	int war=0,dwar=0;
	int naomipt=0,kenpt=0;

	for(int i=0;i<n;i++){
		if(naomi[naomipt]>kent[kenpt]) {dwar++;naomipt++;kenpt++;}
		else naomipt++;
	}
	
	set<float>::iterator itlow;
	
	for(int i=n-1;i>=0;i--){
		itlow=kenset.lower_bound(naomi[i]);
		if(itlow==kenset.end()) {kenset.erase(kenset.begin()); war++;}
		else kenset.erase(itlow);
	}
	printf("Case #%d: %d %d\n",p+1,dwar,war);
}
}
