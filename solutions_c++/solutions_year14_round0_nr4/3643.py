#include <bits/stdc++.h>
#define loop(i, a, b)  for(int i=a;i<b;i++)
#define rloop(i, a, b)  for(int i=b-1;i>=a;i--)
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
	int t, blocks, n1, n2, a, b;
	float naomi[1001], ken[1001];
	cin>>t;
	loop(te, 0, t)
	{

		cin>>blocks;
		a=blocks-1;
		b=blocks-1;
		n1=0;
		n2=0;
		loop(i, 0, blocks)
			cin>>naomi[i];
        loop(i, 0, blocks)
			cin>>ken[i];
		sort(naomi, naomi + blocks);
		sort(ken, ken + blocks);
		rloop(i, 0, blocks)
		{
			if(naomi[a]>ken[b])
            {
                n2++;
                a--;
            }
			else
			{
				a--;
				b--;
			}
		}
		a=0;
		b=0;
		loop(i, 0, blocks)
		{
			if(naomi[a]>ken[b])
			{
				n1++;
				a++;
				b++;
			}
			else
				a++;
		}
		cout<<"Case #"<<te+1<<": "<<n1<<" "<<n2<<endl;
	}
	return 0;
}
