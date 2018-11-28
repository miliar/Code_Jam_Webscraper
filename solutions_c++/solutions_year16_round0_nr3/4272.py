#include <bits/stdc++.h>
using namespace std;

long long int seive[100000000];
long long int seive2[100000000];
long long int val;

long long int power(long long int x, long long int y){
	long long int ans = 1, i = 1;
	while(i <= y){
		ans = ans * x;
		i++;
	}
	return ans;
}

long long int checkPrime(long long int x){
	if(x>1000000){
		int i = 0;
		int flag=0;
		for(i=2;i<val;i++){
			if(x%seive2[i]==0){
				flag=1;
				return 0;
			}
		}
		if(i==val)
			return 1;
	}
	else
	{
		if(seive[x]==0)
			return 1;
		else
			return 0;
	}
}

long long int findDivisor(long long int x){
	long long int i = 2;
	int count=1;
	while(i < x){
		if(x % i == 0){
			count++;
		}	
		if(count==2)
			return i;
		i++;
	}
}

int main(){
	int chu;
	int p;
	int n, j, k, i, count, JP, l;
	long long int m;
	long long int converted;
	long long int arr[10];
	int flag;
	int arr2[16];
	scanf("%d", &chu);
	while(chu--){
		scanf("%d%d", &n, &JP);
		int ans[n];
		int s = 0;
		for(i=2;i<1000000;i++)
		{
			if(seive[i]==0)
			{
				for(j=i+i;j<1000000;j=j+i)
				{
					if (seive[j]==0)
					{
						seive[j]=i;
						s++;
					}
				}
			}
		}
		k=0;
		for(i=0;i<1000000;i++)
		{
			if(seive[i]==0){
				seive2[k]=i;
				k++;
			}
		}
		val=k;

		int x = 1<<(n-1);
		int y = 1<<n;
		int count2 = 0;
		printf("Case #1:\n");

		for(l=x;l<=y;l++) {
			if(seive[l]!=0 && l%2 != 0) {
				count = n - 1;
				m  = l;
				for(;m >= 2;){
					ans[count] = m%2;
					count--;
					m = m/2;
				}

				ans[0] = m;

				i = 0;
				flag = 1;
				for(k = 2; k <= 10; k++){
					converted = 0;
					i = 0;
					while(i < n){
						converted = converted + ans[n - i - 1]*power(k, i);
						i++;
					}
					
					i = 0;

					for(;i < n;){
						arr2[i] = ans[i];
						i++;
					}

					if(checkPrime(converted) == 1){
						flag = 0;
						break;
					}
					
					arr[k] = converted;
				}

				if(flag == 1){
					int xyz = 2;

					i = 0;
					for(;i < n;){
						printf("%d", ans[i]);
						i++;
					}
					printf(" ");
					for(;xyz < 11;){
						printf("%lld ", findDivisor(arr[xyz]));
						xyz++;
					}
					printf("\n");
					count2++;
				}

				if(count2 == JP)
					break;
				}
				
		}

	}
	
	return 0;
}