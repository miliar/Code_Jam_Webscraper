#include <fstream>

using namespace std;

int main()
{
	ifstream cin("/home/simon/Downloads/A-large.in");
	ofstream cout("/home/simon/ovacije.out");
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int smax;
		char tab[100000];
		cin>>smax>>tab;
		int rabimo=0;
		int imamo=0;
		for(int j=0;j<=smax;j++)
		{
			imamo=imamo+tab[j]-'0';
			if(imamo<=j)
			{
				rabimo++;
				imamo++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<rabimo<<endl;
	}
}
