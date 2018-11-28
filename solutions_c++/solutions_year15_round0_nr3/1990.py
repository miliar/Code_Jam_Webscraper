#include<stdio.h>
#include<string>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;

int a[10000];
char s[10010];
int n;

int mul[4][4]={
	{ 1, 2, 3, 4},
	{ 2,-1, 4,-3},
	{ 3,-4,-1, 2},
	{ 4, 3,-2,-1}
};

int sign(int a){
	return a>0? 1: -1;
}

int cheng(int a,int b){
	int c = sign(a), d = sign(b);
	return mul[abs(a)-1][abs(b)-1] * c * d;
}

int main(){
	freopen("stdin","r",stdin);
	freopen("stdout","w",stdout);
	scanf("%d",&n);
	for (int time=0;time<n;time++)
	{
		int len, rep;
		int can = 0;
		scanf("%d %d",&len, &rep);
		scanf("%s",s);
		for (int j=0;j<len;j++){
			switch(s[j]){
			case 'i': a[j] = 2; break;
			case 'j': a[j] = 3; break;
			case 'k': a[j] = 4; break;
			}
		}
		int idx = len;
		for (int i=1;i<rep;i++)
			for (int j=0;j<len;j++)
				a[idx++] = a[j];
		len = rep * len;
		int res = 1, idxi = -1, idxk = -1;
		for (int i=0;i<len;i++){
			res = cheng(res, a[i]);
			if (res == 2){
				idxi = i;
				break;
			}
		}
		res = 1;
		for (int i=len-1;i>=0;i--){
			res = cheng(a[i], res);
			if (res == 4){
				idxk = i;
				break;
			}
		}
		if (idxi != -1 && idxk != -1 && idxi < idxk){
			res = 1;
			for (int i = idxi +1; i<idxk; i++){
				res = cheng(res, a[i]);
			}
			can = (res==3);
		}
		printf("Case #%d: %s\n", time+1, can? "YES":"NO");
	}
	return 0;
}
