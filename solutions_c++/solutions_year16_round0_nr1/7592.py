#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
bool checkx(vector<int> l,int x)
{
	for(int i=0;i<l.size();i++)
	{
		if(x==l[i])
			return true;
	}
	return false;
}
bool checkend(vector<int> l)
{
	if(l.size()==10)
		return true;
	return false;
}
int no(int x)
{
	int count = 0;
	while(x>0)
	{
		x/=10;
		count++;
	}
	return count;
}
int main()
{
	vector<int> l;
	int T;
	int i = 0;
	cin>>T;
	while(T>0)
	{
		i++;
		if(!l.empty())
			l.clear();
		long int N;
		cin>>N;
		if(N==0)
		{
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
			T--;
			continue;
		}
		long int b;
		long int c = N;
		
		while(!checkend(l))
		{
			
			b = N;
			
			while(b>0)
			{
				int d = b%10;
				if(!checkx(l,d))
					l.push_back(d);
				b/=10;
			}
			if(checkend(l))
			{
				cout<<"Case #"<<i<<": "<<N<<endl;
				break;
			}
			N = N+c;
		}
		T--;
	}
	return 0;
}