#include<iostream>
#include<string>
#include<stack>
#include<vector>
using namespace std;
int min(int a,int b)
{
	return a<b?a:b;
}
int waysToWin(int a, int b,int k)
{
	int a1=0,b1=0;
	int cnt=0;
	for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
		{
			if((i&j)<k)
			{
				
				cnt++;
			}
		}
	return cnt;

}

int main()
{

	int cases;
	cin>>cases;
	int T=1;
	int a,b,k;
	while(T<=cases)
	{
		cin>>a>>b>>k;
		cout<<"Case #"<<T<<": ";
		cout<<waysToWin(a,b,k)<<endl;
		T++;
	}
	return 0;
}


