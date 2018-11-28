#include <cstdio>
#include <algorithm>
using namespace std;
int has(int arr[],int row,int e){
	if(arr[(row-1)*4]==e)
		return 1;
	if(arr[(row-1)*4+1]==e)
		return 1;
	if(arr[(row-1)*4+2]==e)
		return 1;
	if(arr[(row-1)*4+3]==e)
		return 1;
	return 0;
}
int main(){
	int t;
	scanf(" %d",&t);
	int tt=0;
	while(tt<t){
		tt++;
		int ans1,ans2,i;
		int arr[16],arr2[16];
		scanf(" %d",&ans1);
		for(i=0;i<16;i++){
			scanf(" %d",&arr[i]);

		}
		scanf(" %d",&ans2);
		for(i=0;i<16;i++){
			scanf(" %d",&arr2[i]);

		}
		int count=0;
		int res=0;
		


		if(has(arr2,ans2,arr[(ans1-1)*4])) {
			res=arr[(ans1-1)*4];
			count++;
	}
		if (has(arr2,ans2,arr[(ans1-1)*4+1])){
			res=arr[(ans1-1)*4+1];
			count++;
		}
		if(has(arr2,ans2,arr[(ans1-1)*4+2]))
			{	res=arr[(ans1-1)*4+2];
				count++;
			}
		if(has(arr2,ans2,arr[(ans1-1)*4+3]))
			{	res=arr[(ans1-1)*4+3];
				count++;
			}
		if(count==1)
			printf("Case #%d: %d\n",tt,res);
		else if(count>1)
			printf("Case #%d: Bad magician!\n",tt);
		else
			printf("Case #%d: Volunteer cheated!\n",tt);

	}
}