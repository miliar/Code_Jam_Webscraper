#include<bits/stdc++.h>

#define sc(x) scanf("%li", &x);
#define CONST 99999999

int check[10]={0,0,0,0,0,0,0,0,0,0};

int verify(){
	for(int i=0;i<10;i++){
		if(check[i]==0)
			return -1;
	}
	for(int i=0;i<10;i++){
		check[i]=0;
	}	
	return 1;
}

int mod(int v){
	int ch1;
	for(int ch=v;ch!=0;){
		ch1=ch%10;
		ch=ch/10;
		if(check[ch1]==0)
			check[ch1]=1;
	}
	return verify();
}


int counting_sheep(){
	long d;
	sc(d);
	for(int i=1;i<CONST;i++){
		if(mod(i*d)==1)
			return (i*d);
	}
	return -1;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d",&t);
	long v1;
	for(int i=1;i<=t;i++){
		v1=counting_sheep();
		if(v1==-1){
			printf("Case #%d: ", i);
			printf("INSOMNIA\n");
		}
		else{
			printf("Case #%d: ", i);
			printf("%li\n", v1);
		}
	}
	return 0;
}