// GJ 2014 A 
// Magician

#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;


int N;
int a1, a2;
int r1[4],r2[4];
int trash;
int ans;
int err;
int cases;


int main(){

	freopen("A-small-attempt00.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	cin >> N;
	cases=0;
	cin.ignore();
	while(N--){
		// input
		ans=0;
		err=0;
		scanf("%d",&a1);
		for(int j=0; j < 4; j++){
			if(j+1 == a1){	// if if guessed by magician
				for(int i=0; i < 4; i++){
					scanf("%d",&r1[i]);
				}
			}else{
				for(int i=0; i < 4; i++){
					scanf("%d",&trash);
				}
			}
		}
		scanf("%d",&a2);
		for(int j=0; j < 4; j++){
			if(j+1 == a2){	// if if guessed by magician
				for(int i=0; i < 4; i++){
					scanf("%d",&r2[i]);
				}
			}else{
				for(int i=0; i < 4; i++){
					scanf("%d",&trash);
				}
			}
		}
		// debug
		/*
		for(int i=0; i < 4; i++){
			printf("%d ",r1[i]);
		}
		cout << endl;
		for(int i=0; i < 4; i++){
			printf("%d ",r2[i]);
		}
		cout << endl<<endl;
		*/

		for(int i=0; i < 4; i++){

			for(int j=0; j < 4; j++){
				if(r1[i]== r2[j]){
					if(ans==0){
						ans=r1[i];
					}else{
						err=1;
						break;
					}
				}
			}
			if(err)break;

		}
		if(err==1)
			printf("Case #%d: Bad magician!\n",++cases);
		else if(ans==0)
			printf("Case #%d: Volunteer cheated!\n",++cases);
		else 
			printf("Case #%d: %d\n",++cases,ans);
	}


return 0;
}