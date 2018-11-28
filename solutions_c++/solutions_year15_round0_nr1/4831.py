#include <iostream>
#include <vector>
#include <string>
#include <assert.h>

using namespace std;

void DoSolve(int test,int smax,const string& audience)
{
	//cout<<"dosolve: "<<smax<<" "<<audience<<endl;
	char shyness[smax + 1];
	assert(audience.length() == smax+1 );

	int numFriends = 0;
	int currStanding = audience[0] - '0';
	//int numaudience = audience[0] - '0';
	//cout<<"audience[0]: "<<currStanding<<endl;
	for (int current=1; current<audience.length(); ++current) {
		if (audience[current] == '0')
			continue;

		//numaudience += (audience[current] - '0');

		if (currStanding < current) {
			//cout<<"currStanding is less than current "<<currStanding<<" "<<current<<endl;
			int delta = current - currStanding;
			numFriends += delta;
			currStanding += (delta + (audience[current] - '0'));
			//cout<<"friends added: "<<delta<<endl;
		} else {
			//cout<<"currStanding is >= current"<<endl;
			currStanding += (audience[current] - '0');
		}
	} //for
	cout<<"Case #"<<test<<": "<<numFriends<<endl;
	//cout<<"audience: "<<numaudience<<endl;
	//cout<<"numstanding: "<<currStanding<<endl;
	//cout<<"------------------------------------"<<endl;
}


int main()
{
	int T;
	cin>>T;
	for (int test=1;test<=T;++test) {
		int smax;
		string audience;
		cin>>smax;
		cin>>audience;
		DoSolve(test, smax, audience);
	}

	return 0;
}
