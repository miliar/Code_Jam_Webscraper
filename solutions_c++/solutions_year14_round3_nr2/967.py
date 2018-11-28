#include<iostream>
#include<string.h>
#include<stdio.h>

#define max 100

using namespace std;

string s[max];	
int length[max];
int no_of_strings;
int no_of_sol;

void check_validity(int order[])
{

	bool occured[26];
	for(int i = 0; i < 26; i++)
			occured[i] = false;

	bool valid = true;
	char prev = s[order[0]][0];
	for(int i = 0; i < no_of_strings; i++)
	{
		for(int j = 0; j < s[order[i]].length(); j++)
		{
			int char_int = (int)(s[order[i]][j]) - 97;	
			if((s[order[i]][j] != prev) && (occured[char_int]))
			{
				valid = false;
				break;
			}	
			prev = s[order[i]][j];
			occured[char_int] = true;
		}	
		
		if(!valid)
			break;
	}

	if(valid)
		no_of_sol++;		
}


void make_permutation(int order[], int order_len, bool left[])
{

	if(order_len == no_of_strings)
		check_validity(order);
	else
	{
	int order_now[max];	
	bool left_now[max];	
	for(int i = 0; i < order_len; i++)
		order_now[i] = order[i];	

	for(int i = 0; i < no_of_strings; i++)
		left_now[i] = left[i];	

	bool prev;
	for(int i = 0; i < no_of_strings; i++)
	{
		if(left[i] == true)
		{
			order_now[order_len] = i;
			prev = left_now[i];
			left_now[i] = false;
			make_permutation(order_now, order_len+1, left_now);
			left_now[i] = prev;
		}
	}

	}			
}


int main()
{
	int no_of_tests;	
	cin>>no_of_tests;
	
	for(int t = 0; t < no_of_tests; t++)
	{
		no_of_sol = 0;	
		cin>>no_of_strings;
		//cout<<no_of_strings<<'\n';

		for(int i = 0; i < no_of_strings; i++)
		{	
			cin>>s[i];
			length[i] = s[i].length();
			//cout<<s[i]<<'\t'<<length[i]<<'\n';
		}	
				
		bool valid = true;
		for(int i = 0; i < no_of_strings; i++)
		{
			bool occured[26];
			for(int j = 0; j < 26; j++)
				occured[j] = false;

			char prev = s[i][0];
			for(int j = 0; j < s[i].length(); j++)
			{
				int char_int = (int)(s[i][j]) - 97;
				if((s[i][j] != prev) && (occured[char_int]))
				{
					valid = false;
					break;
				}	
				prev = s[i][j];
			}	
		
			if(!valid)
				break;
		}

		if(valid)
		{
			//cout<<"Valid!\n";
			int order[max];	
			bool left[max];
			for(int i = 0; i < no_of_strings; i++)
			{
				left[i] = true;
			}	

			make_permutation(order, 0, left);
		}	
		
		cout<<"Case #"<<t+1<<": "<<no_of_sol<<'\n';
	}	

	return 0;
}
