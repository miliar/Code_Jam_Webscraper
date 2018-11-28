#include<iostream>
#include<cmath>
#include<string>
#include<vector>
#include<fstream>
#include<sstream>

using namespace std;
double a=0.0,b=0.0;

bool isp(double y)
{
if (fmod(y,1.0) > 0.0) return 0;
int x=(int)y;

stringstream ss;ss<<x;string st=ss.str();

	for (int i=0;i<(int)(st.size()/2);++i)
	{
		if(!(st[i]==st[st.size()-i-1]))
			return 0;
	}
return 1;
}


int main()
{	
	ofstream out;out.open("output.txt");
	ifstream infile; infile.open("input.in");
	int t;
	infile>>t;
	//cout<<t<<endl;
	for (int i=1;i<=t;++i)
	{
		int n=0;
		infile>>a>>b;
		for(double j=a;j<=b;j+=1.0)
		{
			double sqj=sqrt((double)j);
			if(isp(j)&&isp(sqj))
			{
			n++;
			}
		}
		
	out<<"Case #"<<i<<": "<<n<<endl;
	
	}
	

	
}