#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>

using namespace std;

int main(void){
	int z;
	scanf("%d\n",&z);
	for (int w = 1;w <= z; w++){
		vector<double> n1,n2,k1,k2;
		int m;
		scanf("%d\n",&m);
		n1.assign(m,0);
		k1.assign(m,0);
		n2.assign(m,0);
		k2.assign(m,0);
		for (int i = 0;i < m;i++){
			scanf(" %lf",&n1[i]);
			n2[i] = n1[i];
		}
		for (int i = 0;i < m;i++){
			scanf(" %lf",&k1[i]);
			k2[i] = k1[i];
		}

		sort(n1.begin(),n1.end());
		sort(k1.begin(),k1.end());
		sort(n2.begin(),n2.end());
		sort(k2.begin(),k2.end());
		
		int s = 0;
		for (int i=0;i < m; i++){
			if (k1[i] > -1){
				for (int l = 0; l < m; l++){
					if (n1[l] > -1){
						if (k1[i] > n1[l]){
							s++;
							n1[l] = -1;
							k1[i] = -1;
						}
					}
				}
			}
		}
		int s1 = m-s;
		int s2= 0;
		for (int i=0;i < m; i++){
			if (n2[i] > -1){
				for (int l = 0; l < m; l++){
					if (k2[l] > -1){
						if (n2[i] > k2[l]){
							s2++;
							n2[i] = -1;
							k2[l] = -1;
						}
					}
				}
			}
		}
		printf("Case #%d: %d %d\n",w,s2,s1);	
	}
}
