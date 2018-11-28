#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

bool isPalindrome(int x) 
{
        if(x<0)
            return false;
        string s1, s2;
        while(x>0)
        {
            s1 += x%10;
            x /= 10;
        }
        s2 = s1;
        reverse(s1.begin(), s1.end());
		if(strcmp(s1.c_str(), s2.c_str()) == 0)
            return true;
        else
            return false;
}

int main()
{
	
	//freopen("input.txt", "r", stdin);
	//freopen("C.txt", "w", stdout);
	int n, a, b;
	cin>>n;
	for(int k=0; k<n; k++)
	{
		int count = 0;
		int issqpa = 1;
		int sqr;
		cin>>a>>b;
		for(int i=a; i<=b; i++)
		{
			issqpa = 1;
			if(!isPalindrome(i))
			{
				issqpa = 0;
				continue;
			}
			sqr = (int)sqrt((double)i);
			if(sqr * sqr != i)
				issqpa = 0;
			else if(!isPalindrome(sqr))
				issqpa = 0;
			if(issqpa)
				count++;
		}
		printf("Case #%d: %d\n", k+1, count);
	}

	//fclose(stdout);
	//fclose(stdin);
	return 0;
}

