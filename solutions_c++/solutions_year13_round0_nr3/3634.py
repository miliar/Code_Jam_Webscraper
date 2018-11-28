#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef unsigned long long ll;
vector<ll> palindrome;

// Check if number is palindrome
bool isPalindrome(int x) {
  if (x < 0) return false;
  int div = 1;
  while (x / div >= 10) {
    div *= 10;
  }        
  while (x != 0) {
    int l = x / div;
    int r = x % 10;
    if (l != r) return false;
    x = (x % div) / 10;
    div /= 100;
  }
  return true;
}

// Build a list of all fair and squar palindromes
void buildList()
{
	for (long i=0; i<1000000; i++)
		if (isPalindrome(i) && isPalindrome(i*i))
			palindrome.push_back(i*i);
}

int main() {
	
	// Build a list of all the palindromes
	buildList();

	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int C;
	scanf("%d",&C);

	for (int test=1;test<=C;test++) {
		
		// Read the range
		ll start, end;
		cin >> start >> end;

		// Check all the palindrome numbers between this range
		int total=0;
		for (int i=0; i<palindrome.size(); i++)
			if (palindrome[i] >= start &&  palindrome[i] <= end)
				total++;

		cout << "Case #" << test << ": "  << total << endl;
	}
}
