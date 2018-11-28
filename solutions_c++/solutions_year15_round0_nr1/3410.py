#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin>>t;

	for (int j = 0; j<t; j++)
	{
		int sMax;
		cin>>sMax;
		char c;

		int answer = 0;
		int cursum = 0;

		for (int i = 0; i<=sMax; i++)
		{
			cin>>c;
			
			if (!(cursum>=i))
				answer+=i-cursum,cursum=i;
			cursum+=(int)c-48;
		}
		cout<<"Case #"<<j+1<<": "<<answer<<endl;
	}
}