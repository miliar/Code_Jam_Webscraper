#include<bits/stdc++.h>
using namespace std;

typedef long long int LL;

#define scll(Q)   	scanf("%lld",&Q);
#define sci(Q)   	scanf("%d",&Q);
#define sc(Q)		scanf("%s",&Q);
#define prll(Q)   	printf("%lld\n",Q);
#define pri(Q)    	printf("%d\n",Q);
#define pr(Q)   	printf("%s\n",Q);


int hash[10]={0};


int isnt_complete(int hash[]){
	for(int i=0;i<10;i++){
		if(hash[i]==0)	return 1;
	}
	return 0;
}

void parse(LL n){
	while(n){
		hash[n%10]=1;
		n=n/10;
	}
}



int main()
{

	int t,i;	
	long long n,temp;
	sci(t);
	
	for(i=1;i<=t;i++){
		memset(hash,0,sizeof(hash));
		int j=1;
		scll(n);
		
		if(n==0){
			cout<<"Case #"<<i<<": "<<"INSOMNIA\n";
			continue;
		}
		
		while(isnt_complete(hash)){
			temp=n*j;
			parse(temp);
			j++;
		/*	cout<<temp<<"  ";
			for(int i=0;i<10;i++)	cout<<hash[i];
			cout<<endl;*/
		}
		
		cout<<"Case #"<<i<<": "<<temp<<endl;
		
	}
	
	return 0;
}


