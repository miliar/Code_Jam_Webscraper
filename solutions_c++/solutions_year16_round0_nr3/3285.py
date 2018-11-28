#include<bits/stdc++.h>

using namespace std;

vector<int> primes;

long long int convert(long long int number, int base)
{
	long long int val=0;
	int i=0;
	while(i<16)
	{
		val+=(number%10)*(long long int)pow(base,i);
		number/=10;
		i++;
	}
	return val;
}

long long int modulo (long long int a, long long int b, long long int c){
    long long int result = 1;

    while (b){
        if (b&1){
          result *= a;
          result %= c;
        }
        b >>=1 ;
        a *= a;
        a %= c;
    }

    return result;
}

long long int isPrime(long long int n){
    int i;
    long long int x;

    if (n==2)
        return 1;

    for (i=0;i<10;i++){
        x = rand()%n;
        if (x==0||x==1)
            x++;
        if (modulo(x,n-1,n)!=1)
            return 0;
    }

    return 1;
}

void SieveOfEratosthenes(int n)
{
    bool prime[n+1];
    memset(prime, true, sizeof(prime));
 
    for (int p=2; p*p<=n; p++)
    {
        if (prime[p] == true)
        {
            for (int i=p*2; i<=n; i += p)
                prime[i] = false;
        }
    }
 
    for (int p=2; p<=n; p++)
       if (prime[p])
          primes.push_back(p);
}

long long int factor(long long int n)
{
	long long int ans=-1;
	for(int i=0;i<10000;i++)
	{
		if(primes[i]<=(int)sqrt(n))
		{
			if(n%primes[i]==0)
			{
				ans=primes[i];
				break;
			}
		}
		else
			break;
	}
	return ans;
}

long long int nextval(long long int n)
{
	stack<int> val;
	while(n%10!=0)
	{
		val.push(n%10);
		n/=10;
	}
	n++;
	while(!val.empty())
	{
		n*=10;
		val.pop();
	}
	return n+1;
}

int main()
{
	long long int number=1000000000000001;
	long long int valadd=0;
	int count=0;
	SieveOfEratosthenes(1000000);
	cout<<"Case #1:"<<endl;
	while(valadd<=11111111111111 && count<50)
	{
		long long int currval=number+(valadd*10);
		long long int factorval[11]={-1};
		bool flag=false;
		for(int i=2;i<=10;i++)
		{
			long long int convval=convert(currval,i);
			if(isPrime(convval)==1)
			{
				flag=true;
				break;
			}
			long long int factorof=factor(convval);
			if(factorof==-1)
			{
				flag=true;
				break;
			}
			factorval[i]=factorof;
		}
		if(!flag)
		{
			cout<<currval<<" ";
			for(int i=2;i<=10;i++)
				cout<<factorval[i]<<" ";
			cout<<endl;
			count++;
		}
		valadd=nextval(valadd);
		
	}
	return 0;
}
