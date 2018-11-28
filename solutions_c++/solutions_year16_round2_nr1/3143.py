#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,i,a[100],num[100];
	char input[2500];
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++){
		scanf("%s",input);
		for(i=0;i<26;i++)
			a[i]=0;
		for(i=0;i<10;i++)
			num[i]=0;

		for(i=0;input[i]!='\0';i++){
			a[input[i]-65]++;
		}

		num[0]=a[25];
		a[4]-=a[25];
		a[17]-=a[25];
		a[14]-=a[25];
		a[25]=0;

		num[2]=a[22];
		a[19]-=a[22];
		a[14]-=a[22];
		a[22]=0;

		num[4]=a[20];
		a[5]-=a[20];
		a[14]-=a[20];
		a[17]-=a[20];
		a[20]=0;

		num[6]=a[23];
		a[18]-=a[23];
		a[8]-=a[23];
		a[23]=0;

		num[8]=a[6];
		a[4]-=a[6];
		a[8]-=a[6];
		a[7]-=a[6];
		a[19]-=a[6];
		a[6]=0;

		num[5]=a[5];
		a[8]-=a[5];
		a[21]-=a[5];
		a[4]-=a[5];
		a[5]=0;

		num[7]=a[21];
		a[18]-=a[21];
		a[4]-=a[21];
		a[4]-=a[21];
		a[13]-=a[21];
		a[21]=0;

		num[3]=a[7];
		a[19]-=a[7];
		a[17]-=a[7];
		a[4]-=a[7];
		a[4]-=a[7];
		a[7]=0;

		num[1]=a[14];
		a[13]-=a[14];
		a[4]-=a[14];
		a[14]=0;

		num[9]=a[8];

		printf("Case #%d: ",cas);
		for(i=0;i<10;i++){
			while(num[i]--)
				printf("%d",i);
			// printf("%d\n",num[i]);
		}
		printf("\n");
	}
	return 0;
}