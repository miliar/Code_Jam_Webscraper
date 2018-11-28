#include <stdio.h>
#include <stdlib.h>
#include <math.h>

FILE *fi= fopen("C-large-1.in","r");
FILE *fo= fopen("C-large-1.out","w");	

int checkpelin(__int64 a){
	int i,n[1000],cnt=0;
	if(a<10)
		return 1;
	while(a!=0){
		n[cnt]=a%10;
		cnt++;
		a/=10;
		
	}
	for(i=0;i<=cnt/2;i++){
		if(n[i]!=n[cnt-1-i])
			break;
		if(i==cnt/2)
			return 1;
	}
	return 0;}

/*int square(__int64 a){
	__int64 i;
	//for(i=sqrt((double)a)-2;i<=sqrt((double)a);i++)
	{if(i*i==a)
	return 1;
	}
	return 0;}
	*/
int main(){
	int t,i,cnt=0;
	unsigned long long int a,b,j;
	
	fscanf(fi,"%d",&t);
	
	
	for(i=0;i<t;i++){
		fscanf(fi,"%llu %llu",&a,&b);

		for(j=a;j<=b;j++){
			if(j==1||j==4||j==9||j==121||j==484||j==10201||j==12321||j==14641||j==40804||j==44944||j==1002001||j==1234321||j==4008004||j==100020001||j==102030201||j==104060401||j==121242121||j==123454321||j==125686521||j==400080004||j==404090404||j==10000200001||j==10221412201||j==12102420121||j==12345654321||j==40000800004||j==1000002000001||j==1002003002001||j==1004006004001||j==1020304030201||j==1022325232201||j==1024348434201||j==1210024200121||j==1212225222121||j==1214428244121||j==1232346432321||j==1234567654321||j==4000008000004||j==4004009004004)
				cnt++;
		}

		fprintf(fo,"Case #%d: %d\n",i+1,cnt);
		cnt=0;
	}
	
	return 0;
}