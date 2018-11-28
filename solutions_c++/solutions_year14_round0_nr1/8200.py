#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <istream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void fetch_row(string,vector<int> &,int);
vector<int> vector_intersection(vector<int>,vector<int>);

int main(int argc,char* argv[])
{
	ifstream infile;
        infile.open(argv[1]);
	string cases;
	getline(infile,cases);
	int count = atoi(cases.c_str());
	
	for(int tc_i=0;tc_i<count;tc_i++)
	{
	 	cout<<"Case #"<<tc_i+1<<": ";
		string row_s;
		getline(infile,row_s);
		int row_i = atoi(row_s.c_str());
		
		vector<int> row_first;
		int row_iterator=1;
        	string row_cards;
        	while(row_iterator<=row_i)
        	{
                	getline(infile,row_cards);
                	row_iterator++;
        	}
		fetch_row(row_cards,row_first,row_i);

		//skip lines
		while(row_iterator<=4)
                {
                        getline(infile,row_cards);
                        row_iterator++;
                }

		row_iterator=1;
		getline(infile,row_s);
                row_i = atoi(row_s.c_str());
	
		vector<int> row_second;
		while(row_iterator<=row_i)
                {
                        getline(infile,row_cards);
                        row_iterator++;
                }
                fetch_row(row_cards,row_second,row_i);

		//skip lines
                while(row_iterator<=4)
                {
                        getline(infile,row_cards);
                        row_iterator++;
                }	

		sort(row_first.begin(),row_first.end());
		sort(row_second.begin(),row_second.end());

		vector<int> intersection_vector = vector_intersection(row_first,row_second);
		int intersection_size = intersection_vector.size();
		if(intersection_size==1)
		{
			cout<<intersection_vector[0]<<endl;
		}
		else if(intersection_size>1)
		{
			cout<<"Bad magician!"<<endl;
		}
		else if(intersection_size==0)
		{
			cout<<"Volunteer cheated!"<<endl;
		}
	}
		
}

void fetch_row(string row_cards,vector<int> &row,int row_i)
{
        char *temp;
        char *str;

        str = new char[row_cards.length()];
        for (int i2=0; i2< row_cards.length(); i2++)
        {
        	str[i2] = row_cards[i2];
        }
        
	temp = strtok (str," ");
        row.push_back((int)atoi(temp));

        for(int i=1;i<=3;i++)
        {
        	temp = strtok (NULL," ");
                row.push_back((int)atoi(temp));
        }
}

vector<int> vector_intersection(vector<int> row_first,vector<int> row_second)
{
	vector<int> intersection_vector;

	vector<int>::iterator rf_i = row_first.begin();
	vector<int>::iterator rs_i = row_second.begin();

	while(rf_i!=row_first.end() && rs_i!=row_second.end())
	{
		if(*rf_i == *rs_i)
		{
			intersection_vector.push_back(*rf_i);
			rf_i++;
			rs_i++;
		}
		else if(*rf_i<*rs_i)
		{
			rf_i++;
		}
		else
		{
			rs_i++;
		}
	}
	return intersection_vector;
}
	

