#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int Max(int a, int b)
{
	return (a>b) ? a : b;
}

int play2(vector<double> a, vector<double> b)
{
	int res=0;
	for(int i=0;i<a.size();i++)
	{
		int cur = a[i];
		bool found = false;
		for(int j=0;j<b.size();j++)
		{
			if(b[j] > a[i])
			{
				for(int k = j; k<b.size()-1;k++)
					b[k] = b[k+1];
				b.pop_back();
				found = true;
				break;
			}
		}
		if(!found)
		{
			res++;
			for(int k=0;k<b.size()-1;k++)
				b[k] = b[k+1];
			b.pop_back();
		}
	}
	return res;
}

int playR1(deque<double> a, deque<double> b)
{
	if(a.size() == 0) return 0;
	if(a.size()==1) return (a.front()>b.front()) ? 1 : 0;

	deque<double> copyA = a;
	deque<double> copyB = b;
	deque<double> copyA2 = a;
	deque<double> copyB2 = b;

	int res1 = (a.front() > b.back()) ? 1 : 0;
	a.pop_front();
	b.pop_back();
	res1 += playR1(a,b);

	int res2 = (copyA.back() > copyB.front()) ? 1 : 0;
	copyA.pop_back();
	copyB.pop_front();
	res2 += playR1(copyA,copyB);

	int res3 = (copyA2.front() > copyB2.front()) ? 1 : 0;
	copyA2.pop_front();
	copyB2.pop_front();
	res3 += playR1(copyA2,copyB2);

	return Max(res1,Max(res2,res3));
}


int play1(vector<double> a, vector<double> b)
{
	deque<double> aa(a.begin(),a.end());
	deque<double> bb(b.begin(),b.end());
	int res=0;
	while(aa.size()>0)
	{
		if(aa.front()>bb.front())
		{
			res++;
			aa.pop_front();
			bb.pop_front();
		}
		else
		{
			aa.pop_front();
			bb.pop_back();
		}
	}
	return res;
}

void run()
{
	int N;
	cin>>N;
	vector<double> a(N),b(N);
	for(int i=0;i<N;i++) cin>>a[i];
	for(int i=0;i<N;i++) cin>>b[i];

	sort(a.begin(),a.end());
	sort(b.begin(),b.end());

	int res1 = play1(a,b);
	int res2 = play2(a,b);

	cout<<res1<<' '<<res2<<endl;
}

int main()
{
	string input_name = "D-large.in";
	freopen(input_name.c_str(),"r",stdin);

	string output_name = "output.txt";
	freopen(output_name.c_str(),"w",stdout);
		
	int test;
	cin>>test;
	for(int i = 1;i<=test;i++)
	{
		cout<<"Case #"<<i<<": ";
		run();
	}
	return 0;
}
