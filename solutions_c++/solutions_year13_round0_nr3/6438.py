#include <iostream>
#include <fstream>

using namespace std;

#define IN_FILE_NAME "C-small-attempt1.in"
#define OUT_FILE_NAME "C-small-attempt1.out"

#define MAX_ANSWER 5

int answer[MAX_ANSWER] = {1, 4, 9, 121, 484};
int result[100] = {0};
int count;

void loadFile();
void saveFile();

int main() 
{
	loadFile();

	saveFile();

	return 0;
}

void loadFile() 
{
	ifstream is;
	is.open(IN_FILE_NAME);

	if(!is.is_open()) return;

	is >> count;

	for(int i=0; i< count; i++)
	{
		int val1, val2;
		// initail
		is >> val1 >> val2;

		// check
		int k;
		for(k=0; k<MAX_ANSWER; k++) 
		{
			if(answer[k] >= val1) break;
		}
		
		int j;
		for(j=MAX_ANSWER-1; j>=k; j--)
		{
			if(answer[j] <= val2) break;
		}
		

		result[i] = j-k+1;
	}

	is.close();
}

void saveFile() 
{
	ofstream os;

	os.open(OUT_FILE_NAME);
	if(!os.is_open()) return;

	for(int i=0; i<count; i++)
	{
		os << "Case #" << i+1 << ": " << result[i] << endl;
	}

	os.close();
}