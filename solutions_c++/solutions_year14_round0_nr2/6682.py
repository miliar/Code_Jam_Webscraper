/*--------------------- Author - Akshit ----------------------*/

#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<stack>
#include<list>
#include<queue>
#include<cstdlib>
#include<numeric>
#include<set>
#include<map>
#include<deque>
#include<climits>
#include<cassert>
#include<cctype>
#include<ctime>
#include<iterator>
#include<iomanip>
#include<functional>
#include<fstream>
#include<ostream>
#include<istream>

using namespace std;

#define sf(n)                scanf("%d",&n) 
#define pf(n)                printf("%d",n)          
#define pfln(n)              printf("%d\n",n)         

#define vi                   vector <int > 
#define pb                   push_back()
#define debug(in)             printf("n = %d\n",n)
#define PI 3.14159265358979
#define LL 1000000007

int main()
{
	std::ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	double C,F,X;
	int no = 1;
	while (no<=t){
		cin>>C>>F>>X;
		double win = 0.0;
		double rate = 2.0;
		while ((X/rate) > ((C/rate) + (X/(rate+F)))){
			//double timedirect = X/rate;
			//double timefarm = (C/rate) + (X/(rate+F));
			win+=(C/rate);
			rate+=F;
		}
		win+=(X/rate);
		printf("Case #%d: %.7f\n",no,win);
		no++;
	}
	return 0;
}
