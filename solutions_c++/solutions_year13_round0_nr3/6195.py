#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

bool isPalindrome(int pal);
void solve();

int main()
{
    int T;
    cin >> T;
    for(int i=1; i<=T; ++i)
    {
	cout << "Case #" << i << ": ";
	solve();
    }

    return 0;
}

void solve()
{
    int A,B;
    cin >> A >> B;

    double lower = sqrt(A);
    int low = static_cast<int>(lower);

    double upper = sqrt(B);
    int upp = static_cast<int>(upper) + 1;

    int counter = 0;

    for(int pal = low; pal<upp; ++pal)
    {
	int square = pal*pal;

	if(isPalindrome(pal) && isPalindrome(square) && square <= B && square >= A)
	{
	    counter++;
	}
    }
    cout << counter << endl;
}

bool isPalindrome(int pal)
{
    while(pal > 9)
    {
	int digits = static_cast<int>(log10(pal));

	int divideby = static_cast<int>(pow(10.0, digits));

	if(divideby < 10)
	{
	    divideby = 10;
	}

	if(pal % 10 != pal / divideby)
	    return false;

	pal %= divideby;
	pal /= 10;
    }

    return true;
}
