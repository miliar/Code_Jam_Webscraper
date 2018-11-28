#define maxar 124800
#define maxver 5000
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <math.h>
#include<stdlib.h>
#include<map>

using namespace std;

int vet[10000000];
char buffer[100];
void inicializa(long long int num);
int isPalindrome(long long int num);
long long int intervalo(long int a, long int b);

int main () {
	int casos =0;
	long long int a,b;
	//inicializa(10000000);
  inicializa(10000000);
	scanf("%d",&casos);
	for(int caso=1;caso<=casos;caso++){
	  scanf("%Ld %Ld",&a,&b);  
	  printf("Case #%d: %Ld\n", caso, intervalo(a,b));
	}
	
	
  return 0;
}



//Para o intervalo, basta achar a raiz quadrada e aproximar pra saber de onde
//até onde procurar no vetor
void inicializa(long long int num){
  for(long long int i=0;i<num;i++){
    //printf("1: %Ld %d 2:%Ld %d\n",(long long int)pow(i,2),isPalindrome((long long int)pow(i,2)),i,isPalindrome(i));
    if(isPalindrome((long long int)pow(i,2))&&isPalindrome(i))vet[i]=1;
    else vet[i]=0;
  } 
}

int isPalindrome(long long int num){
  int tam;
  sprintf(buffer,"%Ld",num);
  //printf("Buffer: %s\n",buffer);
  tam = strlen(buffer)-1;
  for(int i=0;i<=tam/2;i++){
    if(buffer[i]!=buffer[tam-i])return 0;
  }
  return 1;  
}

long long int intervalo(long int a, long int b){
  long long int num=0;
  a=ceil(sqrt(a));
  b=floor(sqrt(b));
  for(long long int i=a;i<=b;i++){
    num+=vet[i];
    //printf("numero: %Ld pow: %lf vet: %d\n",i,pow(i,2),vet[i]);
  }
  return num;
}

	
	
	
	

	
