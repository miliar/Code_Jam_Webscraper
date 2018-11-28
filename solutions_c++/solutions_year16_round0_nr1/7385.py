#include <stdio.h>


int main(int argc, const char* argv[]) {
	
	int numtests;
	int casenum = 0;
    int n;
    int check = 1;
    int *a;
    int tempn;
    int multiplier = 1;
    int original_n;

	//printf("ENTER NUMBER OF TEST CASES: ");
	scanf("%d", &numtests);

	while(++casenum <= numtests) {

		// read number of non-zero plate diners
		scanf("%d", &original_n);

		// Print case num and needed nums
		printf("Case #%d: ", casenum);

        if (original_n == 0)
            printf("INSOMNIA\n");

        else {
           
            a = new int[10];
            for (int i = 0; i < 10; i++)
                a[i] = 0;

            n = original_n; 

            check = 1;
            multiplier = 1;

            while (check) {

                //printf("Iteration-Number: %d\n", n);
                tempn = n;
                
                while (tempn != 0) {
                    a[tempn%10] = 1;
                    tempn /= 10;
                }
                
                check = 0;
                //printf("  n = %d\n", n);
                for (int i = 0; i < 10; i++){
                    if (a[i] == 0){
                        check = 1;
                //        printf("   Missing %d\n", i);
                    }
                }
                if (check)
                    multiplier++;
                    n = multiplier * original_n;
            }

            printf("%d\n", n);

            delete[] a;
        }

	}
}
