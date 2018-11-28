#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;


void Solving(int test)
{
	int A, B, C;
	cin >> A >> B >> C;
	int ans = 0;
	for(int X = 0; X < A; ++X)
		for(int Y = 0; Y < B; ++Y)
		{int Z = X&Y;
	if (Z < C) ans++;}
	cout << "Case #" << test <<": " << ans << "\n"; 
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;

	for(int i = 1; i<= T; ++i)
	{
		Solving(i);
	}

	

}