#include <bits/stdc++.h> // Includes Every header file
using namespace std;
vector<int> shyness;

bool checkConstraint(int T){
	
	if(T>=1 && T<=100)
	{
		
		return true;
		
	}
	return false;
	
}


int main() {
	
	int T=0,k=0,a,Case=0;

	
	cin >> T;
	
	
	if(checkConstraint(T)){
		
		while(Case!=T)
		{
			shyness.clear();
			int people_standing=0,friends_needed=0;
			string str;
	
			cin >> k;
			
			cin >> str;
		
				shyness.reserve(str.size()); 
				
				transform(str.begin(), str.end(), back_inserter(shyness),
    			[](char c) {
        		return c - '0';
    			}
				);
			
			
			people_standing=shyness[0];
			
			for(int j=1;j<=k;j++)
			{
				if(people_standing < j && shyness[j]!=0)
				{
					friends_needed += (j-people_standing);
					people_standing += (shyness[j]+friends_needed);
				}
				else
				{
					people_standing += shyness[j];
				}
			}
	
			printf("Case #%d: %d\n",Case+1,friends_needed);
	
		
	
		Case++;
		}
	}
	
	return 0;
}
