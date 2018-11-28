// counting_sheep.cpp : Defines the entry point for the console application.
//

#include "StdAfx.h"

#include <iostream>
#include <vector>



using namespace std;


void check_number(const int a, vector<int> &b)
{
	bool has_number = false;

	if(0==b.size())
	{
		b.push_back(a);
		has_number = false;
	}

	else
	{
		for(int i=0; i<b.size(); i++)
		{
			if(a == b[i])
			{
				has_number = true;
				break;
			}
		}

		if(has_number == false)
		{
			b.push_back(a);
		}
	}
}

int main(int argc, char* argv[])
{
	
	int num;

	vector<int> sleep_collection;

	int sleep_number =0;

	int t;

	int temp_num = 0;

	FILE *f_in = fopen("A-large.in","r");
	FILE *f_out = fopen("A-large_out.txt","w");

	if(feof(f_in))
	{
		printf("Input file is empty!\n");
		return -1;
	}

	if(feof(f_out))
	{
		printf("There is no output file!\n");
		return -1;
	}

	fscanf(f_in, "%d\n", &t);

	for(int i=0; i<t; i++)
	{
		fscanf(f_in, "%d\n", &num);

		
		if( 0==num )
		{
			fprintf(f_out, "Case #%d: INSOMNIA\n", i+1);
			printf("Case #%d: INSOMNIA\n", i+1);
			continue;
		}
		else
		{
			int j=1;
			int reminder = 0;
			bool sleeping = false;
			do
			{
				temp_num = num*j;

				while(temp_num!=0)
				{
					reminder = temp_num%10;

					temp_num = temp_num/10;

					check_number(reminder, sleep_collection);

					if(sleep_collection.size() == 10)
					{
						sleep_number = num*j;

						fprintf(f_out, "Case #%d: %d\n", i+1, sleep_number);
						printf("Case #%d: %d\n", i+1, sleep_number);

						sleep_collection.erase(sleep_collection.begin(), sleep_collection.end());

						sleeping = true;
						break;
					}
				}

				j++;
			}while(sleeping == false);

			sleep_collection.erase(sleep_collection.begin(), sleep_collection.end());

		}
		
	}
	
	fclose(f_in);
	fclose(f_out);


	return 0;
}

