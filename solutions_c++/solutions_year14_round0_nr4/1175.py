#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string.h>

using namespace std;

int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
		int s;
		int oldg,newg;
		oldg = newg = 0;
		double temp;
		vector<double> onaomi;
		vector<double> oken;
		vector<double> nnaomi;
		vector<double> noken;
		scanf("%d",&s);
		for(int ii=0;ii<s;ii++) {
			scanf("%lf",&temp);
			nnaomi.push_back(temp);
			onaomi.push_back(temp);
		}
		for(int ii=0;ii<s;ii++) {
			scanf("%lf",&temp);
			noken.push_back(temp);
			oken.push_back(temp);
		}
		sort(nnaomi.begin(),nnaomi.end());
		sort(noken.begin(),noken.end());
		sort(onaomi.begin(),onaomi.end());
		sort(oken.begin(),oken.end());
		vector<double>::iterator itr;
		while(nnaomi.size()) {
			if(*(nnaomi.end()-1) > *(noken.end()-1)) {
				nnaomi.erase(nnaomi.end()-1);
				noken.erase(noken.end()-1);
				newg++;
			} else {
				nnaomi.erase(nnaomi.begin());
				noken.erase(noken.end()-1);
			}
		}
		while(onaomi.size()) {
			if(*(onaomi.end()-1) > *(oken.end()-1)) {
				onaomi.erase(onaomi.end()-1);
				oken.erase(oken.begin());
				oldg++;
			} else {
				itr = oken.begin();
				while(*itr < *(onaomi.end()-1)) {
					itr++;
				}
				onaomi.erase(onaomi.end()-1);
				oken.erase(itr);
			}
		}
		printf("Case #%d: %d %d\n",i,newg,oldg);
	}
}
