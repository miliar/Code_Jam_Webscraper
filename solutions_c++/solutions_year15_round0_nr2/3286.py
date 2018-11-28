#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void main(){
	int t;
	cin>>t;
	for (int j = 0; j<t; j++)
	{
		int d;
		int p[1005];
		int max = 0;
		int time = 0;

		memset(p,0,sizeof(p));
		cin>>d;
		for (int i = 0; i<d; i++)
		{
			cin>>p[i];			
			if (p[i]>max) max = p[i];
		}

		int answer = 9999999;
		for (int k = 1; k<=max; k++)
		{
			int sum = 0;
			for (int i = 0; i<d; i++)
				if (p[i]>k)
					sum+=(p[i]+(k-1))/k - 1;
			if (sum+k <answer) answer = sum+k;
		}
		cout<<"Case #"<<j+1<<": "<<answer<<endl;
	}
}