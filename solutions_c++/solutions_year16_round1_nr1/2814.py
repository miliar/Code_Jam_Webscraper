#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include<string.h>
using namespace std;
void process(std::istream& ip,std::ostream& op)
{
	int tc,x,i,n,k,l;
	char s[1005],t[1005],u[1005];	
	ip>>tc;
	for(x=1;x<=tc;x++)
	{
		op<<"Case #"<<x<<": ";
		ip>>s;
		t[0]=s[0];
		k=1; l=0;
		for(i=1;s[i]!='\0';i++)
		{
			if(s[i]>=t[k-1])
				t[k++]=s[i];
			else
				u[l++]=s[i];
		}
		t[k]='\0';
		u[l]='\0';
		op<<_strrev(t)<<u;
		op<<"\n";
	}
}
int main()
{
	ifstream myfile ("A-large.in");
	ofstream file ("output.in");
	process(myfile,file);
}