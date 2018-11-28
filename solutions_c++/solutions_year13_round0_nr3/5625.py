#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<string>
using namespace std;
int nextpalin(char a[100])
{
	int length = strlen(a);
	int orgno = atoi(a);
	for(int i=0,j=length - 1;i<j;i++,j--)
	{
		a[j] = a[i];
	}
	int palno = atoi(a);
	if(palno > orgno)
		return palno;
	//	cout << palno << endl;
	else
	{
		int j = 0,k = 1,flag = 1;
		while(j < length/2)
		{
			j++;
			k *= 10;
		}

		if(a[length/2] != '9')
			flag = 0;
		//cout << flag << endl;
		if(length % 2 != 0)
			palno += k;
		else
			palno += (k + k/10);
		sprintf(a,"%d",palno);
		if(flag)
		{
			for(int i=0,j=length - 1;i<j;i++,j--)
			{
				a[j] = a[i];
			}
		}
		palno = atoi(a);
		return palno;
		cout << palno << endl;
	}
}
void reverse(char s[])
{
	int length = strlen(s) ;
	int c, i, j;

	for (i = 0, j = length - 1; i < j; i++, j--)
	{
		c = s[i];
		s[i] = s[j];
		s[j] = c;
	}
}
int main(){
	int tc;
	scanf("%d",&tc);
	int l=1;
	while(tc--){
		int a,b;
		scanf("%d %d",&a,&b);
		int k=a-1;
		int m;
		int count=0;
		int sq;
		float per;
		char rev[100];
		char rev1[100];
		while(1){
		char a1[100];
			if(k > b){
				break;
			}
			sprintf(a1,"%d",k);
			m=nextpalin(a1);
			if(m > b){
				break;
			}
			per=sqrt(m);
			if(per==int(per)){
			sq=per;
			sprintf(rev,"%d",sq);
			strcpy(rev1,rev);
			reverse(rev);
			if(strcmp(rev,rev1)==0){
			//	printf("%d\n",m);
				count++;
			}
			}
			k=m;
		}
		printf("Case #%d: %d\n",l,count);
		l++;
	}
	return 0;
}




