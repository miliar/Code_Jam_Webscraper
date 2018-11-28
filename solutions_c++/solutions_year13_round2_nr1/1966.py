#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<algorithm>
#include<cmath>
#include<math.h>
using namespace std;
vector<int>V;
int arr[101][1000001];
long long R(long long i,long long sum)
{
	if(i==V.size())
		return 0;
	if(arr[i][sum]!=-1)
	{
		return arr[i][sum];
	}
	if(V[i]<sum)
		return R(i+1,sum+V[i])+0;
	long long A=100000001,B=100000001;
	if(sum>1)
		 A=R(i,sum+sum-1)+1;
	B=R(i+1,sum)+1;
	return arr[i][sum]=min(A,B);

}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out","w",stdout);
	int T,A,N,M,counter;
	cin>>T;
	for(int CASE=1 ; CASE<=T ; CASE++)
	{
		memset(arr,-1,sizeof(arr));
		counter=0;
		cin>>A>>N;
		for(int i=0 ;i<N ; i++)
		{
			cin>>M;
			V.push_back(M);
		}
		sort(V.begin(),V.end());
		counter=R(0,A);
		cout<<"Case #"<<CASE<<": "<<counter<<endl;
		V.clear();
	}
	return 0;
}