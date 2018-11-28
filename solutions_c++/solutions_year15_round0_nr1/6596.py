#include <stdlib.h>
#include <stdio.h>

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);


	int lines;
	char aux;
	char aux2[1001];
	int Smax;
	int people;

	scanf("%d", &lines);

	for(int x = 0; x < lines; ++x){

		scanf("%*[ \n\t]%c", &aux);

		scanf("%*[ \n\t]%s", &aux2);

		int invited = 0;
		int total = 0;

		Smax = aux - '0';

		for(int S = 0; S <= Smax; ++S){

			people = aux2[S] - '0';

			if(S > total){

				invited += S - total;
				total = S + people;

			}else{
				total += people;
			}

		}

		printf("Case #%d: %d\n", x + 1, invited);

	}
	
	return 0;
}
