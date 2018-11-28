#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

unsigned long proc(long motes, vector<long>::iterator begin, vector<long>::iterator end)
{
	long mote=motes;
	unsigned long res=-1, tmp;
	vector<long>::iterator cur=begin;
	while (cur!=end && mote>*cur)
	{
		mote+=*cur;
		++cur;
	}
	if (cur==end)
		return 0;
	if (mote*2-1<=mote)
		return end-cur;
	for (int i=1; i<end-cur; ++i)
	{
		mote+=mote-1;
		tmp=i+proc(mote, cur, end);
		if (tmp<res)
			res=tmp;
	}
	if (res<end-cur)
		return res;
	else
		return end-cur;
}

int main()
{
	int T;
	long A, N;
	unsigned long res;
	vector<long> motes;
	cin>>T;
	for (int cases=1; cases<=T; ++cases)
	{
		motes.clear();
		res=0;
		cin>>A>>N;
		for (int i=0; i<N; ++i)
		{
			long tmp;
			cin>>tmp;
			motes.push_back(tmp);
		}
		sort(motes.begin(), motes.end());
		res=proc(A, motes.begin(), motes.end());
		cout<<"Case #"<<cases<<": "<<res<<endl;
	}
	return 0;
}
