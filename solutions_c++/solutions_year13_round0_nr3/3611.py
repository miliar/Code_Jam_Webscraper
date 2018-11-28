#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
using namespace std;

void itoa(int num,char *buffer, int tam){
	int tmp = num;
	int cnt = 0;
	while(tmp>0){
		tmp/=10;
		cnt++;
	}
	for(int x = cnt-1;x>=0;x--){
		buffer[x]=num%10+48;
		num/=10;
	}
	buffer[cnt]='\0';
}


bool isPal(int num){

	if(num<10) return true;

	char buffer[10];
	itoa(num,buffer,10);
	//printf("%d es --- %s\n",num,buffer);
	bool es = true;
	int tmp = strlen(buffer);
	for(int x=0;x<tmp/2;x++)
		es = es && buffer[x]==buffer[tmp-1-x];

	//printf("%d\n",es);
	return es;
}
int main(){

	int t;

	scanf("%d",&t);
	for(int p=0;p<t;p++){
		printf("Case #%d: ",p+1);
		int cnt =0;
		int a,b;
		scanf("%d %d",&a,&b);

		for(int x=0;x<=b && x*x<=b;x++)
			if(x*x>=a && isPal(x) && isPal(x*x)) cnt++;
		
		printf("%d",cnt);


		if(p!=t-1) printf("\n");
	}

	return 0;
}
