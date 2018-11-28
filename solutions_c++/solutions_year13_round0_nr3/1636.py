#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int numDig(unsigned long long inp){
	int size=0;
	unsigned long long temp = inp;
	while(temp!=0) { temp/=10; size++;}
	return size;
}

unsigned long long mirr(unsigned long long inp, int size, int l){
	unsigned long long temp, rev=0;
	int cnt=l;
	while(cnt--) inp = inp / 10;
	if(size-2*l) temp = inp/10;
	else temp = inp;
	cnt = l;
	// printf("temp: %llu\t", temp);
	while(cnt--){
		rev*=10;
		rev += temp%10;
		temp/=10;
	}
	// printf("inp: %llu\tRev: %llu\t", inp,rev);
	cnt = l;
	while(cnt--) inp = inp * 10;
	inp += rev;
	return inp;
}

unsigned long long nextPal(unsigned long long inp){
	int size=0, i;
	unsigned long long temp;
	size = numDig(inp);
	i=size/2; temp=1;
	while(i--){temp *= 10;}
	inp += temp;
	if(size%2){
		if(numDig(inp)>size) return mirr(inp,numDig(inp),size/2)+1;
		return mirr(inp,size,size/2);
	}
	else{
		if(numDig(inp)>size) return mirr(inp,numDig(inp),size/2);
		return mirr(inp,size,size/2);
	}
}

int main()
{
	unsigned long long x,y,z,i,t1,t2,sum;
	char string[101];
	int ii,j,t;
	scanf("%d", &t);
	for(int k = 1; k<=t; k++){
		scanf("%llu %llu",&x,&y);
		// printf("\t\t%llu \t\t%llu\n\n",x,y);
		y = (long long) sqrt(y);
		x = (long long) ceil (sqrt(x));
		sum = 0;
			for(i=x;i<=y;)
			{
				// printf("\t\ntesting: %llu",i);
				snprintf(string,101,"%llu",i);
				j = (strlen(string)/2) + 1;
				for(ii=0;ii<j;ii++)
						if(string[ii]!=string[strlen(string)-ii-1]) break;
				if(ii==j){
					if(i<=1000000000){
					 z = i*i;
					 snprintf(string,101,"%llu",z);
					}
					else{
						t1 = i%10;
						t2 = i/10;
						z = t2*t2 + 2*t1*t2;
						snprintf(string,101,"%llu",z);
						t2 *= t2;
						string[strlen(string)-1] = t2/10 + '0';
						string[strlen(string)] = t2%10 + '0';
						string[strlen(string)+1] = '\0';
					}

						j = (strlen(string)/2) + 1;

						for(ii=0;ii<j;ii++)
								if(string[ii]!=string[strlen(string)-ii-1]) break;

					if(ii==j){
							// printf ("i:%llu z:%llu\n",i,z);
							sum++;
						}
					i = nextPal(i)-1;
					}
					i++;
			}
			printf("Case #%d: %llu\n", k, sum);
	}
	return (0);
}