#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <iterator>
#include <cstring>
#include <climits>
#include <cstdlib>
#include <cstdio>

using namespace std;

const int dim = 4;
int Arr[dim][dim] = {0};
string inFile = "A-small-attempt0.in";
string outFile = "A-small-attempt0.out";
FILE* in = NULL;
FILE* out = NULL;

string judge(const set<int>& row1, const set<int>& row2)
{
	set<int> interSet;
	set_intersection(row1.begin(), row1.end(), row2.begin(), row2.end(), inserter(interSet, interSet.begin()));
	/*for(set<int>::iterator iter=interSet.begin(); iter!=interSet.end(); iter++){
		cout<<*iter<<"  ";
	}
	cout<<endl;*/
	switch(interSet.size())
	{
	case 0:
		return "Volunteer cheated!";
	case 1:
		char arr[10];
		itoa(*(interSet.begin()), arr, 10);
		return arr;
	default:
		return "Bad magician!";
	}
}

int main()
{
	if( !( in = fopen(inFile.c_str(), "r") ) )
		exit(-1);
	if( !( out= fopen(outFile.c_str(), "w") ) ){
		fclose(in);
		exit(-1);
	}

    int T;
	fscanf(in, "%d", &T);
	int pos1, pos2;
	set<int> row1, row2;
	string result;
	for(int t=0; t<T; t++)
	{
		row1.clear();
		row2.clear();
		fscanf(in, "%d", &pos1);
		for(int i=0; i<dim; i++){
			for(int j=0; j<dim; j++){
				fscanf(in, "%d", &Arr[i][j]);
			}
		}
		for(int j=0; j<dim; j++){
			row1.insert(Arr[pos1-1][j]);
		}
		fscanf(in, "%d", &pos2);
		for(int i=0; i<dim; i++){
			for(int j=0; j<dim; j++){
				fscanf(in, "%d", &Arr[i][j]);
			}
		}
		for(int j=0; j<dim; j++){
			row2.insert(Arr[pos2-1][j]);
		}
		/*set<int>::iterator iter;
		cout<<"row1's contents:"<<endl;
		for(iter=row1.begin(); iter!=row1.end(); iter++){
			cout<<*iter<<"  ";
		}
		cout<<"\nrow2's contents:"<<endl;
		for(iter=row2.begin(); iter!=row2.end(); iter++){
			cout<<*iter<<" ";
		}
		cout<<endl;*/
		result = judge(row1, row2);
		fprintf(out, "Case #%d: %s\n", t+1, result.c_str());
	}

	fclose(in);
	fclose(out);
	return 0;
}
