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
int main()
{
	int t, cases = 1, c, x, r;
	cin>>t;
	while(t--)
	{
		cin>>x>>r>>c;
		if(x == 1) //if Gabriel will win no matter what Richard chooses
			cout<<"Case #"<<cases<<": "<<"GABRIEL"<<endl;
		else if(x == 2 and ((c % 2 == 0) or (r % 2 == 0)) )
			cout<<"Case #"<<cases<<": "<<"GABRIEL"<<endl;
		else if(x == 3)
		{
			if((r == 2 and c == 3) or (r == 3 and c == 2) or (r == 4 and c == 3) or (r == 3 and c == 4) or (r == 3 and c == 3))
				cout<<"Case #"<<cases<<": "<<"GABRIEL"<<endl;
			else
				cout<<"Case #"<<cases<<": "<<"RICHARD"<<endl;
		}
		else if(x == 4)
		{
			if((r == 3 and c == 4) or (r == 4 and c == 3) or (r == 4 and c == 4))
				cout<<"Case #"<<cases<<": "<<"GABRIEL"<<endl;
			else
				cout<<"Case #"<<cases<<": "<<"RICHARD"<<endl;
		}
		else
			cout<<"Case #"<<cases<<": "<<"RICHARD"<<endl;
		cases++;
	}
	return 0;
}
