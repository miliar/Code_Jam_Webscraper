#include<iostream>
#include<vector>
#include<algorithm>
#include <string>
using namespace std;

typedef long long ll;

bool isPali(ll val)
{
	vector<int> v;
	
	do
	{
		v.push_back(val%10);
		val /= 10;
	}while(val);

	int s = v.size();

	for(int i=0;i<v.size();i++)
		if(v[i] != v[s-i-1])
			return false;

	return true;
}

int main() {
 
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w", stdout);

	int k;
	cin>>k;

	for(int i=0;i<k;i++)
	{
		ll a, b;
		cin>>a>>b;
		int ans = 0;
		for(ll v = 1;v<=10000000;v++)
			if(v*v <= b && v*v >= a && isPali(v) && isPali(v*v))
				ans++;

		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}

    return 0;
}