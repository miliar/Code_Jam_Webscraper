#include<bits/stdc++.h>
using namespace std;
#define S(x) scanf("%d",&x)
#define MOD 1000000007
#define ll long long
int a[1234567];
int main()
{
	freopen("C:\\Users\\screw_1011\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\screw_1011\\Desktop\\output.txt","w",stdout);
	int t,n,final,standing;
	S(t);
	string s;
	for (int j = 1; j <=t; ++j)
	{
		S(n);
		cin>>s;
		standing = s[0]-48;
		final =0 ;
		for (int i = 1; i <s.size(); ++i)
		{
			if(standing>=i)
			{
				standing  = standing + s[i]-48;	
			}
			else
			{
				final = final + abs(i-standing);
				standing = standing + abs(i-standing);
				standing = standing + s[i] - 48;
			}
		}
		cout<<"Case #"<<j<<": "<<final<<endl;
	}
	return 0;
}
