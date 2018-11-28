#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

__int64 A,B;
int digA[17],digB[17];

void num2dig(__int64 num,int dig[17])
{
	for (int i=0;num;++i)
	{
		dig[i] = num%10;
		num /= 10;
	}
}

void init()
{
	memset(digA,0,sizeof(digA));
	memset(digB,0,sizeof(digB));
	num2dig(A,digA);
	num2dig(B,digB);
}

bool palindrome(__int64 num)
{
	int dig[17];
	memset(dig,0,sizeof(dig));
	num2dig(num,dig);
	int i = 17;
	while(dig[--i] == 0);
	int j = 0;
	while(i>j)
	{
		if (dig[i] == dig[j]){
			--i;++j;
		}else{
			return false;
		}
	}
	return true;
}

int gao(int num,int id,int len,bool lowBound,bool upBound)
{
	if (len >= id+1 || id == -1){
		int cknum = num;
		int tmp = num;
		if (len == id + 2) tmp/=10;
		while(tmp)
		{
			cknum = cknum * 10 + tmp%10;
			tmp/=10;
		}
		if (cknum > B || cknum < A) return 0;
		if (palindrome((__int64)cknum * (__int64)cknum)){
			return 1;
		}else{
			return 0;
		}
	}
	int low = lowBound ? digA[id]:0;
	int up = upBound ? digB[id]:9;
	int ret = 0;
	for (int i=low;i<=up;++i)
	{
		ret += gao(num*10 + i,id-1,i==0?len:len+1,i==low,i==up);
	}
	return ret;
}

int main()
{
	int T;
	scanf("%d",&T);
	for (int caseno = 1;caseno<=T;++caseno)
	{
		scanf("%I64d%I64d",&A,&B);
		A = ceil(sqrt(A));
		B = floor(sqrt(B));
		init();
		int ans = gao(0,16,0,1,1);
		printf("Case #%d: %d\n",caseno,ans);
	}
	return 0;
}