//It's all about what U BELIEVE
#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>
#include<cstring>
#include<map>
//#include<tuple>
#include<cmath>
#include<set>
#define fo(y , z) for(int y = 0 ; y < z ; y++)
#define ui unsigned int
#define ull unsigned long long
#define pb push_back
#define gcu getchar_unlocked
#define wtm while(t--)
#define non if(!n)break;
#define frop freopen("/home/ebram96/Desktop/in" , "r" , stdin);	freopen("/home/ebram96/Desktop/out" , "w" , stdout);
using namespace std;
bool bin(string a , string b){return a > b;}
bool bin(int a , int b){return a > b;}
bool bin(ull a , ull b){return a > b;}
int main()
{
	//frop
	int t , sectors;
	char input_c , prev_c;
	scanf("%d\n" , &t);
	fo(y , t)
	{
		sectors = 1;
		prev_c = gcu();
		while(1)
		{
			input_c = gcu();
			if(input_c != '-' && input_c != '+')break;
			if(input_c != prev_c)
				prev_c = input_c , sectors++;
		}
		printf("Case #%d: %d\n" , y+1 , prev_c == '-' ? sectors : sectors-1);
	}
}
