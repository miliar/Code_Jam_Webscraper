#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

#define DEFAULT_H 100

struct Farm
{
	int ** farm;
	int width,height;

	Farm(int _width, int _height, int num) : width(_width) , height(_height)
	{
		farm = new int *[height];
		for(int i=0;i<height;i++)
		{
			farm[i] = new int[width];
			for(int j=0;j<width;j++)
			{
				farm[i][j] = DEFAULT_H;
			}
		}
	}

	Farm(int _width, int _height) : width(_width) , height(_height)
	{
		farm = new int *[height];
		for(int i=0;i<height;i++)
		{
			farm[i] = new int[width];
			for(int j=0;j<width;j++)
			{
				cin >> farm[i][j];
			}
		}
	}

	~Farm()
	{

		for(int i=0;i<height;i++)
		{
			delete [] farm[i];
		}
		delete [] farm;
	}

	bool isPossible(const Farm & other)
	{
		int maxH;
		for(int col=0;col<width;col++)
		{
			maxH = other.getMaxHorizontal(col);
			cutHorizontal(col,maxH);
		}
		for(int row=0;row<height;row++)
		{
			maxH = other.getMaxVertical(row);
			cutVertical(row,maxH);
		}
		return (*this == other);
	}

	void cutVertical(int row,int h)
	{
		for(int col=0;col<width;col++)
		{
			if(farm[row][col] > h)
			{
				farm[row][col] = h;
			}
		}
	}
	void cutHorizontal(int col,int h)
	{
		for(int row=0;row<height;row++)
		{
			if(farm[row][col] > h)
			{
				farm[row][col] = h;
			}
		}
	}

	int getMaxVertical(int row) const
	{
		int max=-1;
		for(int col=0;col<width;col++)
		{
			if(farm[row][col] > max)
			{
				max = farm[row][col];
			}
		}
		return max;
	}
	int getMaxHorizontal(int col) const
	{
		int max=-1;
		for(int row=0;row<height;row++)
		{
			if(farm[row][col] > max)
			{
				max = farm[row][col];
			}
		}
		return max;
	}
	void print()
	{
		for(int i=0;i<height;i++)
		{
			for(int j=0;j<width;j++)
			{
				cout << farm[i][j] << " ";	
			}
			cout << endl;
		}
		cout << endl;
	}
	bool operator==(const Farm & other) const
	{
		for(int i=0;i<height;i++)
		{
			for(int j=0;j<width;j++)
			{
				if(farm[i][j] != other.farm[i][j])
				{
					return false;
				}
			}
		}
		return true;
	}
private:
	Farm(const Farm & other) {}
	Farm& operator=(const Farm& other) {return *this;}
};

int main(int argc, char const *argv[])
{
	streambuf *iBackup = NULL , *oBackup = NULL;
	ofstream output;
	ifstream input;

	// backsup input/output
	iBackup = cin.rdbuf();
	oBackup = cout.rdbuf();
	
	input.open(argv[1]);
	
	if( input.fail()){
		cout << "input failed." << endl;
		return 1;
	}

	cin.rdbuf(input.rdbuf());
	
	output.open(argv[2]);
	if( output.fail()){
		cout << "output failed." << endl;
		return 1;
	}
	cout.rdbuf(output.rdbuf());
	
	int T=0;
	int width, height;
	cin >> T;
	
	for(int i=1;i<=T;i++)
	{
		cin >> height >> width;
		Farm cur(width,height,1);
		Farm requested(width,height);

		cout << "Case #" << i << ": ";
		cur.isPossible(requested) ? cout << "YES" : cout << "NO";
		cout << endl;
	}
	
	input.close();
	cin.rdbuf(iBackup);
	output.close();
	cout.rdbuf(oBackup);

	return 0;
}