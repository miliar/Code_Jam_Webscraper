#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
void process(std::istream& ip,std::ostream& op)
{
	int tc,arr[105],len,i,j,count,k,l,x;
	char s[105],ch;
	ip>>tc;
	for(x=1;x<=tc;x++)
	{
		ip>>s;
		len=strlen(s);
		i=len-1;
		count=0;
		while(i!=-1)
		{
			for(j=i;j!=-1 && s[j]!='-';j--);
			if(j==-1)
				break;
			count++;
			/*for(k=0,l=j;k<l;k++,l--)
			{
				ch=s[k];
				s[k]=s[l];
				s[l]=ch;
			}*/
			for(k=0;k<=j;k++)
			{
				if(s[k]=='-')
					s[k]='+';
				else
					s[k]='-';
			}
			i=j;
		}
		op<<"Case #"<<x<<": "<<count<<"\n";
	}
}
int main()
{
	//ifstream myfile ("B-small-attempt0.in");
	//ofstream file ("B-small-attempt0 op.in");
	ifstream myfile ("B-large.in");
	ofstream file ("B-large op.in");
	process(myfile,file);
}