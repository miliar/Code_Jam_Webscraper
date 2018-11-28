#include <fstream>
#include <string>

using namespace std;

ifstream cin("D-small-attempt0.in");
ofstream cout("artwork.out");

int T,K,C,S;

int main()
{
	cin>>T;
	for(int o=1; o<=T; o++)
	{
		cin>>K>>C>>S;
		{
			cout<<"case #"<<o<<": ";
	        for(int i=1; i<=S; i++)
	           cout<<i<<" ";
	        cout<<endl;
	    }
    }
return 0;
	
}
