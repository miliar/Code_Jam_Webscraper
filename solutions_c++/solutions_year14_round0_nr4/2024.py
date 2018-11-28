#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;

const double eps=0.000001;
int T,n;
deque<double> v1,v2;
void ReadTAndSort()
{
	cin>>n;
	v1.clear();
	v2.clear();
	v1.resize(n);
	v2.resize(n);
	for(int i=0;i<n;++i)
		cin>>v1[i];
	for(int i=0;i<n;++i)
		cin>>v2[i];

	sort(v1.begin(),v1.end());
	sort(v2.begin(),v2.end());
}

int GetTrueAnsw(deque<double> d1, deque<double> d2)
{
	int answ=0;
	for(int i=n-1;i>-1;--i)
	{
		double ShePresents=d1[i];
		if(d2.back()>=ShePresents)
			d2.pop_back();
		else
		{
			++answ;
			d2.pop_front();
		}
	}
	return answ;
}

int GetSlyAnsw(deque<double> d1, deque<double> d2)
{
	int answ=0;
	for(int i=0;i<n;++i)
		if(d1.front()>d2.front())
		{
			++answ;
			d1.pop_front();
			d2.pop_front();
		}
		else
		{
			d1.pop_front();
			d2.pop_back();
		}

	return answ;
}





int main()
{
	freopen("D:\\in.txt","r",stdin);
	freopen("D:\\out.txt","w",stdout);
	cin>>T;
	for(int i=0;i<T;++i)
	{
		ReadTAndSort();
		int Answ1=GetTrueAnsw(v1,v2);
		int Answ2=GetSlyAnsw(v1,v2);
		cout<<"Case #"<<i+1<<": "<<Answ2<<' '<<Answ1<<endl;
	}
	return 0;
}