#include <stdio.h>
#include <math.h>
#include <iostream>
double arr[410];

int check(long long q)
{
	if(q == 0) return 1;
	if(q%2 == 0) return check(q/2);
	else return 0;
}

int main()
{
    //freopen("ab.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int test,i,cse,no;
	long long p,q,sol;
	scanf("%d",&test);
	for(i=0;i<41;i++) {
		arr[i] = (double)((double)1.0/(double)pow(2,i));
	}
	for(no=1;no<=test;no++) {
		cse = 1;
		scanf("%lld/%lld",&p,&q);
		long long num1, num2;
		num1 = p;
		num2 = q;
		while(num1!=num2)
    	{
        if(num1>num2)
            num1-=num2;
        else
            num2-=num1;
    	}
    	long long m = num1;
		p = p / m;
		q = q / m;
		if((q != 1) && (q & (q - 1))) {
			printf("Case #%d: impossible\n", no);
            cse += 1;
            continue;
		}
		double ans = (double)p/(double)q;
		for(i=0;i<41;i++){
			if(arr[i] <= ans) {
				sol = i;
				break;
			}
		}
		printf("Case #%d: %lld\n", no, sol);
		cse += 1;
	}
	return 0;
}
