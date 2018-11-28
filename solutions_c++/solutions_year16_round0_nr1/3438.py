#include<bits/stdc++.h>
using namespace std;
#define fs first
#define sc second
#define INF 1000000000
#define p 1000000007
#define pb push_back
#define mp make_pair
typedef long long Int;
typedef pair<Int,Int> pii;
typedef vector<Int> vi;
typedef vector<pii> vii;
Int N,T;
bool check1(int * visited)
{
	for(int i=0;i<=9;i++){
		if(visited[i])
			continue;
		else
			return true;
	}
	return false;
}
Int check(Int N,int* visited)
{
	if(N==0)
		return 0;
	else
	{
		Int count=1;
		Int ans;
		while(check1(visited))
		{	
			int temp=N*count;
			 ans=temp;
			while(temp)
			{
				visited[temp%10]=true;
				temp/=10;
			}
			count++;
		}
		return ans;
	}
}

int main() {
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		int visited[10]={0};

		cin>>N;

		cout<<"Case #"<<i<<": ";
		Int temp=check(N,visited);
		if(temp==0)
			cout<<"INSOMNIA"<<endl;
		else
			cout<<temp<<endl;
	}

		
	return 0;
}