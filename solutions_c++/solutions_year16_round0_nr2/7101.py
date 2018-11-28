#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<cmath>
#define LL long long
using namespace std;
int t,n,m;
char s[110];
int main(){
	scanf("%d",&t);
	for (int I=1;I<=t;I++){
		scanf("%s",s);
		n=strlen(s);
		m=0;
		for (int i=n-1;i>=0;i--)
			if (s[i]=='-'){
				m++;
    			for (int j=0;j<=i;j++) s[j]='+'+'-'-s[j];
    		}
    	printf("Case #%d: %d\n",I,m);
    }
	return 0;
}

