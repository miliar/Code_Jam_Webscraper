#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool is_majority (vector<int> senators)
{
	int sum=0;
	for (int i=0; i<senators.size(); i++)
	{
		sum+=senators[i];
	}
	for (int i=0; i<senators.size(); i++)
	{
		if (senators[i]>sum/2)
			return false;
	}
	return true;
}

void remove (vector<int>& senators)
{
	while (1)
	{
	
	int senators_left=0;
	for (int i=0; i<senators.size(); i++)
		senators_left+=senators[i];

	if (senators_left==3)
	{
		int count=0;
		string s;
                for (int i=0; i<senators.size(); i++)
                {
                        if (senators[i]>0)
			{
                                s+=((char)(i+'A'));
				senators[i]--;
				break;
			}
                }
                printf (" %s", s.c_str());
		if (!is_majority(senators))
                cout << "FALSE" << endl;
        }
	else if (senators_left<=2)
	{
		string s;
		for (int i=0; i<senators.size(); i++)
        	{
			if (senators[i]>0)
				s+=((char)(i+'A'));
		}
		printf (" %s", s.c_str());
		return;
	}
	else
	{

	int max_count=0;
	for (int i=0; i<senators.size(); i++)
	{
		if (senators[i]>max_count)
		{
			max_count=senators[i];
		}
	}

	string s;
	int count=0;
	for (int i=0; i<senators.size(); i++)
        {
                if (senators[i]==max_count)
                {
			count++;
			senators[i]--;
			s+=((char)(i+'A'));
                }
		if (count==2)
			break;
        }
	
	printf (" %s", s.c_str());
	if (!is_majority(senators))
		cout << "FALSE" << endl;
	}
	}
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++)
	{
		int parties;
		cin >> parties;
		vector<int> senators(parties);
		int sum=0;
		for (int p=0; p<parties; p++)
		{
			cin >> senators[p];
			sum+=senators[p];
		}
		printf ("Case #%d:",i+1);
		remove(senators);
		cout << endl;
	}
}

/* 1 1 1 
   1 1 2
   1 2 2
   1 2 3
   1 3 4
   1 4 4
   2 2 2
   2 2 3
   2 2 4
   2 3 3
   2 3 4
1 2 997
  1 4 4
  1 3 4
  1 3 3 
  1 2 3 
*/
