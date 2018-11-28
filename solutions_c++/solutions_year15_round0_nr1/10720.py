
#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);

	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);


	//Testcases
	int t, t_copy;
	cin>>t;
	t_copy = t;

	while(t--)
	{
		int inp;
		cin>>inp;
		string val;
		cin>>val;
		vector<int> x;

		//cout<<val[0]<<"  "<<val[inp]<<"  "<<endl;
		
		//Convert the string to a number
		int d;
		for(d=0; d<=inp; d++)
			x.push_back(val[d]-48);

		//Print the numbers
		/*for(d=0; d<=inp; d++)
			cout<<x[d]<<" ";
		cout<<endl;*/

		int i, sum = x[0], ans = 0;
		for(i=1; i<=inp; i++)
		{
			if(x[i]==0)
				continue;
			if(i>sum)
				ans = ans + i - sum;
			//cout<<"\n"<<sum<<"\t"<<ans<<"\t"<<x[i];
			sum = sum + x[i] + ans;
		}

		//Display the output
		printf("Case #%d: %d\n", t_copy-t, ans);
		
	}

	return 0;
}


