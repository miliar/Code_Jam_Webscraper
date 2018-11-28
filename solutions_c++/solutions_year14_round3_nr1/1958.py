#include<cstdio>
#include<cmath>
#include<algorithm>

using namespace std;

int get(long no)
{
	int temp = 1;
	int i;
	for(i=0;temp<no;i++, temp=temp*2);

	if(no==temp)
		return i;
	return i-1;
}

int get_abs(long no)
{
	int temp = 1;
	int i;
	for(i=0;temp<no;i++, temp=temp*2);

	if(no==temp)
		return i;
	return -1;
}
int main(void)
{
	int T;
	//printf("test  = %d\n", get(8));
	scanf("%d", &T);
	for(int i=0;i<T;i++){
		printf("Case #%d: ", i+1);

		long P, Q;
		scanf("%ld/%ld", &P, &Q);
		if(P>Q || P==0){
			printf("impossible\n");
			continue;
		}
		//printf("P=%ld, Q=%ld\n", P, Q);
		for(int j=2;j<=P;j++){
			if(P%j==0 && Q%j == 0){
				P = P/j;
				Q = Q/j;
				j--;
			}
		}
		//printf("P=%ld, Q=%ld\n", P, Q);
		int q = get(Q);
		if(q==get_abs(Q))
			printf("%d\n", q-get(P));
		else
			printf("impossible\n");
	}
}
