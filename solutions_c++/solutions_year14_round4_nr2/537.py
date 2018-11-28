#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int N;
		cin>>N;
		vector<int> A(N);
		for(int i=0;i<N;i++)cin>>A[i];
		int S=0;
		while(!A.empty())
		{
			const int i=min_element(A.begin(),A.end())-A.begin();
			S+=min(i,(int)A.size()-1-i);
			A.erase(A.begin()+i);
		}
		cout<<"Case #"<<t<<": "<<S<<endl;
	}
	return 0;
}
