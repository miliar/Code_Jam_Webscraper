#include<iostream>
#include<math.h>
using namespace std;
int main()
{
//Initializing Values to take as Input
int num,k,c,s,i;
cin>>num;

//Loop for 'num' cases
for(int loop=0;loop < num;loop++)
{	
	cin>>k>>c>>s;
	//Total number of tiles : k^c
	cout<<"Case #"<<loop+1<<": ";
	for(i = 1;i <= s;i++)
	{
		cout<<i<<" ";
	}
	cout<<endl;
}
return 0;

}
