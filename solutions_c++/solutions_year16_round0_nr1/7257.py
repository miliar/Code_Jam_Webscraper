#include<cstdio>

using namespace std;

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int count = (1 << 10) - 1,t,n;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%d",&n);
		printf("Case #%d: ",i+1);
		if (n == 0)
			printf("INSOMNIA\n");
		else {
			int check = 0, temp, multi = 1;
			while(count != check){
				temp = multi * n;
				while(temp > 9){
					check |= 1 << (temp%10);
					temp /= 10;
				}
				check |= 1 << (temp%10);
			//	printf("%d\n",check);
				multi++;
			}
			printf("%d\n",(multi-1)*n);
		}
	}
}
