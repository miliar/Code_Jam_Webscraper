#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <fstream>    // make obj and use it
#include <utility>
using namespace std;
int main()
{
	
		ifstream input("./testcase files/standing ovation/A-large.in");
		ofstream output("./output files/standing ovation/A-large.txt");

	
	int test_cases=0;
	input>>test_cases;
	for(int tt=1;tt<=test_cases;tt++)
	{
		int S;
		string audience;
		
		input>>S>>audience;
		
		int currentStanding=0;
		int requiredStanding=0;
		currentStanding+= audience[0]-'0';
		

		int temp=0;
		int audienceSize = audience.length();
				
		/*
The kth digit of this string (counting starting from 0) represents how many people in the audience have shyness level k. 
For example, the string "409" would mean that there were four audience members with Si = 0 and nine audience members with
 Si = 2 (and none with Si = 1 or any other value). 
Note that there will initially always be between 0 and 9 people with each shyness level.

Input 

4
4 11111
1 09
5 110011
0 1

Output

Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0


*/		
		

		for(int i=1;i<audienceSize;i++)
		{
			int people = (int)(audience[i]-'0');
			int level =  i;
			
			if(i>S) 
			continue;
			if(currentStanding>=i)
			{
				currentStanding+=people;
			}
			else if(people!=0)
			{
				temp = i - currentStanding;
				requiredStanding +=temp;
				currentStanding +=temp+people;
			}
		}
		temp= (S-currentStanding);
		if( temp>=0)
		{
			requiredStanding+=temp;
		}
		
		output<<"Case #"<<tt<<": "<<requiredStanding<<endl;
	}
	
return 0;
}

