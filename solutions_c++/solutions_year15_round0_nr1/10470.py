#include<fstream>
using namespace std;
int main()
{
	ifstream cin("C:/Users/sarthak/Desktop/A-small-attempt1.in");
	ofstream cout("C:/Users/sarthak/Desktop/output.txt");
	unsigned long long int t,i,j,k,s;
	char c[1004];
	cin>>t;
	for(k=0;k<t;k++)
	{
		cin>>s;
		cin>>c;
		unsigned long long int count,ans=0;
		count=c[0]-'0';
	
		for(i=1;i<=s;i++)
		{
			if((count<i)&&(c[i]!='0'))
			{
				ans=i-count+ans;
				count=count+ans;
			
			}
				count=count+c[i]-'0';
		}
		cout<<"Case #"<<k+1<<": "<<ans<<endl;
	}
	
}
