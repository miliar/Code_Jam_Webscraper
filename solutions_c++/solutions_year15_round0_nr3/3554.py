#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<map>
#include<set>
#include<vector>
#include<utility>

using namespace std;
int dig[5][5];

int main() 
{
	dig[1][1] = 1;
	dig[1][2] = 2;
	dig[1][3] = 3;
	dig[1][4] = 4;
	dig[2][1] = 2;
	dig[2][2] = -1;
	dig[2][3] = 4;
	dig[2][4] = -3;
	dig[3][1] = 3;
	dig[3][2] = -4;
	dig[3][3] = -1;
	dig[3][4] = 2;
	dig[4][1] = 4;
	dig[4][2] = 3;
	dig[4][3] = -2;
	dig[4][4] = -1;

	int t, l, x, i, c = 1, ans, minus, flag1, flag2, idx;
	string str;
	cin>>t;
	while(t--)
	{
		cin>>l>>x;
		cin>>str;
		int num[l*x];
		if(l <= 2 and x <= 1)
			cout<<"Case #"<<c<<": NO"<<endl;
		else
		{
			for(i = 0; i < l; i++)
				num[i] = str[i] - 'g';			
			for(i = l; i < l*x; i++)
				num[i] = num[i-l];
			/*for(i = 0; i < l*x; i++)
				cout<<num[i];
			cout<<endl;*/
			ans = num[0];
			minus = 0;
			for(i = 1; i < l*x; i++)
				ans = (ans/abs(ans))*dig[abs(ans)][num[i]];
			if(ans != -1)
				cout<<"Case #"<<c<<": NO"<<endl;
			else
			{
				flag1 = 0;
				for(i = 0; i < l*x; i++)
				{
					if(i == 0)
						idx = num[0];
					else
						idx = (idx/abs(idx))*dig[abs(idx)][num[i]];
					if(idx == 2)
					{
						flag1 = 1;
						i++;
						break;
					}
				}
				flag2 = 0;
				for(; i < l*x; i++)
				{
					idx = (idx/abs(idx))*dig[abs(idx)][num[i]];
					if(idx == 4)
					{
						flag2 = 1;
						break;
					}
				}
				if(flag1 and flag2)
					cout<<"Case #"<<c<<": YES"<<endl;
				else
					cout<<"Case #"<<c<<": NO"<<endl;
			}
		}
		c++;
	}
	return 0;
}
