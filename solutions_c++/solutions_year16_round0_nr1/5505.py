#include<iostream>
#include<vector>
using namespace std;

bool check(int x, vector<int> &v)
{
	bool flag = true;
	while(x)
	{
		int r = x%10;
		if(v[r] == 0)
		{
			v[r] = 1;
		}
		x /= 10;
	}
	for(int i=0;i<10;i++)
	{
		if(v[i] == 0)
			flag = false;
	}
	return flag;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int z = 1;
	while(t--)
	{
		cout<<"Case #"<<z<<": ";
		z++;
		std::vector<int> v;
		v.resize(10,0);
		int n;
		cin>>n;
		int no = n;
		int k = 1;
		bool done = false;
		do{
			n = no*k;
			done = check(n,v);
			k++;
			if(k == 1000)
				done = true;
		}
		while(!done);
		if(k < 1000)
		cout<<n<<endl;
		else
			cout<<"INSOMNIA"<<endl;
	}
	return 0;
}