#include<iostream>
#include<math.h>
using namespace std;
int main()
{
//Initializing Values to take as Input
int num,k,c,s,i,j,l;
cin>>num;

//Loop for 'num' cases
for(int loop=0;loop < num;loop++)
{
	cin>>k>>c>>s;
	//Case of k=s(Trivial)
	cout<<"Case #"<<loop+1<<": ";
	if(k == s)
	{
		for(i = 1; i <= s; i++)
		{
			cout<<i<<" ";
		}
	}
	cout<<endl;
}
return 0;
}
