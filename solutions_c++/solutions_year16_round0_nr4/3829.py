#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
void process(std::istream& ip,std::ostream& op)
{
	int tc,i,x,k,c,s,j;
	ip>>tc;
	for(x=1;x<=tc;x++)
	{
		op<<"Case #"<<x<<": ";		
		ip>>k>>c>>s;
		if(k==1)
		{
			op<<1<<"\n";
		}
		else if(c==1)
		{
			for(i=1;i<k;i++)
				op<<i<<" ";
			op<<k<<"\n";
		}
		else
		{
			for(i=1,j=2;i<k-1;i++,j+=(k+1))
			{
				op<<j<<" ";
			}
			op<<j<<"\n";
		}
	}
}
int main()
{
	ifstream myfile ("D-small-attempt0.in");
	ofstream file ("D-small-attempt0 op.in");
	process(myfile,file);
}