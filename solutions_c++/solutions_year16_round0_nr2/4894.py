#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<map>
#include<string>
#include<iostream>
#include<stack>
#include<set>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

#define EPS (1e-7)
#define PI (acos(-1.0))
#define MAXI(a,b) ((a)>(b)?(a):(b))
#define MINI(a,b) ((a)<(b)?(a):(b))
#define mxx 1005
#define SZOF sizeof
#define SZ size
#define mem(a,b) memset((a),(b),sizeof(a))
#define clr(a) mem(a,0)
typedef long long INT;

char str[105];

void swap(int len){
	char c;
	for(int i=0;i<len/2;i++){
		c = str[i];
		str[i]=str[len-i-1];
		str[len-1-i] = c;
	}
	for(int i=0;i<len;i++){
		if(str[i]=='+'){str[i]='-';}
		else{str[i]='+';}
	}
}

int main(){
	
	int i,j,tst,cas=1,n,len,pres_len,cnt;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	scanf("%d",&tst);
	while(tst--){
		scanf("%s",str);
		len=strlen(str);
		pres_len=len;
		cnt=0;

		while(pres_len){
			while(str[pres_len-1]=='+' && pres_len>0){pres_len--;}
			if(pres_len==0){break;}
			i=0;
			while(str[i]=='+' && i < pres_len){
				str[i]='-';
				i++;
			}
			if(i!=0){cnt++;}
			swap(pres_len);
			cnt++;
		}
		printf("Case #%d: %d\n",cas++,cnt);
	}
	
	

	//system("pause");
	return 0;
}

//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);