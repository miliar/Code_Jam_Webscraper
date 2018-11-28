#include<iostream>
#include <string>
#include <cstdio>
#include <vector>



using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

	int T; // no. of test cases
	int mSh ;  // max shyness level
	string sh;
	cin>>T;
	for (int i=1; i<= T; i++)
	{ 
		
		cin>> mSh >> sh;
		if ( mSh == 0) cout << "Case #"<<i<<": 0"<<endl;
		else
		{   vector<int> S;   // to store no. of persons  for every shyness level 
			for ( int j=0; j<mSh+1; j++)
			{ 
				S.push_back( sh[j]-'0');

			}

			int  noOFfriends =0; 
			int sum = S[0]; // no of people who stood, initially = no of people who have shyness =0
			for ( int z=1; z<mSh+1; z++)
			{

				if( S[z] !=0)
				{
					if (z>sum  ) 
					{
						noOFfriends = noOFfriends+ ( z- sum);
						sum = z;
					}
				}

				sum = sum + S[z];
			}

			cout << "Case #"<<i<<": "<< noOFfriends<<endl;
		}


	}


	return 0;
}