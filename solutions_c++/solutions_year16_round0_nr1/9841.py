#include <stdio.h>

int main() {
	

	int in[1000], in2[1000], in3[1000], cc=1, numvals;

	scanf_s("%d", &numvals);

	for (int i=0; i<numvals; i++) {
		scanf_s("%d", &in3[i]);
	}

	printf("\n");

	for (int i=0; i<numvals; i++) {
		bool a[10] = {false,false,false,false,false,false,false,false,false,false};
		bool exit=false;
		cc=1;

		if (in3[i]!=0) {
			while (exit==false) {
				exit=false;

				in2[i]=in3[i]*cc;

				cc++;

				in[i]=in2[i];

				while (in[i]>0) {
					a[in[i]%10]=true;

					exit=true;
	
					for (int b=0; b<10; b++) {
						if (!a[b]) {
							exit=false;
						}
					}

					if (exit==true) {
						in[i]=0;
					}

					in[i] = in[i]/10;
				}
			}

			printf("Case #%d: %d \n", i+1, in2[i]);
		} else {
			printf("Case #%d: INSOMNIA \n", i+1);
		}
	}

	scanf_s("%d", &in3[10000]);
}