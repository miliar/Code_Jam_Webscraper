#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
#define lli long long int
void process(std::istream& ip,std::ostream& op)
{
	int tc,n,x,res,i;
	ip>>tc;	
	lli ans,temp;
	int result=(1<<10)-1;
	for(x=1;x<=tc;x++)
	{
		res=0;
		ip>>n;		
		if(n==0)
			op<<"Case #"<<x<<": INSOMNIA\n";
		else
		{
			for(i=1;res!=result;i++)
			{
				temp=i*n;
				ans=temp;
				while(temp!=0 && res!=result)
				{
					res=res|(1<<(temp%10));
					temp=temp/10;
				}
				if(res==result)
					break;
			}
			op<<"Case #"<<x<<": "<<ans<<"\n";
		}
	}
}
int main()
{
	ifstream myfile ("A-large.in");
	ofstream file ("A-large op.in");
	process(myfile,file);
}