#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>
#include<algorithm>
#include<cstring>

using namespace std;
long long fact[11];

long long findnum(long long num, int base)
{
    long long ans = 0;
    int pw = 0;
    while(num)
    {
        if(num&1)
        {
            double tmp = pow(base, pw);
            ans+=tmp;
        }

        pw++;
        num = num>>1;
       // cout<<ans<<endl;
    }

    return ans;
}

bool isprime(long long num, int indx)
{
    for(long long i=2; i*i<=num; i++)
        if((num%i)==0)
        {
            fact[indx] = i;
            return 0;
        }

    return 1;
}

/*long long tobin(long long num)
{
    long long ans = 0;
    int pw = 0;
    while(num)
    {

        num = num>>1;
    }

    return ans;
}*/

void tobin(long long num)
{
	int rem;

	if(num <= 1)
    {
		cout << num;
		return;
	}

	rem = num%2;
	tobin(num >> 1);
	cout << rem;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-output0.out", "w", stdout);
    // small input n=16, j=50;
    long long n = (1<<15);
    //long long n = (1<<3) + 1;
    printf("Case #1:\n");

    int J=0;
    while(J<50)
    {
        bool cn = 0;
        n++;
        if((n&1)==0)
            continue;

        for(int i=2; i<=10; i++)
            if(isprime(findnum(n, i), i))
            {
                cn = 1;
                break;
            }

        if(cn)
            continue;

        tobin(n);
        cout<<" ";
        for(int i=2; i<=10; i++)
            cout<<fact[i]<<" ";
        J++;
        cout<<endl;
    }
    return 0;
}
