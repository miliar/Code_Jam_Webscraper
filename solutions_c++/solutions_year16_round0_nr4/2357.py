#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	
	freopen("D-small-attempt0.in","r",stdin);
	freopen("a.txt","w",stdout);
	
	cin >> t;
	
	for(int tt=0;tt<t;tt++)
	{
		int k,c,s;
		
		cin >> k >> c >> s;
		
		cout << "Case #" << tt+1 << ": ";
		
		if(s<(k+1)/2)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		
		if(c==1)
		{
			if(s!=k)
				cout << "IMPOSSIBLE" << endl;
			else
			{
				for(int i=0;i<k;i++)
					cout << i+1 << " ";
					
				cout << endl;
			}
			
			continue;
		}
		
		int cnt=1;
		
		if(k%2)
			cnt=0;
		
		for(int i=0;i<(k+1)/2;i++,cnt+=k+1)
			cout << cnt+(k+1)/2 << " ";
			
		cout << endl;
	}
	
	return 0;
}
