#include <stdio.h>
#include <iostream>
#include <math.h>
#include <vector>
#include <utility>
#include <algorithm>
#include <string>
#include <set>

using namespace std;

int main() {
    freopen("D-large.in", "r",stdin);
    freopen("output.txt", "w",stdout);
    int n,k=1;
    scanf("%d",&n);
    while(n--){
		vector<double> a1,a3;
		double c;
		int b,z=0,y=0;
		scanf("%d",&b);
		for(int i=0;i<b;i++){
		scanf("%lf",&c);
		a1.push_back(c);
			}
		for(int i=0;i<b;i++){
		scanf("%lf",&c);
		a3.push_back(c);
			}
		sort(a1.begin(),a1.end());
		sort(a3.begin(),a3.end());	
		int as=b-1,bs=b-1,as1=b-1,bs1=b-1;
		int gf=0,gf1=0;
		for(int i=0;i<b;i++){	
			if(a1[as]>a3[bs]){
				z++;
				as--;
				}else{
					as--;
					bs--;
					}
					
			if(a1[as1]>a3[bs1]&&a1[gf]>a3[gf1]){
				y++;
				gf++;
				gf1++;
				}else{
					gf++;
					bs1--;
				}
			}
		printf("Case #%d: %d %d\n",k,y,z);	
		k++;
	}
   
} 
