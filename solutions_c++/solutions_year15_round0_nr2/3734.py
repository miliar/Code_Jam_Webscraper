#include<cstdio>

int main(){
	
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);

	freopen("B-large.in","r",stdin);
	freopen("largeOutput.txt","w",stdout);

//	freopen("B-small-attempt0.in","r",stdin);
//	freopen("smallOutput.txt","w",stdout);
	
	int t,d,maxd;
	int p[1000];
	long ansp[1000];
	long ans;
	
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		ans=0;
		scanf(" %d",&d);
		maxd = 0;
		
		for(int j=0;j<d;j++){
			scanf("%d",&p[j]); // input
			if(p[j] > maxd)	// finding the max no of Pancakes
				maxd = p[j];
			
		}
		
		for(int k=0;k<maxd;k++){
			ansp[k] = k+1; // initialising ans array
			for(int j=0;j<d;j++){
				ansp[k] += (p[j]-1)/(k+1); // no of min reqd to reduce to kth value
			}
			if(k==0){
				ans = ansp[k];
			} else if( ans > ansp[k]){
				ans = ansp[k];
			}
		}
		printf("Case #%d: %ld\n",i+1,ans);
	}
	
	return 0;
}
