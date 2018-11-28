#include<vector>
#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include <set>
using namespace std;

double C, F, X;
double tt;

bool check(double s) {
	if(X/s <= C/s + X/(s+F))
		return false;
	return true;
}

int main() {
//	freopen ("D-large.in","r",stdin);
//	freopen ("out_large.txt","w",stdout);
	
	set<double> naomi;
	set<double> ken;
	int t;
	scanf("%d", &t);
	
	int y, z;
	while (t--) {
		naomi.clear();
		ken.clear();
		int n;
		scanf("%d", &n);
		
		double w;
		for(int i=0; i<n; i++){
			scanf("%lf", &w);
			naomi.insert(w);
		}
		for(int i=0; i<n; i++){
			scanf("%lf", &w);
			ken.insert(w);
		}
		
		y=0;
		double previous_2=-1;
		for(set<double>::iterator it=ken.begin(); it!=ken.end(); ++it){
			double a=*it;
			double b;
			set<double>::iterator itup;
			itup=naomi.upper_bound(a);
			if(itup==naomi.end()){
				break;
			}
			else {
				while(*itup<=previous_2){
					itup++;
					if(itup==naomi.end()){
						break;
					}
				}
				if(itup==naomi.end()){
					break;
				}
				y++;
				previous_2=*itup;
			}
		}
		
		
		z=0;
		double previous=-1;
		for(set<double>::iterator it=naomi.begin(); it!=naomi.end(); ++it){
			double a=*it;
			double b;
			set<double>::iterator itup;
			itup=ken.upper_bound(a);
			if(itup==ken.end()){
				z++;
			}
			else {
				while(*itup<=previous){
					itup++;
					if(itup==ken.end()){
						z++;
						break;
					}
				}
				if(itup==ken.end()){
					itup--;
				}
				previous=*itup;
			}
		}
		
		static int id = 0;
		printf("Case #%d: %d %d\n", ++id, y, z);
		
		
	}
	return 0;
}
