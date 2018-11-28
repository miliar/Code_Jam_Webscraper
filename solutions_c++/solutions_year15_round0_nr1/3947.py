#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include <vector>
#include <string>
#include <map>

int main(void)
{
	int t,T;
	scanf("%d\n",&T);
	for (t=1;t<=T;t++){
		int Smax;
		scanf("%d ",&Smax);
		char str[Smax+1];
		int n_s[Smax+1];
		scanf("%s\n",str);
		// fprintf(stderr,"Smax=%d\n",Smax);
		int i;
		for (i=0;i<=Smax;i++){
			n_s[i]=str[i]-'0';
			// fprintf(stderr,"n_s[%d]=%d\n,",i,n_s[i]);
		}
		assert(n_s[Smax]>0);
		int sakura=0;
		int sum_standing=0;
		for (i=0;i<=Smax;i++){
			if (sum_standing+sakura<i){
				// —§‚Á‚Ä‚¢‚él‚½‚¿‚Ì”‚ªshyness level–¢–‚È‚Ì‚ÅƒTƒNƒ‰‚ğ‘‚â‚·
				int new_sakura = i - sum_standing;
				assert(new_sakura>sakura);
				sakura = new_sakura;
			}
			sum_standing+=n_s[i];
		}
		printf("Case #%d: %d\n",t,sakura);
	}
	return 0;
}
