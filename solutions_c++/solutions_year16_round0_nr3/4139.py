#include<iostream>
#include<cmath>
#include<cstdlib>

using namespace std;

long long power(int num, int p)
{
    long long res = 1;
    int i;
    for(i = 0; i < p; i++)
    {
	res *= num;
    }
    return res;
}

long long to_base(long long num, int base)
{
    long long res = 0, b;
    int p = 0;

    while(num != 0)
    {
	b = num % 10;
	num /= 10;
	res += power(base, p) * b;
	p++;
    }
    return res;
}

long long test_prime(long long num)
{
    long long i;
    //cout<<"In test_prime "<<num<<endl;
    if(num <= 3)
	return -1;
    if((num % 2) == 0)
	return 2;
    if((num % 3) == 0)
	return 3;
    for(i = 5; i * i <= num; i = i + 6)
    {
	if((num % i) == 0)
	    return i;
	if((num % (i + 2)) == 0)
	    return i + 2;
    }
    return -1;
}

void to_bin(long long num, char *res)
{
    int i, j, temp, len = 0;
    //cout<<num<<endl;
    while(num != 0)
    {
	if((num % 2) == 1)
	    res[len++] = '1';
	else
	    res[len++] = '0';
	num /= 2;
    }
    res[len] = '\0';
    for(i = 0, j = len - 1; i < j; i++, j--)
    {
	temp = res[i];
	res[i] = res[j];
	res[j] = temp;
    }
}


int main()
{
    int T, N, J;
    int i, k, num_coins;
    long long j, s, num;
    long long div[9];
    char res[256];

    cin>>T;
    for(i = 0; i < T; i++)
    {
	cout<<"Case #"<<i+1<<": "<<endl;
	cin>>N>>J;
	num_coins = 0;
	for(j = power(2, N - 1) + 1; j <= power(2, N) - 1 && num_coins < J; j++)
	{
	    //cout<<j<<endl;
	    if(!((j >> (N - 1)) & 1) || !(j & 1))
		continue;
	    //cout<<j<<endl;
	    to_bin(j, res);
	    s = atol(res);
	    //cout<<s<<endl;
	    for(k = 2; k <= 10; k++)
	    {
		num = to_base(s, k);
		if((div[k - 2] = test_prime(num)) == -1)
		    break;
	    }
	    if(k == 11)
	    {
		//to_bin(j, res);
		cout<<res<<" ";
		for(k = 0; k < 9; k++)
		    cout<<div[k]<<" ";
		cout<<endl;
		num_coins++;
	    }
	}
    }
    return 1;
}
