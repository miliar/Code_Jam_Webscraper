#include<bits/stdc++.h>
using namespace std;

#define ull unsigned long long

int check_not_prime(ull num){
	ull i;
	for(i=2;i*i<=num;++i){
		if(num%i==0){
			return 1;		
		}
	}
	return 0;
}

ull find_divisor(ull num){
	ull i;
	for(i=2;i*i<=num;++i){
		//printf("exit\n");
		if(num%i==0){
				//printf("exit\n");
			return i;
		}
	}
	//printf("exit\n");
	return 0;
}

ull modular_pow(ull base, ull exponent)
{
    ull result = 1;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            result = (result * base);
        exponent = exponent >> 1;
        base = (base * base);
    }
    return result;
}

char str[200]; int mark[200];

int main(){
	
	freopen("input.txt", "r" , stdin);
	freopen ("output.txt","w",stdout);
	
	int t,r,i,j,n,k;
	
	scanf("%d",&t);
	
	for(r=1;r<=t;++r){
		scanf("%d %d",&n,&j);
		printf("Case #%d: \n",r);
		ull num=1;
		for(i=1;i<n;++i){
			num=num*2;
		}
		num+=1; int count=0; ull mark[n],div[11];
		while(count!=j){
			if(check_not_prime(num)){
				ull copy=num; int counter=n-1;
				while(copy>0){
					ull digit=copy%2; mark[counter]=digit; --counter; copy=copy/2;
				}
				if(mark[0]==1&&mark[n-1]==1){ 
					for(i=2;i<=10;++i){
						ull new_num=1;
						for(k=0;k<n-1;++k){
							if(mark[k]==1){
								new_num+=modular_pow(i,n-k-1);
							}
						}
						//printf("%ulld\n",new_num);
						div[i]=find_divisor(new_num);
						//if(div==0) printf("%d\n",check_not_prime(new_num));
					}
					int flag=1;
					for(i=2;i<=10;++i){
						if(div[i]==0){
							flag=0;
						}
					}
					if(flag){
						++count;
						for(i=0;i<n;++i) printf("%llu",mark[i]); printf(" ");
						for(i=2;i<=10;++i) printf("%d ",div[i]);
						printf("\n");
					}
				}
			}
			++num;
		}
	}
	
	fclose(stdout);
	return 0;
}
