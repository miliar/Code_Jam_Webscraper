#include <iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	int z; cin>>z; for(int x=0; x<z; x++)
	{
		int w =0;
		int k =0;


		int n; cin>>n;
		for(int i=0; i<=n; i++)
		{
			char a; cin>>a;
			a = a-'0';

			while(k<i)
			{
				w++;
				k++;
			}
			k+=a;

		}

		cout<<"Case #"<<x+1<<": "<<w<<endl;

	}

	return 0;
}