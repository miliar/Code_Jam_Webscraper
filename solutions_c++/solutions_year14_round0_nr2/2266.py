#include <cstdio>
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <string>
#include <cstring>

using namespace std;

#define DEBUG 0
#define all(C) (C).begin() , (C).end()
#define tr(C , it) for(typeof((C).begin()) it = (C).begin() ; it != (C).end() ; it++)
#define present(C , key) ((C).find(key) != (C).end())
#define cpresent(C , key) (find(all(C) , key) != (C).end())
#define sz(a) int((a).size())
#define pb push_back
#define MOD 1000000007


typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int , int> PI;

int main()
{
	int __A;
	scanf("%d" , &__A);
	
	double C , F , X , crate , nrate , t1 , t2 , t3 , ans;
	for(int _i = 1 ; _i <= __A ; _i++)
	{
		printf("Case #%d: " , _i);
		
		scanf("%lf %lf %lf" , &C , &F , &X);
		//printf("%lf %lf %lf\n" , C , F , X);
		crate = 2;
		ans = 0;
		t1 = X/crate;
		t2 = C/crate;
		nrate = crate + F;
		t3 = X/nrate;
		//printf("%lf %lf %lf\n" , t1 , t2 , t3);
		while((t2 + t3) < t1)
		{
			//printf("%lf %lf %lf\n" , t1 , t2 , t3);
			ans += t2;
			t1 = t3;
			crate = nrate;
			t2 = C/crate;
			nrate = crate + F;
			t3 = X/nrate;
		}
		
		ans += t1;
		printf("%.7lf\n" , ans);
	}
	return 0;
}
