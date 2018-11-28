#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#define limit 2000
using namespace std;

int main(){
	int time=0,k=1;
	scanf("%d",&time);
	while(time--){
		int people[limit];
		memset(people,0,sizeof(people));
		int total=0,time=0;
		scanf("%d",&total);
        for(int a=0;a<total;a++){
			scanf("%d",&people[a]);
        }
        sort(people,people+total);
        reverse(people,people+total);
        int ans=people[0]+100;
		for(int t=people[0];t>0;t--){
			int tmpans=0;
			for(int a=0;a<total;a++){
				if(people[a]>t){
					tmpans=tmpans+((people[a]/t)-1);
					if(t*(people[a]/t)<people[a]){
						tmpans++;
					}
				}
			}
			tmpans=tmpans+t;
			ans=min(ans,tmpans);
		}
		printf("Case #%d: %d\n",k,ans);
		k++;
	}
	return 0;
}
