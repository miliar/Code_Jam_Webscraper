#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
	ifstream in("D-large.in");
	ofstream out("out.txt");
	int caseCount;
	vector<int> answers;
	in>>caseCount;
	
	for(int i=0;i<caseCount;i++)
	{
		int n;
		in>>n;
		vector<double> first(n);
		vector<double> second(n);
		vector<double> first2(n);
		vector<double> second2(n);
		for(int i = 0 ; i < n; i++)
		{
			in>>first[i];
			first2[i] = first[i];
		}
		for(int i = 0 ; i < n; i++)
		{
			in>>second[i];
			second2[i] = second[i];
		}
		sort(first.begin(), first.end());
		sort(second.begin(), second.end());
		sort(first2.begin(), first2.end());
		sort(second2.begin(), second2.end());

		int score = 0;
		while(first.size()!=0)
		{
			if(first.back() > second.back())
			{
				vector<double>::iterator i = upper_bound(first.begin(), first.end(), second.front());
				first.erase(i);
				second.erase(second.begin());
				score++;
			}
			else
			{
				first.erase(first.begin());
				second.erase(second.end()-1);
			}
		}
		
		answers.push_back(score);
		score = 0;
		while(first2.size()!=0)
		{
			if(first2.back() > second2.back())
			{
				first2.erase(first2.end()-1);
				second2.erase(second2.begin());
				score++;
			}
			else
			{
				vector<double>::iterator i = upper_bound(second2.begin(), second2.end(), first2.front());
				first2.erase(first2.begin());
				second2.erase(i);
			}
		}
		answers.push_back(score);
		
	}

	for(int i=0;i<answers.size();i+=2)
	{
		out<<"Case #"<<i/2+1<<": "<<answers[i]<<" "<<answers[i+1]<<endl;
	}
	return 0;
}