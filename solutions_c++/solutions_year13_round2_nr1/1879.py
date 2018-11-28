#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	long t=0;
	cin>>t;

	int N,A;
	int k;
	vector<int> vec;
	int count=0;
	int mincount;
	for(int j=0;j<t;j++)
	{
		cin>>A>>N;
		count=N;
		mincount=N;
		for(int i=0;i<N;i++)
		{
			cin>>k;
			vec.push_back(k);
		}
		sort(vec.begin(),vec.end());

		for(int i=0;i<vec.size();)
		{
			if(vec[i]<A)
				{A+=vec[i++];count--;}
			else
			{
				if(vec[i]>=A)
				{
					if(A<=1)
						break;
					A+=(A-1);
					count++;
					
				}
			}
			if(count<mincount)mincount=count;
		}
		cout<<"Case #"<<j+1<<": "<<mincount<<endl;
		vec.clear();
	}
	return 0;
}