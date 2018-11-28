#include <iostream>
#include <cstring>
#include <climits>
using namespace std;

bool checkValid(int *arr, int N, int rem)
{
	for(int i=0; i<N; i++)
		if (arr[i] < 0 || arr[i] > rem/2)
			return false;
	return true;
}

bool one(int *arr, int N, int rem)
{
	if ( rem < 1 )  return false;
	for(int i=0; i<N; i++) {
		arr[i] -= 1;
		if (checkValid(arr, N, rem-1)) {
			cout << (char)(i + 'A');	
			return true;
		}
		arr[i] += 1;
	}
	return false;
}

bool two(int *arr, int N, int rem)
{
	if ( rem < 2 ) return false;
	for(int i=0; i<N; i++) 
	{
		arr[i] -= 2;
		if(checkValid(arr, N, rem-2)) {
			cout << (char)(i + 'A');
			return true;
		}
		arr[i] += 2; 
	}
	return false;
}

void three(int *arr, int N, int rem)
{
	int mx=INT_MIN, smx=INT_MIN;
	for(int i=0; i<N; i++)
	{
		if(smx < arr[i]) { smx = i; }
		if(mx < arr[smx])  {
			int temp = smx;
			smx = mx;
			mx = temp;
		}
	}
	arr[mx]--;
	arr[smx]--;
	cout << (char)(mx + 'A') << (char)(smx + 'A');
}

void solve(int *arr, int N, int &rem)
{
	if (rem <= 0 ) return;
	if (one(arr, N, rem)) rem--;
	else if (two(arr, N, rem)) rem -= 2;
	else
	{
		three(arr, N, rem);
		rem -= 2;
	}
	if ( rem )  {
		cout << " ";
		solve(arr, N, rem);
	}
}

int main()
{
	int T, N;
	cin >> T;
	for(int kases=1; kases<=T; kases++)
	{
		cin >> N;
		int arr[N], rem=0;
		memset(arr, 0, sizeof(N));
		for(int i=0; i<N; i++) {
			cin >> arr[i];
			rem += arr[i];
		}
		cout << "case #" << kases << ": ";
		solve(arr, N, rem);
		cout << endl;
	}
	return 0;
}