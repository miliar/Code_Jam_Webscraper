#include<bits/stdc++.h>

using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
            freopen("B-large.in", "r", stdin);
            freopen("2large.out", "w", stdout);
    #endif // ONLINE_JUDGE
	int t;
	scanf("%d",&t);
	for(int j=1;j<=t;j++)
	{
		string str;
		cin >> str;
		int count = 0;
		for(int i=0;i<str.length()-1;++i)
		{
			if(str[i+1]==str[i]);
			else
			{
				for(int j=0;j<=i;++j)
					str[j] = str[i+1];
				count++;
			}
		}
		if(str[str.length()-1]=='-')
			count++;
		cout << "Case #" << j <<": "<<count<<endl;
	}
}
