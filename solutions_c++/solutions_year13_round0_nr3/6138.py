#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

void reverse(char s[]) //extraido Lenguaje C, KERNIGHAN,Dennis M. Ritchie
{
	int c,i,j;
	
	for(i=0,j = strlen(s)-1; i < j;i++,j--) {
		c = s[i];
		s[i]=s[j];
		s[j]=c;
	}
	
}


bool espalindromo(int n) {

	char s1[10];
	char s2[10];
	
	sprintf(s1,"%d",n);
	strcpy(s2,s1);
	reverse(s2);
	//printf("%s = %s \n",s1,s2);
	if(strcmp(s1, s2) == 0 )
		return true;
	
	return false;
}

bool cuadpalindromo(int n) {
	float c=0;
	int aux=0;
	
	c = sqrt((float)n);
	aux = (int)c;
	if(aux*aux == n)
		if(espalindromo(aux))
			return true;
	
	return false;
}

int square(int a, int b) {
	int res = 0;
	int i=0;
	
	for(i=a;i<=b;i++) {
		if(espalindromo(i) && cuadpalindromo(i))
			res++;
	}
	
	return res;
}


int main()
{
	int n,j,aux=0;
	char c;
	int res = 0;
	
	scanf("%d\n",&n);
	if(!(n>0 && n<=100))
		perror("t fuera de limite\n");
	fflush(stdin);
	
	int a[n],b[n];
	
	for(j=0;j<n;j++) {
		scanf("%d",&aux);
		a[j] = aux;
		scanf("%c",&c);
		scanf("%d",&aux);
		b[j] = aux;
	}
	
	
	for(j=0;j<n;j++) {
		res = square(a[j],b[j]);
		printf ("Case #%d: %d\n", j+1,res);
	}

	return 0;
}

