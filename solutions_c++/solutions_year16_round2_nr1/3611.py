#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(){

	int *p = (int*)malloc(sizeof(int));
	*p = 'a';
    int i,j;
	while (1) {

        printf("%d\n\n" , -10%7);
        memset(p,'a',10);
		for(i=0;i<5;i++)
        {
            printf("%x: %x\n\t",p,*(long*)p);
            for(j=0;j<4;j++)
                printf("%x %x  ",((unsigned char*)p)+j, *((unsigned char*)p+j));
            printf("\n\t");
            for(j=0;j<4;j++)
                printf("%x %x  ",((char*)p)+j, *((char*)p+j));
            printf("\n");
            p++;
        }
        scanf("%c\n",&i);
	}

}
