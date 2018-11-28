#include<cstdio>
#include<iostream>
#include<cmath>
#include<map>
#include<vector>
#include<algorithm>

using namespace std;
#define Base 10
#define Cap 128
typedef long long hugeint;

struct bignum
{
    int Len;
    int Data[Cap];
    bignum() : Len(0) {}
    bignum(const bignum& V) : Len(V.Len){ memcpy(Data, V.Data, Len * sizeof *Data);}
    bignum(int V) : Len(0) { for (; V > 0; V /= Base) Data[Len++] = V % Base; }
    bignum& operator=(const bignum& V) { Len = V.Len;
                  memcpy(Data, V.Data, Len * sizeof *Data); return *this; }
    int& operator[](int Index) { return Data[Index]; }
    int operator[](int Index) const { return Data[Index]; }
};


int compare(const bignum& A, const bignum& B)
{
    int I;
    if (A.Len != B.Len) return A.Len > B.Len ? 1 : -1;
    for (I = A.Len - 1; I >= 0 && A[I] == B[I]; I--);
    if (I < 0) return 0;
    return A[I] > B[I] ? 1 : -1;
}

bignum operator+(const bignum& A, const bignum& B)
{
    bignum R;
    int I;
    int Carry = 0;
    for (I = 0; I < A.Len || I < B.Len || Carry > 0; I++)
    {
       if (I < A.Len) Carry += A[I];
       if (I < B.Len) Carry += B[I];
       R[I] = Carry % Base;
       Carry /= Base;
    }
    R.Len = I;
    return R;
}

bignum operator-(const bignum& A, const bignum& B)
{
    bignum R;
    int Carry = 0;
    R.Len = A.Len;
    int I;
    for (I = 0; I < R.Len; I++)
    {
       R[I] = A[I] - Carry;
       if (I < B.Len) R[I] -= B[I];
       if (R[I] < 0) Carry = 1, R[I] += Base;
       else Carry = 0;
    }
    while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--;
    return R;
}

bignum operator*(const bignum& A, const int B)
{
    int I;
    if (B == 0) return 0;
    bignum R;
    hugeint Carry = 0;
    for (I = 0; I < A.Len || Carry > 0; I++)
    {
       if (I < A.Len) Carry += hugeint(A[I]) * B;
       R[I] = Carry % Base;
       Carry /= Base;
    }
    R.Len = I;
    return R;
}

bignum operator*(const bignum& A, const bignum& B)
{
    int I;
    if (B.Len == 0) return 0;
    bignum R;
    for (I = 0; I < A.Len; I++)
    {
       hugeint Carry = 0;
       for (int J = 0; J < B.Len || Carry > 0; J++)
       {
          if (J < B.Len) Carry += hugeint(A[I]) * B[J];
          if (I + J < R.Len) Carry += R[I + J];
          if (I + J >= R.Len) R[R.Len++] = Carry % Base;
          else R[I + J] = Carry % Base;
          Carry /= Base;
       }
    }
    return R;
}

bignum operator/(const bignum& A, const int B)
{
    bignum R;
    int I;
    hugeint C = 0;
    for (I = A.Len - 1; I >= 0; I--)
    {
       C = C * Base + A[I];
       R[I] = C / B;
       C %= B;
    }
    R.Len = A.Len;
    while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--;
    return R;
}

bignum operator/(const bignum& A, const bignum& B)
{
    int I;
    bignum R, Carry = 0;
    int Left, Right, Mid;
    for (I = A.Len - 1; I >= 0; I--)
    {
       Carry = Carry * Base + A[I];
       Left = 0;
       Right = Base - 1;
       while (Left < Right)
       {
          Mid = (Left + Right + 1) / 2;
          if (compare(B * Mid, Carry) <= 0) Left = Mid;
          else Right = Mid - 1;
       }
       R[I] = Left;
       Carry = Carry - B * Left;
    }
    R.Len = A.Len;
    while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--;
    return R;
}

bool operator==(const bignum& A, const bignum& B)
{
    int i;
    if(A.Len != B.Len)return 0;
    for(i=0;i<A.Len;i++)
    if(A.Data[i]!=B.Data[i])return 0;
    return 1;
}

bignum operator%(const bignum& A, const bignum& B)
{
    int I;
    bignum R, Carry = 0;
    int Left, Right, Mid;
    for (I = A.Len - 1; I >= 0; I--)
    {
       Carry = Carry * Base + A[I];
       Left = 0;
       Right = Base - 1;
       while (Left < Right)
       {
          Mid = (Left + Right + 1) / 2;
          if (compare(B * Mid, Carry) <= 0) Left = Mid;
          else Right = Mid - 1;
       }
       R[I] = Left;
       Carry = Carry - B * Left;
    }
    R.Len = A.Len;
    while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--;
    return Carry;
}

