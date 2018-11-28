#include <stdio.h>
#include <conio.h>
#include <climits>
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;
typedef vector<float>::iterator vit;
typedef vector<float>::reverse_iterator rvit;

void solve(vector<float> naomi, vector<float> ken, int &war, int &dec_war)
{
	sort(naomi.begin(), naomi.end());
	sort(ken.begin(), ken.end());
	reverse(naomi.begin(), naomi.end());

	int n = ken.size();
	int i =0, startKen = 0, endKen = n-1;

	//war
	while( i< n&& startKen <= endKen)
	{
		if(naomi[i] > ken[startKen] && naomi[i] > ken[endKen])
		{
			startKen++;
			war++;
		}
		else
		{
			endKen--;
		}
		i++;
	}

	//dec_war
	reverse(naomi.begin(), naomi.end());

	int j = 0;
	int endNaomi = naomi.size() -1,  startNaomi = 0;
	startKen = 0;
	endKen = ken.size()-1;

	while(startNaomi <= endNaomi && startKen <= endKen)
	{
		if(naomi[startNaomi] < ken[startKen])
		{
			startNaomi++;
			endKen--;
		}
		else
		{
			dec_war++;
			startNaomi++;
			startKen++;
		}
	}

}


int main()
{
	
	unsigned short int testcases;
	int n;
	float t;
	
    cin >> testcases;
	
    for(int i=1; i <= testcases; i++) 
	{ 
		cin >> n;
		vector<float> naomi, ken;

        for(int x = 0; x<n; x++)
		{
			cin >> t ;
			naomi.push_back(t);			
		}

		 for(int x = 0; x<n; x++)
		{
			cin >> t ;
			ken.push_back(t);			
		}
		 	
		int war = 0, dec_war = 0;
		solve(naomi, ken, war, dec_war);
		printf("Case #%d: %d %d\n", i, dec_war, war);
    }

	getch();
}
