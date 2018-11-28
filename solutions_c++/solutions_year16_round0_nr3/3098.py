#include <bits/stdc++.h>
using namespace std;
#define ll long long int

ll power(ll x, ll y)
{
    if( y == 0)
        return 1;
    else if (y%2 == 0)
        return power(x, y/2)*power(x, y/2);
    else
        return x*power(x, y/2)*power(x, y/2);
 
}

int main()
{
	ll N, i, j, k, J, t, l;
	cin >> t;
	for(i=0; i<t; i++)
	{
		ll count = 0;
		cin >> N;
		cin >> J;
		cout << "Case #" << t << ": " << '\n';
		for(j=1; j<N-1; j++)
		{
			for(k=j+1; k<N; k++)
			{
				ll arr[N];
				ll arr2[9];
				for(l=0; l<N; l++)
				{
					arr[l]=0;
				}
				ll y = N-1-k;
				ll z = N-1-k+j;
				if(y!=j && y!=k && j!=z && k!=z)
				{
					arr[y] = 1;
					arr[z] = 1;
					arr[j] = 1;
					arr[k] = 1;
					arr[0] = 1;
					arr[N-1] = 1;
					if(k > N-1-k)
					{
						for(l=2; l<11; l++)
						{
							arr2[l-2] = 1+ power(l,N-1-k);
						}
					}
					else
					{
						for(l=2; l<11; l++)
						{
							arr2[l-2] = 1+ power(l,N-1-k);
						}
					}
					string s="";
					for(l=0;l<N;l++)
					{
						s+=to_string(arr[l]);
					}
					
					cout << s << " ";
					for(l=0; l<9; l++)
					{
						cout << arr2[l] << " ";
					} 
					cout << '\n';
					count++;
					if(count == J)
					{
						break;
					}
				}

			}
			if(count == J)
			{
				break;
			}
		}
		

	}
}