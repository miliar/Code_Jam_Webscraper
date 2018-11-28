#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
vector<double> naomi, ken;

int war(){
	int n = 0, k = 0;
	int a = naomi.size(), b = ken.size();
	int count = 0;
	while(n < a && k < b){
		if(naomi[n] > ken[k]){
			n++;b--;count++;
		}
		else if(ken[k] > naomi[n]){
			k++;n++;
		}
	}
	return count;
}

int deWar(){
	int n = 0, k = 0;
	int a = naomi.size(), b = ken.size();
	int count = 0;
	while(k<b && n < b){
		if(naomi[a-1] < ken[k]){
			n++;k++;
		}
		else if(naomi[a-1] > ken[k]){
			count++;k++;a--;
		}
	}
	return count;
}

bool mycomp (double i, double j) { return i>j;}

int main(){
	int t,n;
	double a;
	
	scanf("%d",&t);
	for(int i=1;i<=t;++i){
		scanf("%d",&n);
		for(int j=0;j<n;++j){
			scanf("%lf",&a);
			naomi.push_back(a);
		}
		for(int j=0;j<n;++j){
			scanf("%lf",&a);
			ken.push_back(a);
		}
		
		sort(naomi.begin(),naomi.end(),mycomp);
		sort(ken.begin(),ken.end(),mycomp);
		
		int out2 = war();
		sort(naomi.begin(),naomi.end());
		int out1 = deWar();
		
		printf("Case #%d: %d %d\n",i,out1,out2);
		
		naomi.clear();
		ken.clear();
	}
	return 0;
}