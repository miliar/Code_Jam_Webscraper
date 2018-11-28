#include<iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include<cstdlib>
#include<climits>
#define pi acos(-1.0)
using namespace std;

bool palindrome(int num)
{
	int n,digit, rev = 0;
     n = num;
     do
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);
     if (n == rev)
       return true;
     else
       return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d",&test);
	for (int CASE = 1; CASE <= test; CASE++)
	{
		int num1,num2,counter=0;
		cin>>num1>>num2;
		for(int i=num1;i<=num2;i++)
		{
			int y=pow(i,0.5);
			if(y*y==i)
			{
				if(palindrome(y) && palindrome(i))
					counter++;
			}
		}
		printf("Case #%d: %d\n",CASE,counter);
	}
}