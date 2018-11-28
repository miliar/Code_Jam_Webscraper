#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>

#define MAX 100000

using namespace std;

void compute(int num)
{
	int cnt,rem,mul;
	bool exist[10];
	long long int temp,val;
	
	memset(exist, false, sizeof(exist));
	
	cnt = mul = 0; 
	val = num;

	while (cnt < 10 && mul < MAX) {
		temp = val;
		while (temp > 0) {
			rem = temp % 10;
			temp /= 10;
			if (!exist[rem]) {
				exist[rem] = true;
				cnt++;
			}
		}
		val += num;
		mul++;
	}

	if(mul == MAX) {
		printf("INSOMNIA\n");
		return;
	}
	printf("%lld\n",val-num);
		
}

int main()
{
	int t,num;

	freopen("input2.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);

	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%d", &num);
		printf("Case #%d: ",i+1);
		if (num != 0)
			compute(num);
		else
			printf("INSOMNIA\n");

	}
	return 0;
}
