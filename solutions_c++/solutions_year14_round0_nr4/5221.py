#include<stdio.h>
#include<string.h>
#include<vector>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<limits>
#include<algorithm>

using namespace std;
typedef long long LL;
int main() {
	int caseNum;
	char dummy; //read the '\n' after the caseNum
	scanf("%d%c", &caseNum, &dummy);
	for (int caseCount = 1; caseCount <= caseNum; caseCount++) {
		int n;
		vector<double> Naomi;
		vector<double> Ken;
		int i;
		double t;
		scanf("%d",&n);
		for (i = 0; i < n; i++) {
			scanf("%lf", &t);
			Naomi.push_back(t);
		}
		for (i = 0; i < n; i++) {
			scanf("%lf", &t);
			Ken.push_back(t);
		}
		sort(Naomi.begin(),Naomi.end());
		sort(Ken.begin(),Ken.end());
		int deceitful=0;
		int plain=0;
		vector<double> NaomiCopy(Naomi);
		vector<double> KenCopy(Ken);
		for(i=0;i<n;i++){
			t=Ken[i];
			vector<double>::iterator itr;
			itr=lower_bound(NaomiCopy.begin(),NaomiCopy.end(),t);
			if(itr==NaomiCopy.end()){
				break;
			} else {
				NaomiCopy.erase(itr);
				deceitful++;
			}
		}
		printf("Case #%d: %d ", caseCount,deceitful);
		for(i=0;i<n;i++){
			t=Naomi[i];
			vector<double>::iterator itr;
			itr=lower_bound(KenCopy.begin(),KenCopy.end(),t);
			if(itr==KenCopy.end()){
				break;
			} else {
				KenCopy.erase(itr);
				plain++;
			}
		}
		printf("%d\n",n-plain);
	}
	return 0;
}
