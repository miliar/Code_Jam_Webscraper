#include <iostream>
#include <string.h>

using namespace std;

int noFriends(int smax, int *arr)
{
	int ans = 0;
	int indexSum = arr[0];
	
	for (unsigned int i = 1; i < smax+1; i += 1) {
		if (indexSum < i) {
			arr[i-1] += (i - indexSum);
			ans += (i - indexSum);
			indexSum += (i - indexSum);
		}
		indexSum += arr[i];
	}
	
	return ans;
}

int main (int argc, char const* argv[])
{
	int t, caseno = 1, smax;
	cin >> t;
	
	int arr[1005];
	
	while (t--) {
		bzero(arr, sizeof arr);
		cin >> smax;
		char temp;
		
		for (unsigned int i = 0; i < smax+1; i += 1) {
			cin >> temp;
			arr[i] = temp - '0';
		}
		
		cout << "Case #" << caseno++ << ": " << noFriends(smax, arr) << endl;
	}
	
	return 0;
}
