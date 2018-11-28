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
	
	int N , warW , dwarW;
	vector<double> nao , ken;
	bool usedN[1001] , usedK[1001] , win;
	double tempd , np , kp;
	int i , j , smallj;
	
	for(int _i = 1 ; _i <= __A ; _i++)
	{
		printf("Case #%d: " , _i);
		nao.clear();
		ken.clear();
		scanf("%d" , &N);
		for(i=0 ; i<N ; i++)
		{
			scanf("%lf" , &tempd);
			nao.pb(tempd);
			usedN[i] = 0;
		}
		
		for(i=0 ; i<N ; i++)
		{
			scanf("%lf" , &tempd);
			ken.pb(tempd);
			usedK[i] = 0;
		}
		
		sort(nao.begin() , nao.end());
		sort(ken.begin() , ken.end());
		
		//play war
		warW = 0;
		for(i=0 ; i<N ; i++)
		{
			//nao plays smallest available
			win = true;
			smallj = N;
			for(j=0 ; j<N ; j++)
			{
				if(usedK[j])
					continue;
					
				smallj = min(smallj , j);
				if(ken[j] > nao[i])
				{
					win = false;
					usedK[j] = true;
					break;
				}
			}
			if(win)
			{
				//ken is loosing this round so uses the smallest he has
				usedK[smallj] = true;
				warW++;
			}
		}
		
		//play Deceitful War
		for(i=0 ; i<N ; i++)
			usedK[i] = false;

		dwarW = 0;
		for(i=0 ; i<N ; i++)
		{
			//nao plays smallest available
			//find the smallest available to ken
			for(j=0 ; j<N ; j++)
			{	
				if(!usedK[j])
					break;
			}
			if(nao[i] > ken[j])
			{
				usedK[j] = true;
				dwarW++;
				continue;
			}
			//else
			//find the largest available to ken and waste it.
			for(j=N-1 ; j >= 0 ; j--)
			{	
				if(!usedK[j])
					break;
			}
			usedK[j] = true;
			
		}
		printf("%d %d\n" , dwarW , warW);
	}
	return 0;
}
