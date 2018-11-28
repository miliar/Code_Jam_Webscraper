#include <bits/stdc++.h>
using namespace std;
set<int> s;

void visitedDigit(long long x)
{
	while(x!=0)
	{
		int digit=x%10;
		s.insert(digit);

		x=x/10;
	}

}
int main()
{
	int t;
	scanf("%d",&t);

	for(int q=1;q<=t;q++)
	{
		int n;
		scanf("%d",&n);
		s.clear();
		if(n==0) {printf("Case #%d: INSOMNIA\n",q) ; continue;}
		long long no;
		
		
			for(int i = 1 ; ; i++)
			{
				 no= n*i;

				visitedDigit(no);

				if(s.size()==10) {
					break;
				}




			}

			printf("Case #%d: %lld\n",q,no);

		


	}


}