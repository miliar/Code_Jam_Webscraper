#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <functional>

#define MAXLEN 1500000

using namespace std;
unsigned int long long size;
FILE *input, *output;

unsigned int long long a,n;
char str[MAXLEN];
char mo[6] = "aeiou";
unsigned int long long temp[MAXLEN];

int main(void)
{
	memset(temp, 0, sizeof(unsigned int long long)*MAXLEN);
	if((input = fopen("A-large.in", "rt")) == NULL)
	{
		printf("input fopen err\n");
		return 0;
	}

	if((output = fopen("A-large.out", "wt")) == NULL)
	{
		printf("output fopen err\n");
		return 0;
	}

	fscanf(input,"%lld",&size);
	
	int tempindx = 0;

	for( unsigned int long long i = 0 ; i < size ; i++ ) 
	{
		unsigned int long long  check = 0;
		unsigned int long long  count = 0;
		tempindx = 0;
		memset( str, 0, MAXLEN );
		fscanf(input,"%s %lld", str, &n);
		int len = strlen(str);
		for( int j = 0 ; j < len ; j++ ) {
			if( str[j] == 'a' || str[j] == 'e' || str[j] == 'i'  || str[j] == 'o'  || str[j] == 'u' ) {
				//str[j] = 'a';
				check = 0;
			}
			else {
				//str[j] = 'b';
				check++;
				if( check == n ) {
					temp[tempindx++] = j - n + 1;
					check = n -1 ;
				}
			}
		}

		for( int j = 0 ; j < tempindx ; j++ ) {
			if( temp[j] == 0 ) 
				count += len - (temp[j] + n) + 1;
			else if ( j != 0 )
				count += (temp[j] - temp[j-1]) * (len - temp[j] - n + 1);
			else
				count += (temp[j] + 1) * (len - temp[j] - n + 1);
		}
		fprintf(output, "Case #%lld: %lld\n", i+1 , count);
		//printf("%d", i);
	}

	return 0;
}