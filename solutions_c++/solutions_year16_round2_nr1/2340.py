#include <cstring>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;
int T,t,l,ll;
char buf[5000];
int let[30];
int num[10];

int main(){
	scanf("%d\n",&T);
	for(t=0;t<T;t++){
		scanf("%s",buf);
		ll=strlen(buf);
		memset(let,0,sizeof(let));
		memset(num,0,sizeof(num));
		for(l=0;l<ll;l++)
			let[buf[l]-'A']++;
		//printf("%d\n",ll);
		num[0]=let[25];let[14]-=num[0];let[17]-=num[0];
		num[2]=let[22];let[14]-=num[2];
		num[4]=let[20];let[5]-=num[4];let[14]-=num[4];let[17]-=num[4];
		num[6]=let[23];let[18]-=num[6];
		num[8]=let[6];
		num[1]=let[14];let[13]-=num[1];
		num[3]=let[17];
		num[5]=let[5];
		num[7]=let[18];let[13]-=num[7];
		num[9]=let[13]/2;
		printf("Case #%d: ",t+1);
		for(int i=0;i<10;i++)
			for(int j=0;j<num[i];j++)
				printf("%c",'0'+i);
		printf("\n");
	}
}
