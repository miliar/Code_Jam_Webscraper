#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int T,alph[30],num[15],l;
char str[2005];

int main(){
	freopen("digit.in","r",stdin);
	freopen("digit.out","w",stdout);
	
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		scanf(" %s",str);
		memset(alph,0,sizeof(alph));
		memset(num,0,sizeof(num));
		l=strlen(str);
		for(int j=0;j<l;j++){
			alph[str[j]-64]++;
		}
		num[0]+=alph[26];
		alph[5]-=alph[26];
		alph[18]-=alph[26];
		alph[15]-=alph[26];
		alph[26]=0;
		num[2]+=alph[23];
		alph[15]-=alph[23];
		alph[20]-=alph[23];
		alph[23]=0;
		num[4]+=alph[21];
		alph[6]-=alph[21];
		alph[15]-=alph[21];
		alph[18]-=alph[21];
		alph[21]=0;
		num[6]+=alph[24];
		alph[19]-=alph[24];
		alph[9]-=alph[24];
		alph[24]=0;
		num[8]+=alph[7];
		alph[5]-=alph[7];
		alph[9]-=alph[7];
		alph[8]-=alph[7];
		alph[20]-=alph[7];
		alph[7]=0;
		num[1]+=alph[15];
		num[3]+=alph[8];
		num[5]+=alph[6];
		alph[9]-=alph[6];
		alph[22]-=alph[6];
		alph[5]-=alph[6];
		alph[6]=0;
		num[7]+=alph[19];
		num[9]+=alph[9];
		printf("Case #%d: ",i);
		for(int j=0;j<10;j++){
			for(int k=1;k<=num[j];k++) printf("%d",j);
		}
		printf("\n");
	}
	return 0;
}
