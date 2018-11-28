#include<iostream>
#include<string>
using namespace std;
typedef long long ll;
ll calculatePeopleRequired(int sMax,string s)
{
	ll numOfPeopleStanding=0,numOfFriendsRequired=0;
	int i;
	
	for(i=0;i<=sMax;++i)
	{
		numOfPeopleStanding += (s[i]-'0');
		if(numOfPeopleStanding < i+1)
		{
				numOfFriendsRequired++; 
				numOfPeopleStanding++;
		}
		
	}
	return numOfFriendsRequired;
}

int main()
{
	int t;
	int sMax;
	string s;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		cin>>sMax;
		cin>>s;
		cout<<"Case #"<<i<<": "<<calculatePeopleRequired(sMax,s)<<endl;
	}
	return 0;
}