bignum pow(bignum a,int n)
{
    bignum tmp = a;
    while(--n)
       tmp = tmp * a;
    return tmp; 
}

istream& operator>>(istream& In, bignum& V)
{
    char Ch;
    for (V = 0; In >> Ch;)
    {
       V = V * 10 + (Ch - '0');
       if (cin.peek() <= ' ') break;
    }
    return In;
}
int ans[1000000];
int aanslen;
ostream& operator<<(ostream& Out, const bignum& V)
{
    int I;
    Out << (V.Len == 0 ? 0 : V[V.Len - 1]);
    for (I = V.Len - 2; I >= 0; I--)
    for (int J = Base / 10; J > 0; J /= 10)
        Out << V[I] / J % 10;
    return Out;
}

bool check(bignum V)
{
	int s[128], len = 0;
    int I;
    s[len++] = (V.Len == 0 ? 0 : V[V.Len - 1]);
    for (I = V.Len - 2; I >= 0; I--)
    for (int J = Base / 10; J > 0; J /= 10)
    {
        s[len++] = V[I] / J % 10;
	}

    int i;
	for(i = 0; i < len-1-i; i ++)
	{
		if(s[i] != s[len-1-i])return false;
	}
	//cout << num << endl;
	return true;
}

bignum base[80000], weight[128];
bignum list[80000], tmp;
int bsize, size;
int wsize[80000];

void init()
{
	base[0] = 0; wsize[0] = 0;
	base[1] = 0; wsize[1] = 1;
	base[2] = 1; wsize[2] = 1;
	base[3] = 2; wsize[3] = 1;
	base[4] = 3; wsize[4] = 1;
	bsize = 5;
	
	list[0] = 0;
	list[1] = 1;
	list[2] = 4;
	list[3] = 9;
	size = 4;
	
	int i, j;
	weight[0] = 1;
	for(i = 1; i <= 100; i ++)
	{
		weight[i] = weight[i-1]*10;
	}
	
	for(i = 2; i <= 50; i ++)
	{
		for(j = 0; j < bsize; j ++)
		{
			if(wsize[j] >= i-1)break;
			if((i-wsize[j])%2 != 0)continue;
			int halfsize = (i-wsize[j])/2;
			tmp = weight[i-1];
			tmp = tmp + 1;
			tmp = tmp + base[j]*weight[halfsize];
			//cout << halfsize << " " << wsize[j] << endl;
			base[bsize] = tmp;
			list[size] = tmp*tmp;
			//cout << list[size] << ' ' << tmp << endl;
			if(check(list[size]))
			{
				wsize[bsize] = i;
				bsize ++;
				size ++;
			}
		}
		
		for(j = 0; j < bsize; j ++)
		{
			if(wsize[j] >= i-1)break;
			if((i-wsize[j])%2 != 0)continue;
			int halfsize = (i-wsize[j])/2;
			tmp = weight[i-1]*2;
			tmp = tmp + 2;
			tmp = tmp + base[j]*weight[halfsize];
			//cout << halfsize << " " << wsize[j] << endl;
			base[bsize] = tmp;
			list[size] = tmp*tmp;
			//cout << list[size] << ' ' << tmp << endl;
			if(check(list[size]))
			{
				wsize[bsize] = i;
				bsize ++;
				size ++;
			}
		}
		
		for(j = 1; j < size; j ++)
		{
			if(compare(list[j], list[j-1]) <= 0)
			{
				cout << j << " " << "fuck!" << endl;
			}
		}
		cout << i << " " << bsize << endl;
	}
	list[size++] = weight[100]*100;
/*
	for(i = 0; i < size; i ++)
	{
		cout << list[i] << ' ';
	}*/
	
}

int GetIndex(bignum num, bool Upper)
{
	int left, right, mid;
	int Ret = size;
	left = 0; right = size-1;
	while(left <= right)
	{
		mid = (left + right)>>1;
		if(compare(num, list[mid]) == 1)
		{
			left = mid+1;
		}
		if(compare(num, list[mid]) <= 0)
		{
			Ret <?= mid-1;
			right = mid-1;
		}
	}
	
	if(Upper)
	{
		if(compare(num, list[Ret+1]) == 0)Ret ++;
	}
	
	return Ret;
}

int main()
{
	init();
	
	printf("Input File Name ?");
	char FileName[128];
	scanf("%s", FileName);
	freopen(FileName, "r", stdin);
	freopen("C_big.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	int Case;
	for(Case = 1;  Case <= T; Case ++)
	{
		bignum A, B;
		cin >> A >> B;
		//cout << GetIndex(B, true) << " " << GetIndex(A, false) << endl;
		int Ans = GetIndex(B, true) - GetIndex(A, false);
		printf("Case #%d: %d\n", Case, Ans);
	}
	
	return 0;
}
