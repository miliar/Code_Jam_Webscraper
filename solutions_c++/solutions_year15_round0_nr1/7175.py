#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

int ExecCase(int *vec, int len)
{
    int total = vec[0];
    int nGuest = 0;
    for (int i = 1; i < len; ++i) {
        if(total >= i){
            total += vec[i];
        }else{
            nGuest += i - total;
            total += (i - total) + vec[i];
        }
    }
    return nGuest;
}

int main() {

    int nTest;
    int smax;

    scanf("%d",&nTest);
    for(int t = 0; t < nTest; t++)
    {
    	char buffer;
        scanf("%d ",&smax);
		int *vec = (int*) malloc (sizeof(int)*(smax+1));
		for(int i = 0; i <= smax; i++){
			scanf("%c",&buffer);
			vec[i] = buffer - '0';
		}
        cout << string("Case #") << t+1 << ": " << ExecCase(vec,smax+1) << endl;
        free(vec);
    }
    return 0;
}

