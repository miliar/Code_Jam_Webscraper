//Programmer: Kyle Hatfield
//Email: ktbh4jc@gmail.com
//Date: April 10, 2015
//standing ovation
#include <iostream>
using namespace std;
int main()
{
	const int INIT_TO_ZERO = 0;
	int standing,friends, num_shows, max_shy, get_crowd = INIT_TO_ZERO;
	int * crowd;
	cin >> num_shows;
	for(int i=INIT_TO_ZERO; i<num_shows; i++)
	{
		cin >> max_shy;
		cin >> get_crowd;
		max_shy++;
		crowd=new int[max_shy];
		friends = INIT_TO_ZERO;
		for(int x = max_shy-1; x>=0; x--)
		{
			crowd[x]=get_crowd%10;
			get_crowd /=10;
		}
		standing = crowd[INIT_TO_ZERO];
		for (int z = 1; z < max_shy; z++)
		{
			if(friends+standing < z)
				friends = z - standing;
			standing = (standing + crowd[z]);
		}
		delete[]crowd;
		cout << "Case #" << i+1 << ": " << friends << endl;
		friends = INIT_TO_ZERO;
		standing = INIT_TO_ZERO;
		max_shy = INIT_TO_ZERO;
		get_crowd = INIT_TO_ZERO;
	}
	return INIT_TO_ZERO;
}