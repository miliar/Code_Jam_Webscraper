#include<cstdio>

int main(){
//	freopen("test.txt","r",stdin);
//	freopen("ans.txt","w",stdout);
	
	freopen("A-large.in","r",stdin);
	freopen("largeOutput.txt","w",stdout);

//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("smallOutput.txt","w",stdout);
	
	int t,n;
	long ans1, ans2, maxDiff;
	int input[1000];
	scanf(" %d",&t);
	for(int l=0;l<t;l++){
		scanf(" %d",&n);
		ans1 = 0; ans2 = 0; maxDiff = 0;
		for(int i=0;i<n;i++)
			scanf(" %d",&input[i]);
		
		for(int i=1;i<n;i++){
			if(input[i-1]-input[i] > 0){
				ans1 += input[i-1]-input[i];
				if(maxDiff < (input[i-1]-input[i]) )
					maxDiff = input[i-1]-input[i];
			}
		}
		
		for(int i=0;i<n-1;i++){
			if(input[i] < maxDiff)
				ans2 += input[i];
			else
				ans2 += maxDiff;
		}
		
		printf("Case #%d: %ld %ld\n",l+1,ans1,ans2);
	}
	return 0;
}
