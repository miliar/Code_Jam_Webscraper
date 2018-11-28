#include<fstream>

using namespace std;

int main()
{
	ifstream readfile("C:/Users/user/Desktop/B-small-attempt0.in");
	ofstream writefile("C:/Users/user/Desktop/results.txt");
	
	int a;
	readfile>>a;
	for(int i=0;i<a;i++)
	{
		int b,c,d;
		int ans=0;
		readfile>>b>>c>>d;
		for(int j=0;j<b;j++)
		{
			for(int k=0;k<c;k++)
			{
				int w=j&k;
				
				if(w<d) ans++;
			}
		}
		writefile<< "Case #"<<i+1<<": "<<ans<<"\n";
	}
	return 0;
}
	
