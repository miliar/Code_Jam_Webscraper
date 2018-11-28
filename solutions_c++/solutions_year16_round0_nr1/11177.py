#include<bits/stdc++.h>


int digit(int dig[],int a){
	int i=0,pot=10,n=a;
//	printf("%d\n",n);
	while(n>0){
		dig[i]=n%pot;
		n=n/10;
//		printf("%d\n",n);
		i++;
	}
	return i;
}


int solve(long int n){
	
	int i,dig[100],num[10],d,c=0,m=1;
//	bool s=true;
	
	for(i=0;i<10;i++){
		num[i]=1;
	}
	
	while(1){
		d=digit(dig,n*m);
		for(i=0;i<d;i++){
			if(num[dig[i]]){
				num[dig[i]]=0;
				c++;
			}
		}
		m++;
		if(c==10){
//			for(i=0;i<10;i++){
//				printf("%d\n",num[i]);
//			}
			return n*(m-1);
		}
	}
}



int main()
{
	int t,i;
	long int n,num;
//	freopen ("pru.txt","r",stdin);
//	freopen ("input_C_S_L.in","r",stdin);
//	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(i=0;i<t;i++){
		scanf("%ld",&n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n",i+1);
		}else{
			num=solve(n);
			printf("Case #%d: %ld\n",i+1,num);
		}
	}
	return 0;
}

