#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<stdlib.h>

using namespace std;

int cmpfunc (const void * a, const void * b)
{
   return ( *(int*)a - *(int*)b );
}

void removeChar(char string[], char remove, int length){
	int a;
	for(a = 0; a < length; a++){
		if(string[a] == remove){
			string[a] = '\0';
			return;
		}
	}
}

int main(){
	int a;
	int b;
	int T;
	int num[700];
	char string[2000];
	int length;
	int count;
	
	scanf("%d", &T);
	
	for(a = 0; a < T; a++){
		count = 0;
		for(b = 0; b < 700; b++){
			num[b] = 10;
		}
		scanf("%s", string);
		length = strlen(string);
		//search zero
		for(b = 0; b < length; b++){
			if(string[b] == 'Z'){
				removeChar(string, 'Z', length);
				removeChar(string, 'E', length);
				removeChar(string, 'R', length);
				removeChar(string, 'O', length);
				num[count] = 0;
				count++;
			}
		}
		for(b = 0; b < length; b++){
			if(string[b] == 'X'){
				removeChar(string, 'S', length);
				removeChar(string, 'I', length);
				removeChar(string, 'X', length);
				num[count] = 6;
				count++;
			}
		}
		for(b = 0; b < length; b++){
			if(string[b] == 'S'){
				removeChar(string, 'S', length);
				removeChar(string, 'E', length);
				removeChar(string, 'V', length);
				removeChar(string, 'E', length);
				removeChar(string, 'N', length);
				num[count] = 7;
				count++;
			}
		}
		for(b = 0; b < length; b++){
			if(string[b] == 'G'){
				removeChar(string, 'E', length);
				removeChar(string, 'I', length);
				removeChar(string, 'G', length);
				removeChar(string, 'H', length);
				removeChar(string, 'T', length);
				num[count] = 8;
				count++;
			}
		}
		for(b = 0; b < length; b++){
			if(string[b] == 'W'){
				removeChar(string, 'T', length);
				removeChar(string, 'W', length);
				removeChar(string, 'O', length);
				num[count] = 2;
				count++;
			}
		}
		for(b = 0; b < length; b++){
			if(string[b] == 'T'){
				removeChar(string, 'T', length);
				removeChar(string, 'H', length);
				removeChar(string, 'R', length);
				removeChar(string, 'E', length);
				removeChar(string, 'E', length);
				num[count] = 3;
				count++;
			}
		}
		for(b = 0; b < length; b++){
			if(string[b] == 'V'){
				removeChar(string, 'F', length);
				removeChar(string, 'I', length);
				removeChar(string, 'V', length);
				removeChar(string, 'E', length);
				num[count] = 5;
				count++;
			}
		}
		for(b = 0; b < length; b++){
			if(string[b] == 'F'){
				removeChar(string, 'F', length);
				removeChar(string, 'O', length);
				removeChar(string, 'U', length);
				removeChar(string, 'R', length);
				num[count] = 4;
				count++;
			}
		}
		for(b = 0; b < length; b++){
			if(string[b] == 'I'){
				removeChar(string, 'N', length);
				removeChar(string, 'I', length);
				removeChar(string, 'N', length);
				removeChar(string, 'E', length);
				num[count] = 9;
				count++;
			}
		}
		for(b = 0; b < length; b++){
			if(string[b] == 'O'){
				removeChar(string, 'O', length);
				removeChar(string, 'N', length);
				removeChar(string, 'E', length);
				num[count] = 1;
				count++;
			}
		}
		qsort(num, count + 1, sizeof(int), cmpfunc);
		printf("Case #%d: ", a + 1);
		for(b = 0; b < count; b++){
			printf("%d", num[b]);
		}
		printf("\n");
	}
	return 0;
}
