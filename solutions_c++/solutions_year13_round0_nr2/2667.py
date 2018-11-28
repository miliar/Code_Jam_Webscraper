#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <fstream>
#include <istream>

using namespace std;

void test_print_matrix(int **,int,int);
int** create_matrix_dynamic(int,int);
void deallocate_matrix(int**,int,int);
bool find_min(int**,int**,int,int,int&);

int main(int argc,char* argv[])
{
	ifstream infile;
        infile.open(argv[1]);
	string cases;
	getline(infile,cases);
	int count = atoi(cases.c_str());
	
		
	for(int i=0;i<count;i++) //loop for number of test cases
	{
		int rows,cols;
		char *temp;
		char *str;

		string line;
		getline(infile,line);	
	
		str = new char[line.length()];
                for (int i=0; i< line.length(); i++)
                {
                        str[i] = line[i];
                }

		temp = strtok (str," ");
                rows = (int)atoi(temp);
                temp = strtok (NULL," ");
                cols = (int)atoi(temp);

		//dynamically create 2D array	
    		int **desired_lawn = create_matrix_dynamic(rows,cols);
		int **output_lawn = create_matrix_dynamic(rows,cols);
	
		//for each row
		for(int i=0;i<rows;i++)
		{
			getline(infile,line);

			delete[] str;
			str = new char[line.length()];
                	for (int j=0; j<line.length();j++)
                	{
                        	str[j] = line[j];
                	}

			int col_count = 0;
			int max = 0;
			temp = strtok (str," ");

			while (temp != NULL)
  			{
				int current = (int) atoi(temp);
				desired_lawn[i][col_count] = current;
				if(current>max) max=current;
				col_count++;
    				temp = strtok (NULL, " ");
  			}

			//set the max for the entire row in output_lawn
			for(int k=0;k<cols;k++)
			{
				output_lawn[i][k]=max;
			}
		}

		bool possible = true;

		for(int i=0;i<cols;i++)
		{
			//find min in the column from desired lawn
			int min = 100;
			bool is_same;
			is_same = find_min(desired_lawn,output_lawn,rows,i,min);

			if(is_same) continue;

			//try to replace each element in the column with min, if it looks diferent than what is in the desired lawn break
			for(int j=0;j<rows;j++)
			{
				output_lawn[j][i] = min;
				if(output_lawn[j][i]!=desired_lawn[j][i])
				{
				 	possible = false;
					break;
				}
			}
			
			if(!possible)
				break;
		}

		string result;
		if(possible)
			result = "YES";
		else
			result = "NO";

		cout<<"Case #"<<i+1<<": "<<result<<endl;

		//test_print_matrix(desired_lawn,rows,cols);
		//cout<<endl<<endl;
		//test_print_matrix(output_lawn,rows,cols);
		//cout<<endl<<endl<<endl<<endl;

		//deallocate all dynamic stuff
		delete[] str;
		deallocate_matrix(desired_lawn,rows,cols);
		deallocate_matrix(output_lawn,rows,cols);

	}
}

//test method to print matrix
void test_print_matrix(int **matrix,int rows,int cols)
{
	for(int i=0;i<rows;i++)
	{
		for(int j=0;j<cols;j++)
		{
			cout<<matrix[i][j]<<" ";
		}
		cout<<endl;
	}
}

int** create_matrix_dynamic(int rows,int cols)
{
	int **matrix = new int*[rows];
        for (int count=0;count<rows;count++)
        {
        	matrix[count] = new int[cols];
        }

	return matrix;
}

void deallocate_matrix(int **matrix,int rows,int cols)
{
	for(int i=0;i<rows;i++)
	{
		delete[] matrix[i];
	}

	delete[] matrix;
}

bool find_min(int **desired_lawn,int **output_lawn,int rows,int current_column,int &min)
{
	bool is_same = true;
	min = 100;
	for(int i=0;i<rows;i++)
	{
		if(desired_lawn[i][current_column]<min) min = desired_lawn[i][current_column];
		if(desired_lawn[i][current_column]!=output_lawn[i][current_column]) is_same=false;
	}

	return is_same;
}
