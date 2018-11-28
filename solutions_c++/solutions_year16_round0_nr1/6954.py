#include <iostream>
#include <cstdio>
using namespace std;
bool dig [10] = {false};
int digc(int n)
{
	int digs = 1;
	while(true)
	{
		n /= 10;
		if(n == 0)
			break;
		digs++;
	}
	return digs;

}
void count(int n)
{
	int base = 1;
	for(int i = 0 ; i < digc(n)-1;i++)
		base *= 10;
	while(base != 0)
	{
		//cout << (n%(base*10))/base << " ";
		dig[(n%(base*10))/base] = true;
		base /= 10;
	}
	
}
int stop(int last,int now)
{
	if(last == now)
		return true;

	int ok = 0;
	for(int i = 0 ; i< 10 ; i++)
	{
		if(dig[i])
			ok ++;
	}
	if(ok == 10)
		return true;
	else
		return false;
}
int main ()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int t;
	cin >> t;
	for(int tn = 1 ; tn <= t ; tn++)
	{
		for(int i = 0 ; i< 10 ; i++)
			dig[i] = false;
		int n;
		cin >> n;
		int T = 2;
		count(n);
		int last  = n;
		int next = n * T ;
		while(!stop(last,next))
		{
			T++;
			count(next);
			last = next;
			next = n * T;
			//cout << "For "<< last <<endl;
		}

		int ok = 0;
		for(int i = 0 ; i< 10 ; i++)
		{
			if(dig[i])
				ok ++;
		}
		cout<<"Case #"<<tn<<": ";
		if(ok == 10)
			cout<<last<<endl;
		else
			cout<<"INSOMNIA\n";	
	}

}