#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <cassert>
#include <pthread.h>
using namespace std;

//i=2
//j=3
//k=4
int matrix[5][5]= { {0, 1, 2, 3, 4},
									  {1, 1, 2, 3, 4},
									  {2, 2, -1,4, -3},
									  {3, 3, -4, -1, 2},
									  {4, 4, 3, -2, -1}} ;


inline int Compute(int row,int column)
{
	bool negative = (row < 0) || (column < 0);

	return matrix[abs(row)][abs(column)] * (negative ? -1:1);
}


//find me k
bool FindMeK(const string& input, int start, int end, int lookFor)
{
	//cout<<"INside findmek "<<start<<" "<<end<<endl;
	assert(lookFor == 4);
	int prefix_k = 1;
	for (int index=start; index<=end; ++index) {
		prefix_k = Compute(prefix_k,input[index] - '0');
	}
	return (prefix_k == lookFor) ? true:false;
}


//find me j
bool FindMeJ(const string& input, int start, int end, int lookFor)
{
	//cout<<"INside findmej "<<start<<" "<<end<<endl;
	assert(lookFor == 3);
	bool found = false;
	int prefix_j = 1;
	for (int index=start; index<=end; ++index) {
		prefix_j = Compute(prefix_j, input[index] - '0');
		if (prefix_j == lookFor) {
			//cout<<" --Found j !! "<<index<<endl;
			found = FindMeK(input, index + 1, end, 4);
			if (found) {
				//cout<<"--Found k !!"<<endl;
				break;
			} else {
				//cout<<"--K NOT found .. continuing...."<<endl;
			}
		}
	} //for
	return found;
}

void DoSolve(int test, const string& input, int L, int X)
{
	//cout<<"DoSolve: "<<input<<endl;
	int prefix_i = 1;
	bool found = false;

	//find if we can get a prefix containing 'i'
	for (int index=0; index<input.length(); ++index) {
		prefix_i = Compute(prefix_i, input[index]-'0');

		//cout<<"index: "<<index<<" prefix_i: "<<prefix_i<<endl;

		//2 is same as 'i'
		if (prefix_i == 2) {
			//cout<<"--Found i !! "<<index<<endl;
			found = FindMeJ(input, index + 1, input.length()-1, 3);
		}

		//some segments indeed make up '234' i.e. 'ijk'
		if (found) break;
	} //for

	if (found)
		cout<<"Case #"<<test<<": YES"<<endl;
	else
		cout<<"Case #"<<test<<": NO"<<endl;
}

inline bool FindMeI(const string& input, int start,int end, int lookFor)
{
	assert(lookFor == 2);
	int prefix_i = 1;
	bool found = false;

	for (int index=end; index>=start; --index) {
		prefix_i = Compute(prefix_i, input[index] - '0');
	}

	if (prefix_i == lookFor)
		return true;
	return false;
}

bool FindMeJ_Try1(const string& input, int start, int end, int lookFor)
{
	assert(lookFor == 3);
	int prefix_j = 1;
	bool found = false;

	for (int index=end; index>=start; --index) {
		prefix_j = Compute(prefix_j, input[index] - '0');
		
		if (prefix_j == lookFor) {
			found = FindMeI(input, 0, index-1, 2);
			
			if(found)
				return found;
		}
	}//for

	return found;
}


void DoSolveTry1(int test,const string& input, int L, int X)
{
	int prefix_k = 1;
	bool found = false;
	
	//do right to left...
	for (int index=input.size()-1; index>=0; --index) {
		prefix_k = Compute(prefix_k, input[index] - '0');

		if (prefix_k == 4) {
			found = FindMeJ_Try1(input, 0, index-1, 3);
			if (found)
				break;
		}
	} //for

	if (found)
		cout<<"Case #"<<test<<": YES"<<endl;
	else
		cout<<"Case #"<<test<<": NO"<<endl;
}

int main()
{
	int T;
	cin>>T;

	for (int test=1; test<=T; ++test) {
		int L; //length
		int X; //repeatations.
		cin>>L>>X;

		string s;
		cin>>s;

		//cout<<"--------------------------"<<endl;
		//cout<<"S: "<<s<<endl;
		if (s == "ijk") {
			cout<<"Case #"<<test<<": YES"<<endl;
			continue;
		}

		if (L*X < 3) {
			cout<<"Case #"<<test<<": NO"<<endl;
			continue;
		}

		string input;
		//convert
		for (int z=0; z<s.length(); ++z) {
			if (s[z] == 'i')
				input += '2';
			else if (s[z] == 'j')
				input += '3';
			else {
				input += '4';
			}
		}

		string temp;
		//cout<<"Repeatations: "<<X<<endl;
		for (int z=1; z<=X; ++z) {
			//cout<<"z: "<<z<<" : " <<input<<endl;
			temp += input;
		}

		DoSolve(test, temp, L, X);
	}

	return 0;
}
