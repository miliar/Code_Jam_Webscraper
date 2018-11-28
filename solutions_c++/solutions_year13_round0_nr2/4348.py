//#include <boost/thread/thread.hpp>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <assert.h>

using namespace std;

struct Field
{
	int size_x, size_y;
	vector<int> data, max_x_height, max_y_height;

	Field(int size_x, int size_y) : size_x(size_x), size_y(size_y), data(size_x*size_y), max_x_height(size_x), max_y_height(size_y){}

	int& get(int x, int y)
	{
		if (x < 0 || y< 0 || x>=size_x || y>=size_y)
		{
			cout << "bad []" << x << " " << y << endl;
			throw exception();
		}

		return data[y*size_x + x];
	};

	bool can() 
	{
		for (int y=0; y<size_y; y++)
		for (int x=0; x<size_x; x++)
		{
			int v = get(x, y);
			max_x_height[x] = max(v, max_x_height[x]);
			max_y_height[y] = max(v, max_y_height[y]);
		}

		for (int y=0; y<size_y; y++)
		for (int x=0; x<size_x; x++)
		{
			int v = get(x, y);
			if (v < max_x_height[x] && v < max_y_height[y])
				return false;
		}

		return true;
	}

};

void main()
{
	ifstream f;
	f.open("in.txt");
	if (f.fail())
	{
		cout << "cannot open file" << endl;
		return;
	}

	int cases = 0;
	f >> cases;
	for (int _case=1; _case<=cases; _case++)
	{
		int size_y, size_x;
		f >> size_y;
		f >> size_x;
		Field field(size_x, size_y);
		for (int y =0; y<size_y; y++)
		{
			for (int i=0; i<size_x; i++)
			{
				int v;
				f >> v;
				field.get(i, y) = v;
			}
		}

		cout << "Case #" << _case << ": ";
		if (field.can())
			cout << "YES";
		else
			cout << "NO";

		cout << endl;
	}
}
