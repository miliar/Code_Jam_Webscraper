#include <cstdio>
#include <cstring>
int arr[1001], N;
char str[1005];
int main()
{
	int i, TN, ca=0;
	scanf("%d", &TN);
	while(TN--){
		scanf(" %d %s", &N, str);
		
		for(i=0;i<=N;i++){
			arr[i]=str[i]-'0';
		}
		int stand=0, inv=0;
		for(i=0;i<=N;i++){
			if(i>stand){
				inv+=(i-stand);
				stand+=(i-stand);
			}
			stand+=arr[i];
		}
		printf("Case #%d: %d\n", ++ca, inv);

	}

	return 0;
}