#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main() {
	// your code goes here
	
	int cases;
	cin>>cases;
	
	for(int q=0 ; q<cases ; q++)
	{
		int max_shyness;
		cin>>max_shyness;
		
		int shy_count[1001];
		string str_shy_count;
		cin>>str_shy_count;
		for(int i=0 ; i<=max_shyness ; i++)
		{
			shy_count[i] = str_shy_count[i]-'0';
		}
		int guys_needed = 0;
		
		for(int i=1 ; i<=max_shyness ; i++)
		{
			int total_standing = shy_count[i-1];
			//cout<<total_standing<<"*";
			int extras = max(i-total_standing, 0);
			guys_needed += extras;
			shy_count[i] = shy_count[i-1]+extras+shy_count[i];
		}
		cout<<"Case #"<<q+1<<": "<<guys_needed<<"\n";
	}
	
	return 0;
}