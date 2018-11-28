#include <iostream>
#include <string>
using namespace std;


unsigned long long N;
bool ex[10];
void fill(long long num)
{
	while(num>0LL)
	{
	int dig = num%10;
		ex[dig] = true;
	num/=10LL;	
	}
}
long long solve()
{
	if(N==0LL) return -1LL;

	for(int i =  0 ; i < 10;i ++)
	 ex[i] = false;
long long i = 1LL, M = N;

	while(true)
	{
		bool t = true;
	fill(N);
		for(int i = 0 ; i < 10  && t; i ++)
					if(!ex[i]) t = false;
		
	if(t) return M*i;
		i++;
	N = M * i;

	}
}
int main()
{
	
	  ios_base::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);   freopen("1.out","w",stdout);
 int T;
 cin >> T;
 long long maxres=0;
 for(int i = 0 ; i <T ; i++)
 {
 
	cin >> N;
	long long res = solve();

	cout << "Case #"<< i +1 <<  ": ";
	if(res == -1)
	cout << "INSOMNIA";
	else 
	cout << res;
	cout << endl;
	}
//cout << maxres << endl;
	return 0;
}
