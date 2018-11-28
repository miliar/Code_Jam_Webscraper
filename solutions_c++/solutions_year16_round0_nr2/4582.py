#include <bits/stdc++.h>

using namespace std;

#define eb emplace_back
typedef unsigned long long int llu;

int main()
{
	int t;
	cin >> t;
	for (int j = 0; j < t; j++)
	{
		string a;
		cin >> a;
		int v[200];
		int ans=0;
		
		v[0]=0;
		int sz=a.size();
		for (int i = 0; i < sz; i++)
		{
			if(i==0){
				if(a[i]=='+') v[i]=0;
				else v[i]=1;
			}else{
				if(a[i]=='+') v[i]=v[i-1];
				else{
					if(a[i-1]=='-') v[i]=v[i-1];
					else v[i]=v[i-1]+2;
				}
			}
		}
		
		printf("Case #%d: %d\n", j+1, v[sz-1]);
		//cout << v[a.size()-1] << endl;
		
	}
	
	
	return 0;
}
