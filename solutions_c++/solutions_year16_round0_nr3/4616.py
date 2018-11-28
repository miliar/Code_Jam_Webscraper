#include<bits/stdc++.h>
using namespace std;
#define Int long long
Int Power[11][33];
/* a function to compute (ab)%c */
/* This function calculates (ab)%c */
int modulo(int a,int b,int c){
    long long x=1,y=a; // long long is taken to avoid overflow of intermediate results
    while(b > 0){
        if(b%2 == 1){
            x=(x*y)%c;
        }
        y = (y*y)%c; // squaring the base
        b /= 2;
    }
    return x%c;
}
/* this function calculates (a*b)%c taking into account that a*b might overflow */
long long mulmod(long long a,long long b,long long c){
    long long x = 0,y=a%c;
    while(b > 0){
        if(b%2 == 1){
            x = (x+y)%c;
        }
        y = (y*2)%c;
        b /= 2;
    }
    return x%c;
}
/* Miller-Rabin primality test, iteration signifies the accuracy of the test */
bool Miller(long long p,int iteration){
    if(p<2){
        return false;
    }
    if(p!=2 && p%2==0){
        return false;
    }
    long long s=p-1;
    while(s%2==0){
        s/=2;
    }
    for(int i=0;i<iteration;i++){
        long long a=rand()%(p-1)+1,temp=s;
        long long mod=modulo(a,temp,p);
        while(temp!=p-1 && mod!=1 && mod!=p-1){
            mod=mulmod(mod,mod,p);
            temp *= 2;
        }
        if(mod!=p-1 && temp%2==0){
            return false;
        }
    }
    return true;
}
void Print(Int num,Int arr[]){
	Int sq,i,j;
	printf("%lld ",arr[10]);
	for(i=2;i<=10;i++){
		sq = sqrt(arr[i]);
		for(j=2;j<=sq;j++){
			if(arr[i]%j==0){
				printf("%lld ",j);break;
			}
		}
	}
	printf("\n");
}
Int convertToBase(Int num,Int base){

	Int ans=0,c=0;
	while(num>0){
		if(num&1)
			ans += Power[base][c];
		c++;num>>=1;
	}
	return ans;
}
int main(){
	Int n,t,T,i,j,J,limit,num,arr[11],count;
	for(i=2;i<=10;i++){
		Power[i][0] = 1;
		for(j=1,t=1;j<=32;j++){
			Power[i][j] = Power[i][j-1]*i;
		}
	}
	scanf("%lld",&T);
	for(t=1;t<=T;t++){
		scanf("%lld %lld",&n ,&J);
		printf("Case #%lld:\n",t);
		limit = (1<<(n-2));
		for(i = 0,count=0;i<limit && count<J;i++){
			num = (i<<1) | 1;
			num = (num) | (1<<(n-1));
			if(!Miller(num,20)){
				//cout<<"NUMBER IS: "<<num<<endl;
				arr[2] = num;j=3;
				for(;j<=10;j++){
					arr[j] = convertToBase(num,j);
					if(Miller(arr[j],20))break;
				}
				if(j>10){
					Print(num,arr);
					count++;
				}
			}
		}
	}
	return 0;
}