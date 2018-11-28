#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;
void nalesniki()
{
	int n;
	cin>>n;
	int PiMAX=0;
	vector<int> P(n);
	for(int i=0 ; i<n; i++)
	{
		cin>>P[i];
		PiMAX=max(PiMAX, P[i]);
	}
	int result=2000000000;
	for(int k=1; k<=PiMAX; k++)
	{
		int tmp=0;
		for(int i=0; i<n; i++)
		{
			tmp+=P[i]/k;
			if(P[i]%k==0)
				tmp--;
		}
		tmp+=k;
		result=min(result, tmp);
	}
	cout<<result<<endl;;
}
int main()
{
	ios_base::sync_with_stdio(false);
	int z;
	cin>>z;
	for(int i=1; i<z+1; i++)
	{
		cout<<"Case #"<<i<<": ";
		nalesniki();
	}
	return 0;
}
