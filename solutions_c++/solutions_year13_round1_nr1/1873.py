#include<iostream>
#include<math.h>
using namespace std;

int main()
{

int t=0;
cin>>t;
for(int ctr=1;ctr<=t;ctr++)
{
	cout<<"Case #"<<ctr<<": ";

	long long r=0;
	long long t=0;
	long long wR=0;
	long long bR=0;
	long long wA=0;
	long long bA=0;
	long long usedP=0;
	long long count=0;

	cin>>r;
	cin>>t;

	wR=r;
	bR=wR+1;

	while(usedP<t)
	{
		wA=(long long)pow(wR,2);
		//cout<<"wA == "<<wA;
		bA=(long long)pow(bR,2);
		//cout<<"bA == "<<bA;

		count++;


		usedP=usedP + (bA-wA);
		//cout<<"UsedP = "<<usedP<<endl;
		wR=bR+1;
		bR=wR+1;

		if(usedP>t)
			--count;

	}
	cout<<count<<endl;



}//t, for loop
return 0;

}
