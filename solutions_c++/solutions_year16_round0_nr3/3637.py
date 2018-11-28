#include<bits/stdc++.h>
#define ll long long

int prime(ll int n,ll int *div,int j){
	ll int n1 = sqrt(n);
	for(int i=2;i<=n1;i++){
		if(n%i==0){
			div[j]=i;
			return 0;
		}
	}
	return 1;	
}
/*
ll int convertToBase(char *s,int b){
	ll int res=0;
	int len = strlen(s);
	//printf("Length of String: %d\n",len);
	
	for(int i=0;i<len;i++){
		res = res + (pow(b,i)*(s[len-i-1]-'0'));
	}
	return res;
}

ll int divisor(ll int n){
	ll int n1 = sqrt(n);
	for(int i=2;i<=n1;i++){
		if(n%i==0){
			return i;
		}
	}
}
*/

int check(char *s,int n){
	int i,status=0;
	int len = strlen(s);
	ll int b[20]={0};
	ll int div[20];
	
	for(int j=2;j<=10;j++){
		b[j]=0;
		div[j]=0;
		for(int i=0;i<len;i++){
			b[j]+=(pow(j,i)*(s[len-i-1]-'0'));
		}
		ll int a;
		//printf("Number in base %d -> %lld\n",i,b[j]);
		if(prime(b[j],div,j)){
			status=1;
			break;
		}
		//num = convertToBase(s,i);	
	}
	if(status){
		return 0;
	}
	else{
		printf("%s ",s);
		
		for(i=2;i<=10;i++){
			printf("%lld ",div[i]);
		}
		
		printf("\n");
		return 1;	
	}
}

void generatejJamCoins(char *s,int n,int j,int *count,int index){
	if(*count==j){
		return;
	}
	if(index==n-1){
		//printf("\nFor String: %s\n",s);	
		if(check(s,n)){
			(*count)++;
			//printf("String: %s, Count: %d\n",s,*count);			
		}
		//index=0;
		return;
	}
	s[index]='0';
	generatejJamCoins(s,n,j,count,index+1);
	s[index]='1';
	generatejJamCoins(s,n,j,count,index+1);
	//s[index]='0';
}

int main(){
	
	int i,t,n,j;
	scanf("%d",&t);
	scanf("%d",&n);
	scanf("%d",&j);
	int count = 0;
	int index=1;
	char s[n+1];
	
	for(i=0;i<n;i++){
		s[i]='0';
	}
	s[i]='\0';
	s[0]=s[n-1]='1';
	printf("Case #1:\n");
	generatejJamCoins(s,n,j,&count,index);
	
	return 0;
}
