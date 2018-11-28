#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
	ofstream myout;
	myout.open("output.txt",ios::out);
	int tst;
	cin>>tst;
	for(int re=0;re<tst;re++)
	{
		int ans1,ans2;
		cin>>ans1;
		int ar[4],br[4];
		int dump;
		for(int i=0;i<4*(ans1-1);i++)
		{
			cin>>dump;
		}


		for(int u=0;u<4;u++)
		{
			cin>>ar[u];
		}
		for(int i=4*ans1;i<=15;i++)
		{
			cin>>dump;
		}

		cin>>ans2;

		for(int i=0;i<4*(ans2-1);i++)
		{
			cin>>dump;
		}

		for(int u=0;u<4;u++)
		{
			cin>>br[u];
		}
		for(int i=4*ans2;i<=15;i++)
		{
			cin>>dump;
		}

		sort(ar,ar+4);
		sort(br,br+4);

		int ans;
		int h=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(ar[i]==br[j])
				{

				h++;
				ans=ar[i];
				break;}
			}
		}

		if(h==0)
		{
			myout<<"Case #"<<re+1<<": Volunteer cheated!\n";
		}
		else if(h==1)
		{
			myout<<"Case #"<<re+1<<": "<<ans<<"\n";
		}
		else if(h>1)
		{
			myout<<"Case #"<<re+1<<": Bad magician!\n";
		}
	}
	myout.close();
	return 0;

}

