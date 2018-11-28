#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <fstream>
#include <istream>
#include <sstream>
#include <string.h>
#include <set>
#include <math.h>

using namespace std;

bool is_palindrome(char*,int);
set<unsigned long long int> get_fair_and_square(unsigned long long int);

int main(int argc,char* argv[])
{
	ifstream infile;
        infile.open(argv[1]);
	string cases;
	getline(infile,cases);
	int count = atoi(cases.c_str());
	//unsigned long long int max = 1000;
	unsigned long long int max = 100000000000000;
	set<unsigned long long int> fair_and_square = get_fair_and_square(max);
		
	for(int i=0;i<count;i++) //loop for number of test cases
	{

		unsigned long long int lower_bound,upper_bound;

                string line,u_b_s,l_b_s;
                getline(infile,line);

		unsigned long long int j=0;
                for (j=0; j< line.length(); j++)
                {
			if(line[j]==' ') break;
			l_b_s.push_back(line[j]);
                }

		for(unsigned long long int k=j+1;k<line.length();k++)
		{
			u_b_s.push_back(line[k]);
		}


		stringstream ss1(l_b_s);
		ss1>>lower_bound;

		stringstream ss2(u_b_s);
		ss2>>upper_bound;

		int count = 0;
		/*for(unsigned long long int l=lower_bound;l<=upper_bound;l++)
		{
			if(fair_and_square.count(l)>0) count++;
		}*/

		set<unsigned long long int>::iterator set_iterator;
		for(set_iterator = fair_and_square.begin();set_iterator!= fair_and_square.end();set_iterator++)
		{
			if(*set_iterator>upper_bound) break;
			if(*set_iterator>=lower_bound && *set_iterator<=upper_bound) count++;
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
}

set<unsigned long long int> get_fair_and_square(unsigned long long int max)
{
	set<unsigned long long int> fair_and_square;

	unsigned long long int i;

        for(i=1;i<=max;i++)
        {
                unsigned long long int max_square = i*i;
                if(max_square>max) break;

                char max_s[20];
                char max_square_s[20];

                sprintf(max_s,"%llu",i);
                sprintf(max_square_s,"%llu",max_square);

                if(is_palindrome(max_s,strlen(max_s)) && is_palindrome(max_square_s,strlen(max_square_s)) )
                {
			//cout<<max_square<<endl;
                        fair_and_square.insert(max_square);
                }
        }

	return fair_and_square;
}

bool is_palindrome(char *input,int length)
{
        int l = 0;
        int h = length-1;

        while(h>l)
        {
                if(input[h]!=input[l]) return false;
                h--;
                l++;
        }

        return true;
}

