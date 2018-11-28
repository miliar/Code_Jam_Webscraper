#include<iostream>
#include<string>
using namespace std;
bool is(char a)
{
	switch ( a)
	{
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u':
			return 0;
	}
	return 1;

}


int main()
{
	int N;
	cin>>N;
	for ( int ttt=1;ttt<=N;ttt++)
	{
		cout<<"Case #"<<ttt<<": ";
		int n;
		string a;
		cin>>a;
		cin>>n;
		int ans=0;
		for (int i =0;i<a.size();i++)
		{
			for (int j=i;j<a.size();j++)
			{
				int count=0; 
				for ( int k=i; k <=j; k++) 
				{
					if(is(a[k]))
						count++;
					else
						count=0;
					if(count == n)
					{

						ans++;
						break;


					}



				}



			}

		}
                 cout<<ans<<endl;



	}



}
