#include<iostream>
#include<math.h>
#define K 32767
#define left(i) (2*(i)+1)
#define right(i) (2*(i)+2)
//K=2^15-1

#define N 16
#define J 50

int countPrint=0;

long long int power(int k,int n)//k^n
{
	int i;
	long long int ans = 1;
	for (i = 0; i < n; i++)
		ans *= k;
	return ans;
}

long long int interpret(int k, int jamCoin[])//将jamCoin[]解释成k进制
{
	int i;
	long long int ans = 0;
	for (i = 0; i < N - 1; i++)
		if(jamCoin[i]==1)ans += power(k, N - 1 - i);
	ans += 1;
	return ans;
}

long long int isComposite(long long int t)//合数返回一个因子，佛则返回0
{
	long long int i = 2;
	long long int f = sqrt(t)+1;
	for (; i <= f; i++)
	{
		if ((t / i)*i == t)return i;
	}
	return 0;
}
void dfs(int i, int tree[], int deep[], int jamCoin[])
{
	jamCoin[deep[i]] = tree[i];
	if (deep[i] == (N - 2) && countPrint<J)
	{
		int j = 2;
		int count = 0;
		long long int divTable[9];
		for (j = 2; j <= 10; j++)
		{
			long long int intk = interpret(j, jamCoin);
			long long int div = isComposite(intk);
			if (div == 0)break;
			divTable[j - 2] = div;
			count++;
		}
		if (count == 9)//IT MEANS IT ACTUALLY IS A JAMCOIN!!
		{
			countPrint++;
			int k;
			for (k = 0; k < N - 1; k++)
				std::cout << jamCoin[k];
			std::cout << 1<<" ";
			for (k = 0; k < 9; k++)
				std::cout << divTable[k]<<" ";
			std::cout <<std::endl;
		}
	}

	if (i <= (K / 2 - 1))
	{
		dfs(left(i), tree, deep,jamCoin);
		dfs(right(i), tree, deep,jamCoin);
	}
}
int main()
{
	int jamCoin[N-1];
	int i;
	int tree[K];
	int deep[K];
	//initialize
	tree[0] = 1;
	deep[0] = 0;
	for (i = 0; i <=(K / 2 - 1); i++)
	{
		tree[left(i)] = 1;
		deep[left(i)] = deep[i] + 1;
		tree[right(i)] = 0;
		deep[right(i)] = deep[i] + 1;
	}
	freopen("out.txt", "w", stdout);
	std::cout << "Case #1:" <<std::endl;
	dfs(0, tree, deep, jamCoin);
}
