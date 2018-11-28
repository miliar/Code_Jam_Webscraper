//
//  main.cpp
//  google_code_jam
//

#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

using std::vector;
using std::cin;
using std::cout;

int main(int argc, const char * argv[])
{
	int num_test_cases = 0;
	
	cin>>num_test_cases;
	for (int test_case = 1; test_case <= num_test_cases; test_case++)	{
		
		int num_weights = 0;
		cin>>num_weights;
		
		vector<double> n_wt (num_weights, 0.0);
		vector<double> k_wt (num_weights, 0.0);
		
		for (int i =0 ; i<num_weights; i++)	{
			cin>>n_wt[i];
		}
		
		for (int i =0 ; i<num_weights; i++)	{
			cin>>k_wt[i];
		}
		
		std::sort(n_wt.begin(), n_wt.end());
		std::sort(k_wt.begin(), k_wt.end());
		
		int i = 0;
		int j = 0;
		vector<bool> k_war_wins(n_wt.size(), false);
		
		while(true)	{
			if (n_wt[i] < k_wt[j])	{
				k_war_wins[i] = true;
				i++;
			}
			
			j++;
			if (j >= k_wt.size())	{
				break;
			}
		}
		
		int n_war_count = 0;
		for (i =0 ; i < k_war_wins.size(); i++)	{
			if (k_war_wins[i] == false)
				n_war_count++;
		}
		
		i = n_wt.size() - 1;
		j = k_wt.size() - 1;
		int n_d_war_count = 0;
		
		while(true)	{
			if (n_wt[i] > k_wt[j])	{
				i--;
				n_d_war_count++;
			}
			j--;
			
			if (j < 0)
				break;
		}
		
		cout<<"Case #"<<test_case<<": "<<n_d_war_count<<" "<<n_war_count<<"\n";
	}
	
    return 0;
}

