#include <iostream>

using namespace std;

int array[1000];

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
	int n;
	cin >> n;

	for (int i = 0; i < n; ++i)
	{
		cin >> array[i];
	}

	int biggest = 0;
	for (int i = 0; i < n; ++i)
	{
		if(array[i] > biggest){
			biggest = array[i];
		}
	}

	int cumul, temp;
	int bestTime = 9999999;

	for (int i = biggest; i > 0; --i)
	{
		cumul = 0;
		for (int j = 0; j < n; ++j)
				{
					if(array[j] > i){
						cumul += array[j]/i;
						if(array[j]%i == 0){
							cumul--;
						}
					}	
				}
		if (cumul+i < bestTime){
			bestTime = cumul+i;
		}		
	}
	cout << "Case #" << casenumber << ": " << bestTime << "\n";

}