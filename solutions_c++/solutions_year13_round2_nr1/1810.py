#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	long long int t=0;
	cin>>t;

	long long int N,A;
	long long int temp;
	vector<long long int> v;
	long long int count=0;
	long long int min_count;
	for(long long int j=0;j<t;j++)
	{
		cin>>A>>N;
		count=N;
		min_count=N;
		for(long long int i=0;i<N;i++)
		{
			cin>>temp;
			v.push_back(temp);
		}
		sort(v.begin(),v.end());

		for(long long int i=0;i<v.size();)
		{
			if(v[i]<A)
				{A+=v[i++];count--;}
			else
			{
				if(v[i]>=A)
				{
					if(A<=1)
						break;
					A+=(A-1);
					count++;
					
				}
			}
			if(count<min_count)
				min_count=count;
		}
		cout<<"Case #"<<j+1<<": "<<min_count<<endl;
		v.clear();
	}
	return 0;
}