#include "bits/stdc++.h"
using namespace std;
#define int long long

vector <string> strings;
void generate (string s, int left)
{
    if (left==1) strings.push_back(s+"1");
    else
    {
        generate (s+"0", left-1);
        generate (s+"1", left-1);
    }
}

int convert (string s, int b)
{
	int x = 0;
	for (int i=0; i<s.length(); i++)
		x+=llround(pow(b, s.length()-i-1))*(s[i]-'0');
	return x;
}

int pass (int n)
{
	if (n%2==0) return 2;
	for (int i=3; i<=1000; i+=2)
		if (n%i==0) return i;
	return 0;
}

signed main()
{
    vector <string> answers;
    generate("1", 15);
    bool jamcoin;
    for (auto i: strings)
    {
        for (int b=2; b<=10; b++)
        	if (not pass(convert(i, b))) goto next;
        answers.push_back(i);
        next:;
    }

	cout << "Case #1: \n";
    
    for (int i=0; i<50; i++)
    {
    	cout << answers[i] << ' ';
    	for (int b=2; b<=10; b++)
    	{
    		int number = convert(answers[i], b);
    		cout << pass(number) << ' ';
    	}
    	cout << '\n';
    }
 
}
