#include<cstdio>

using namespace std;

#define MAX_S 1100
#define min(a,b) ( (a)<(b)?(a):(b))


int main(void)
{
	int cases;
	int cas;
	char s[MAX_S];
	int s_max;
	int i;
	int ans;
	int total;

	scanf("%d",&cases);
	
	for(cas=1;cas<=cases;cas++){
		ans=0;
		total=0;
		scanf("%d %s",&s_max,s);
		for(i=0;i<=s_max;i++){
			if(total<i){
				if(s[i]-'0' !=0){
					ans+=i-total;
					total+=(i-total);
				}
			}
			total+=s[i]-'0';
		}

		printf("Case #%d: %d\n",cas,ans);
	}


}
