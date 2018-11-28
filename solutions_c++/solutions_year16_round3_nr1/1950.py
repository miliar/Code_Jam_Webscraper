#include <bits/stdc++.h>
using namespace std;

class party
{
public:
	party()
	{
		members = 0;
		id = -1;
	}
	int id,members;
};

bool fun(party a, party b)
{
	return a.members > b.members;
}

int k = 1;
void solve()
{
	int n;
	cin>>n;
	party arr[n];
	
	int total = 0;

	int temp;
	for (int i = 0; i < n; ++i)
	{
		cin>>temp;
		arr[i].members = temp;
		arr[i].id = i;
		total += arr[i].members;
	}

	int a,b;
	int count = total;
	while(count != 0 )
	{
		sort(arr,arr+n, fun);
		cout.flush();
		if(count == 1)
		{
			cout<<(char)(arr[0].id + 'A');
			count--;
		}
		else if(count == 2)
		{
			if(arr[1].members == 0)
			{
				cout<<(char)(arr[0].id + 'A')<<(char)(arr[0].id + 'A');
				count -= 2;
			}
			else
			{
				cout<<(char)(arr[0].id + 'A')<<(char)(arr[1].id + 'A');
				count-=2;
			}
		}
		else
		{
			cout<<(char)(arr[0].id + 'A');
			arr[0].members-=1;
			count--;
			if(count == 2){
				cout<<" ";
				continue;
			}
			sort(arr,arr + n, fun);
			cout<<(char)(arr[0].id + 'A');
			arr[0].members-=1;
			count--;
		}
		cout<<" ";
	}
	cout<<"\n";
	
}

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		cout<<"Case #"<<k<<": ";
		solve();
		k++;
	}
}