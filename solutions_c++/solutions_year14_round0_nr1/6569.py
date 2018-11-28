#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

int main(int argc, char* argv[]) {
	int T;
	
	setbuf(stdout, NULL);
		

	scanf("%d\n", &T);
	for(int t=0; t<T; t++) {
		int r0, r1;
		int map[17];
		memset(map, 0, sizeof(map));

		scanf("%d", &r0);
		for (int i=0; i<4; i++) {
		    for (int j=0; j<4; j++) {
			     int v;
				 scanf("%d", &v);
			    if (i + 1 == r0)
                    map[v] += 1;				
			}
		}
		scanf("%d", &r1);
		for (int i=0; i<4; i++) {
		    for (int j=0; j<4; j++) {
			     int v;
				 scanf("%d", &v);
			    if (i + 1 == r1)
                    map[v] += 1;				
			}
		}
		
		int found = 0;
		int v;
		for(int i=1; i<=16; i++)
		    if (map[i] == 2) {
			    found++;
				v = i;
		}
		
		if (found == 0)
		     printf("Case #%d: Volunteer cheated!\n", t+1);
	    else if (found > 1)
		     printf("Case #%d: Bad magician!\n", t+1);
		else
			printf("Case #%d: %d\n", t+1, v);
	}
	
	return 0;
}
