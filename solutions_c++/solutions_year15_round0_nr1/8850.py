#include <stdio.h>
#include <string.h>

int main(){
	int t, n, i, r=1, peopleNeeded, numberOfPeopleNeededActuallyToOvate, peopleInILevel, peopleStoodUp;
	
	char audience[1003];
	memset(audience,' ', 1003);

	while (scanf("%d", &t)==1){
		while(r<=t){
			peopleNeeded=0;
			peopleStoodUp=0;
			scanf("%d %s", &n, audience);
			//printf("audience %s\n", audience);

			for(i=0; i<=n; i++){
				peopleInILevel = audience[i] - '0';
				//printf("Analising level %d with %d people char %c.\n", i, peopleInILevel, audience[i]);
				//printf("people needed before:%d\n", peopleNeeded);
				if(peopleInILevel> 0){
					if(i > peopleStoodUp+peopleNeeded) peopleNeeded += i - (peopleStoodUp+peopleNeeded);
					peopleStoodUp += peopleInILevel;
				}
			}

			printf("Case #%d: %d\n", r++, peopleNeeded);
		}		
	};
return 0;
}
