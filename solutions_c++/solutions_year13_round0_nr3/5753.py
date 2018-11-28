#include<fstream>
#include<iostream>
using namespace std;
bool check(long ll)
{
	long lt=ll;
	long tmp=0;
	while(true)
	{
		tmp+=ll%10;
		ll/=10;
		if(ll==0)
			break;
		tmp*=10;
	}
	if(tmp == lt) return true;
	else return false;
}
int main()
{
	/*unsigned c=1;
	for(int i=1;i<10;i++)
		for(int j=0;j<10;j++)
			{
				long long la=100*i+10*j+i;
				long long lb = 1000*i+100*j+10*j+i;
				long long ll=la*la;
				if(check(ll))
					cout<<la<<"@"<<ll<<" ";
				ll=lb*lb;
				if(check(ll))
					cout<<lb<<"@"<<ll<<" ";
			}
	return 0;
}*/
	fstream readfile("theIn.txt");
	fstream writefile("theOut.txt",ios::out) ;
	if(!readfile || !writefile)
		return -1;
	size_t c=0;
	readfile>>c;
	for(size_t i=0;i<c;i++)
	{
		long lg1,lg2;
		readfile>>lg1>>lg2;
		unsigned count=0;
		long bound1=sqrt(lg1);
		long bound2=sqrt(lg2);
		for(long j=bound1-1;j<=bound2+1;j++)
		{
			if(j*j>=lg1 && check(j)&& j*j<=lg2 && check(j*j))
				count++;
		}
		writefile<<"Case #"<<i+1<<": "<<count<<endl;
	}
	writefile.close();
	readfile.close();
}