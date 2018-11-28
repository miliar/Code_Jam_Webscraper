#include <iostream>
#include <stdio.h>

using namespace std;

int a1[4][4],a2[4][4];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ans1,ans2,T;
	scanf("%d",&T);
	for(int z=0;z<T;z++){
		scanf("%d",&ans1);
		ans1--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				scanf("%d",&a1[i][j]);
			}
		}

		scanf("%d",&ans2);
		ans2--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				scanf("%d",&a2[i][j]);
			}
		}

		int oc = 0,oci = -1;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if(a1[ans1][i]==a2[ans2][j]){
					oc++;
					oci = i;
				}
			}
		}
		printf("Case #%d: ",z+1);

		if(oc==1){
			printf("%d\n",a1[ans1][oci]);
		}
		else if(oc>1){
			printf("Bad magician!\n");
		}
		else{
			printf("Volunteer cheated!\n");
		}
	}

}