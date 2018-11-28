#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cstdio>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int A;
int N;
int T;
vector<int> M;

int count(int x,int y)
{
	int l0=0;
	int l1=x;
	if(x==1)
	 return -1;
	while(x<=y)
	{
		x=(2*x)-1;
		l0++;
	}
//	printf("%d to %d, %d times\n",l1,y,l0);	
	return l0;
}

int solve(int index,int currSize,int rep)
{
//	cout<<index<<","<<currSize<<","<<rep<<endl;


	if(index>=N)
	{
	return rep;
	}
	else if(M[index] < currSize)
	{
		currSize+=M[index];
		return solve(index+1,currSize,rep);
	}
	else
	{
		if(M[index] < (2*currSize)-1)
		{
			return solve(index+1,2*currSize-1+M[index],rep+1);
		}
		else
		{
		int t0 = count(currSize,M[index]);
		int a0 = solve(index+1,currSize,rep+1);
		int b0 = 999999999;
		if( t0 > 0)
		{
			for(int l0=0;l0<t0;l0++)
				currSize=(2*currSize)-1;
			b0 = solve(index+1,currSize+M[index],rep+t0);
		}
		return (a0>b0) ? b0 : a0;	
		}
	}
}
int main()
{
		
	freopen("c2.in", "r", stdin);
	freopen("c2.out", "w", stdout);

	cin >>T;
	for(int l0=1;l0<=T;l0++)
	{
	cin >> A;
	cin >> N;
		for(int l1=0;l1<N;l1++)
		{
			int t0;
			cin>>t0;
			M.push_back(t0);
		}
		
		sort(M.begin(),M.end());
//		cout<<A<<endl;
//		cout<<N<<endl;
//		for(int l1=0;l1<N;l1++)	cout<<M[l1]<<endl;	
		cout<<"Case #"<<l0<<": ";
		cout<<solve(0,A,0)<<endl;
		M.clear();
	}
}
