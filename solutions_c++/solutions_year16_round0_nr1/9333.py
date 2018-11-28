//It's all about what U BELIEVE
#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>
#include<cstring>
#include<map>
#include<tuple>
#include<cmath>
#include<set>
#define fo(y , z) for(ull y = 0 ; y < z ; y++)
#define ui unsigned int
#define ull unsigned long long
#define pb push_back
#define gcu getchar_unlocked
#define wtm while(t--)
#define non if(!n)break;
#define frop freopen("/home/ebram96/Downloads/A-large.in" , "r" , stdin);	freopen("/home/ebram96/Desktop/out" , "w" , stdout);
using namespace std;
bool bin(string a , string b){return a > b;}
bool bin(int a , int b){return a > b;}
bool bin(ull a , ull b){return a > b;}
int main()
{
	//frop
	unsigned long long t , n , temp , bin , result;
	scanf("%I64llu" , &t);
	fo(y , t)
	{
		scanf("%I64llu" , &n);
		if(!n)
		{
			printf("Case #%llu: INSOMNIA\n" , y+1);
			continue;
		}
		bin = 0;
		for(ull multiply = 1; bin != 1023 ; multiply++)
		{
			temp = n*multiply;
			result = temp;
			while(temp)
			{
				bin |= (1<<(temp%10));
				temp /= 10;
			}
		}
		printf("Case #%llu: %llu\n" , y+1 , result);
	}
}
