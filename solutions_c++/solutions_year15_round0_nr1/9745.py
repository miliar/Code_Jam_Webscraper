#include <iostream>
using namespace std;
#define debug 0

char * str;

int minfriends(int smax)
{
	int friends=0;
	int currpeople=0;
	int i=0;
	int temp;
	
	for(i=0;i<=smax;i++)
	{
		if(currpeople>=i)
		{
		currpeople=currpeople+(str[i]-'0');
		if(debug) cout << currpeople << "\n";
		}
		else
		{
			temp = i-currpeople;
			friends=friends+temp;
			currpeople=currpeople+(str[i]-'0')+temp;
			if(debug) cout << currpeople << " " << friends << "\n";
		}
	}
	
	return friends;
}

void getinput(int smax)
{
	str = new char[smax+1];
	cin >> str;
}

int main()
{
	int T,smax,friends,i;
	cin >> T;
	for(i=1;i<=T;i++)
	{
		cin >> smax;
		getinput(smax);
		friends=minfriends(smax);
		cout << "Case #" << i << ": " << friends << "\n";
	}
	return 0;
}
