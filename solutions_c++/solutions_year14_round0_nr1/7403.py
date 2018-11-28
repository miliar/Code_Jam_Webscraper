#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve();

int main()
{
    int T;
    cin >> T;
    for(int i=1; i<=T; ++i)
    {
	int res = solve();

	cout << "Case #" << i << ": ";

	if(res > 0)
	{
	    cout << res << endl;
	}
	else if(res == 0) /* No answer */
	{
	    cout << "Volunteer cheated!" << endl;
	}
	else
	{
	    cout << "Bad magician!" << endl;
	}
    }

    return 0;
}


int solve()
{
    vector<int> possible1;

    int r;
    cin >> r;

    for(int i=1; i<=4; ++i)
    {
	int tmp;

	for(int j=0; j<4; ++j)
	{
	    cin >> tmp;
	    if(i == r)
		possible1.push_back(tmp);
	}
	
    }


    vector<int> possible2;

    cin >> r;

    for(int i=1; i<=4; ++i)
    {
	int tmp;

	for(int j=0; j<4; ++j)
	{
	    cin >> tmp;
	    if(i == r && find(possible1.begin(), possible1.end(), tmp) != possible1.end())
	    {
		possible2.push_back(tmp);
	    }
	}
    }

    if(possible2.size() > 1)
	return -1;
    if(possible2.size() == 0)
	return 0;
    else
	return possible2[0];

}
