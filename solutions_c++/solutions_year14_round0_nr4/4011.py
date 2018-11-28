#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <queue>
#include <map>
#include <stack>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;
int n;



int main(){

	freopen("D-large.in","r",stdin);
	freopen("salidabig.out","w",stdout);

	
	int t;
	
	scanf("%d",&t);
	
	
	for(int c=0;c<t;c++){
		vector<int> naomi;
		vector<int> ken;
		deque<int> ndipolo;
		deque<int> kdipolo;

		scanf("%d",&n);
		double a;
		for(int i=0;i<n;i++){
			scanf("%lf",&a);
			naomi.push_back(int(100000.0*a+0.000001));


		}
		
		for(int i=0;i<n;i++){
			scanf("%lf",&a);
			ken.push_back(int(100000.0*a+0.000001));
			
			//cout<<ken[i]<<endl;
		}
		
		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		
		for(int i=0;i<n;i++){
			ndipolo.push_back(naomi[i]);
			kdipolo.push_back(ken[i]);
		}
		
		int guerraEN=0;
		int guerraEK=0;
		int guerraN=0;
		int guerraK=0;
		
		int can=n;
		while(can>0){
			int na=ndipolo.back();
			int ke=kdipolo.back();
			
			if(na>ke){
				guerraN++;
				kdipolo.pop_front();
				ndipolo.pop_back();
			}else{
				guerraK++;
				kdipolo.pop_back();
				ndipolo.pop_back();
			}
			can--;
			
		}
		//cout<<guerraN<<endl;
		
		for(int i=0;i<n;i++){
			ndipolo.push_back(naomi[i]);
			kdipolo.push_back(ken[i]);
		}
		
		can=n;
		while(can>0){
			int na=ndipolo.front();
			int ke=kdipolo.front();
			

			
			if(na>ke){
				guerraEN++;
				kdipolo.pop_front();
				ndipolo.pop_front();
			}else{
				guerraEK++;
				kdipolo.pop_back();
				ndipolo.pop_front();
			}
			can--;
			
		}
		//cout<<guerraEN<<endl;
		printf("Case #%d: %d %d\n",c+1,guerraEN,guerraN);
	
		
		
	}
	
	
}