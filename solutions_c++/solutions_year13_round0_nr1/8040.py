#include <iostream>
#include <fstream>

using namespace std;

#define IN_FILE_NAME "A-small-attempt4.in"
#define OUT_FILE_NAME "A-small-attempt4.out"

#define O_WIN "O won"
#define X_WIN "X won"
#define DRAW "Draw"
#define ING "Game has not completed"

int loadFile(char* result);
void saveFile(char* result, int count);

int main() 
{
	char result[1000] = {0};

	int count = loadFile(result);

	saveFile(result, count);

	return 0;
}

int loadFile(char* result) 
{
	ifstream is;
	is.open(IN_FILE_NAME);

	if(!is.is_open()) return -1;

	int count;
	is >> count;

	char val[4][4];
	char temp;

	for(int i=0; i< count; i++)
	{
		// initail
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; )
			{
				is.get(temp);
				if(temp == 'O' || temp == 'X' || temp == 'T' || temp == '.') {
					val[j][k] = temp;
					k++;
				}
			}
		}

		// check
		int flag = false;
		result[i] = 0;
		for(int j=0; j<4; j++) 
		{
			temp = val[j][0];
			if(temp == '.')
			{
				result[i] = 9;
				continue;
			}


			if(temp == 'T')
			{
				int k;
				for(k=1; k<4; k++) 
				{
					temp = val[j][k];
					if(k != 'T') break;
				}

				if(temp == '.')
				{
					result[i] = 9;
					continue;
				}
			}

			int k;
			for(k=1; k<4; k++)
			{
				if(val[j][k] == 'T') continue;
				if(temp != val[j][k] ) break;
			}
			if(k==4) 
			{
				result[i] = temp;
				flag = true;
				break;
			}
		}

		if(flag == false) 
		{
			for(int j=0; j<4; j++) 
			{
				temp = val[0][j];
				if(temp == '.')
				{
					result[i] = 9;
					continue;
				}
				if(temp == 'T')
			{
				int k;
				for(k=1; k<4; k++) 
				{
					temp = val[k][j];
					if(k != 'T') break;
				}

				if(temp == '.')
				{
					result[i] = 9;
					continue;
				}
			}

				int k;
				for(k=1; k<4; k++)
				{
					if(val[k][j] == 'T') continue;
					if(temp != val[k][j] ) break;
				}
				if(k==4) 
				{
					result[i] = temp;
					flag = true;
					break;
				}
			}
		}

		if(flag == false)
		{
			temp = val[0][0];
			if(temp == '.')
			{
				result[i] = 9;
				continue;
			}
			if(temp == 'T')
			{
				int k;
				for(k=1; k<4; k++) 
				{
					temp = val[k][k];
					if(k != 'T') break;
				}

				if(temp == '.')
				{
					result[i] = 9;
					continue;
				}
			}

			int k;
			for(k=1; k<4; k++)
			{
				if(val[k][k] == 'T') continue;
				if(temp != val[k][k] ) break;
			}
			if(k==4) 
			{
				result[i] = temp;
				flag = true;
			}


		}

		if(flag == false)
		{
			temp = val[0][3];
			if(temp == '.')
			{
				result[i] = 9;
				continue;
			}
			if(temp == 'T')
			{
				int k;
				for(k=1; k<4; k++) 
				{
					temp = val[k][3-k];
					if(k != 'T') break;
				}

				if(temp == '.')
				{
					result[i] = 9;
					continue;
				}
			}

			int k;
			for(k=1; k<4; k++)
			{
				if(val[k][3-k] == 'T') continue;
				if(temp != val[k][3-k] ) break;
			}
			if(k==4) 
			{
				result[i] = temp;
				flag = true;
			}
		}
	}

	is.close();

	return count;
}

void saveFile(char* result, int count) 
{
	ofstream os;

	os.open(OUT_FILE_NAME);
	if(!os.is_open()) return;

	for(int i=0; i<count; i++)
	{
		switch(result[i]) 
		{
		case 'O':
			os << "Case #" << i+1 << ": " << O_WIN << endl;
			break;
		case 'X':
			os << "Case #" << i+1 << ": " << X_WIN << endl;
			break;
		case 9:
			os << "Case #" << i+1 << ": " << ING << endl;
			break;
		case 0:
			os << "Case #" << i+1 << ": " << DRAW << endl;
			break;
		}
	}

	os.close();

}