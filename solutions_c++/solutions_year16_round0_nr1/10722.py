//Rohan Tiwari
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<cmath>
#include<map>
#include<cstring> 	//For memset.
#define endl '\n'
#define pb(n) push_back(n)
#define M 1000000007
typedef long long ll ;
using namespace std ;
int check ;
int flag[10] ;
void count(int x)
{
	while(x)
	{
		int d = x % 10 ;
		x /= 10 ;
		if(flag[d] == 0)
		{
			flag[d] = 1 ;
			check++ ;
		}
	}
	return ;
}
int main()
{
	ios_base::sync_with_stdio(false) ;
	int T ;
	cin >> T ;
	for(int i = 1 ; i <= T ; i++)
	{
		int N , stop = 0 , index = 1 ;
		cin >> N ;
		while(stop == 0)
		{
			if(check == 10)
				stop = 1 ;
			else if(index >= 200)
				stop = 1 ;
			else 
				count(index * N) ;
			index++ ;
		}
		cout << "Case #" << i << ": " ; 
		if(index < 200)
			cout << (index - 2) * N << endl ;
		else
			cout << "INSOMNIA" << endl ;
		for(int i = 0 ; i <= 9 ; i++)
			flag[i] = 0 ;
		check = 0 ;
	}
	return 0 ;
}

