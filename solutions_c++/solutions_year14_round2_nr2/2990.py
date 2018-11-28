#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>

using namespace std;
int table[1001][1001];
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("data.out","w",stdout);
	int T;
	int A,B,K;
	int s;
	int num;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		cin>>A>>B>>K;
		num=0;
		for(int i=0;i<A;i++)
		{
			for(int j=0;j<B;j++)
			{
				s=i&j;
				if(s<K)
					num++;
			}
		}
		cout<<"Case #"<<t+1<<": "<<num<<endl;
	}
	return 0;
}