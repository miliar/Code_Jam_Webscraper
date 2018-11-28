#include <iostream>
#include <vector>
#include <string>

using namespace std;

void main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin >> t;

	for (int i = 0; i<t; i++){
		int n;
		cin>>n;
		int m[10000];

		for (int j = 0; j<n; j++)
			cin>>m[j];
		int answer1 = 0;
		int answer2 = 0;

		int max = 0;
		for (int j = 0; j<n-1; j++)
		{
			if (m[j]>m[j+1]) answer1+= m[j]-m[j+1];

			if (m[j]>m[j+1] && m[j] - m[j+1] > max)
				max = m[j] - m[j+1];
		}
		for (int j = 0; j<n-1; j++)
				answer2+=min(max,m[j]);

		cout<<"Case #"<<i+1<<": "<<answer1<<" "<<answer2<<endl;
	}
}