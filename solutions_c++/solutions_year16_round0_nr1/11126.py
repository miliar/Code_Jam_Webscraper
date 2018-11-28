#include <iostream>
#include <fstream>
#include <bitset>

using namespace std;

const int inf = 1e9+7;

bitset<10> a;
int get(long long int n,long long int i)
{
	if(i>10000||n==0) return inf;
	if(a.count()==10)
	{
		return n*(i-1);
	}
	long long int n1 = n*i;
	do
	{
		a[n1%10] = 1;
		n1/=10;
	}
	while(n1>0);
	return(get(n, i+1));
}
int main(){
	ios::sync_with_stdio(false);
	ifstream cin("adat.txt");
	ofstream cout("output.txt");
	long long int n;
	long long int answer;
	cin >> n;
	for(int i = 0; i<n; i++)
	{
		a.reset();
		cin >> answer;
		answer = get(answer,1);
		cout << "Case #"<<i+1<<": ";
		if(answer!=inf)
		{
			cout << answer << "\n";
		}
		else
		{
			cout << "INSOMNIA\n";
		}
	}
	return 0;
}