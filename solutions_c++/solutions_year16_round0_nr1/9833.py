#include<sstream>
#include<iostream>
#include<thread>
#include<set>
#include<vector>

using namespace std;

void print_num(int case_num, int n)
{
	if(n==0)
	{
		cout<<"Case #"<<case_num<<": INSOMNIA"<<endl;
		return;
	}
	int temp=n;
	int nn=n;
	set<int> s;
	while(true)
	{
		temp=nn;
		while(temp!=0)
		{
			s.insert(temp%10);
			temp/=10;
		}
		if(s.size()==10)
		{
			break;
		}
		nn+=n;
	}
	cout<<"Case #"<<case_num<<": "<<nn<<endl;
}

int main()
{
	int cases=0;
	cin>>cases;
	vector<thread> v;
	int val=0;
	for(int i=0;i<cases;++i)
	{
		cin>>val;
		print_num(i+1,val);
		//v.push_back(thread(print_num,i+1,val));
	}
	for(auto it=v.begin();it!=v.end();++it)
	{
		//it->join();
	}
}
