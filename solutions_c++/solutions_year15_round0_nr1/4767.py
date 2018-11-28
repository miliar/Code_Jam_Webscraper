#include <iostream>
using namespace std;
int main()
{
	int T,Smax,curShy,standing=0,invited=0,n=1;
	string shylevels;
	cin>>T;
	while(n<=T)
	{
		standing=0;
		invited=0;
		cin>>Smax;
		cin>>shylevels;
		for(int i=0;i<Smax+1;i++)
		{
			curShy=shylevels[i]-'0';
			if(standing>=i)
			{
				standing+=curShy;
			}
			else
			{
				invited+=i-standing;
				standing=i+curShy;
			}
		}
		cout<<"Case #"<<n<<": "<<invited<<endl;
		n++;
	}
	return 0;
}