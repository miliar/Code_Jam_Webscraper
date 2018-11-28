#include<cstdio>
#include<cstdlib>


int main(){
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("smallOutput.txt","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("largeOutput.txt","w",stdout);
//	
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);

//	freopen("input.in","r",stdin);
//	freopen("output.in","w",stdout);

	int t,n;
	int s[1001],splus[1001];
	int ans;
	scanf("%d",&t);
	for(int k=0;k<t;k++)
	{
		ans=0;
		scanf(" %d ",&n);
		for(int i=0;i<=n;i++){
			s[i] = (int)(getchar()-'0');
			if(i==0){
				splus[i] = s[i];
			}else{
				if(splus[i-1] < i){
					//less than reqd for ovation
					ans+= i-splus[i-1]; // no of frnds reqd
					splus[i-1] += i-splus[i-1];
				}
				splus[i] = splus[i-1]+s[i];
			}
			
		}

		printf("Case #%d: %d\n",k+1,ans);
	}
}
