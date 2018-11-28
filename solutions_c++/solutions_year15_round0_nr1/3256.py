#include <iostream>

using namespace std;

int array[1002];


void solve(int casenumber);

int main(int argc, char const *argv[])
{

	int cases;
	cin >> cases;
	
	for (int i = 0; i < cases; ++i)
	{

		solve(i+1);
	}

	return 0;
}

void solve(int casenumber){
	
	int maxshy;
	cin >> maxshy;
	string input;
	cin >> input;
	for (int i = 0; i <= maxshy; ++i)
	{
		array[i] = input[i] - '0';
	}

	int friends = 0;
	int friendsinvited = 0;
	for (int i = 0; i <= maxshy; ++i)
	{
		friends += array[i];
		if(friends <= i){
			friends++;
			friendsinvited++;
		}
	}
	cout << "Case #" << casenumber << ": " << friendsinvited << "\n";

}