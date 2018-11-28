#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	 ifstream in("inp.txt");
	 ofstream op("op.txt");
	 int t;
	 in>>t;
	 for(int c=1;c<=t;c++)
	 {
	 	int max;
	 	in>>max;
	 	int ans=0,tot=0;
	 	for(int i=0;i<max+1;i++)
	 	{
	 	char t;
	 	in>>t;
	 	if(tot>=i)
	 	tot+=t-'0';
	 	else if(tot<i)
	 	{
	 	ans+=i-tot;
	 	tot=i;
	 	tot+=t-'0';
	 	
	 	}
	 	//cout<<"i = "<<i<<' '<<ans<<" "<<tot<<'\n';
	 	 	
	 	}
	 	op<<"Case #"<<c<<": "<<ans<<'\n';
	 }
}
