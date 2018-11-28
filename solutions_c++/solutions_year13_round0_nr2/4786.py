#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <map>

int lawn[100][100];
//std::vector<std::pair<int, point> > height_points;
//expects certain functions to be defined
	//generate queries, given a node

struct point{
	int x;
	int y;
	point(int a, int b): x(a), y(b)
	{}
};
/*
struct work{
	point p;
	int children;

}

template <class workelements, class iter>
void depth_first_search(std::stack<workelements> work, iter workiterator)
{
	std::map visited;
	std::map explored;
	while()

}

bool heightsort(std::pair<int, point> a, std::pair<int, point> b)
{
	return a.first<b.first;
}

int main()
{
	using namespace std;
	int problems;
	cin>> problems;
	for(int i = 0;i<problems;i++)
	{
		int N, M;
		cin>>N;
		cin>>M;
		for(int i = 0;i<100;i++)
			for(int j = 0;j<100;j++)
				lawn[i][j] = 100;
		std::vector<std::pair<int, point> > height_points;
		for(int y=0;y<N;y++)
			for(int x=0;x<M;x++)
			{
				cin>>lawn[y][x];
				height_points.push_back(pair<int, point>(lawn[y][x], point(x,y)));
			}

		std::sort(height_points.begin(), height_points.end(), heightsort);
		std::vector<pair<int, point>>::iterator it = height_points.begin();

		pair<int, point> first_element = *it;
		stack workstack; //must contain... row/column to whack
		depth_first_search( , it);
	}
	
	return 0;
}*/


int main()
{
	using namespace std;
	int problems;
	cin>> problems;
	for(int i = 0;i<problems;i++)
	{
		int N, M; //N columns, N rows
		cin>>N;
		cin>>M;
		for(int i = 0;i<100;i++)
			for(int j = 0;j<100;j++)
				lawn[i][j] = 100;
		std::vector<std::pair<int, point> > height_points;
		for(int y=0;y<N;y++)
			for(int x=0;x<M;x++)
			{
				cin>>lawn[y][x];
				height_points.push_back(pair<int, point>(lawn[y][x], point(x,y)));
			}
		int * rowmax = new int[N];
		int * colmax = new int[M];
		
		for(int row = 0;row<N;row++)
		{
			rowmax[row] = 1;
			for(int x = 0;x<M;x++)
				rowmax[row] = max(rowmax[row], lawn[row][x]);
		}
		for(int col = 0;col<M;col++)
		{
			colmax[col] = 1;
			for(int y = 0;y<N;y++)
				colmax[col] = max(colmax[col], lawn[y][col]);
		}

		bool possible = true;
		for(int y=0;y<N;y++)
			for(int x=0;x<M;x++)
				if(lawn[y][x]<colmax[x] && lawn[y][x]<rowmax[y])
				{
					possible = false;
					break;
				}

		delete rowmax;
		delete colmax;
		cout<<"Case #"<<i+1<<": "<<((possible)?"YES":"NO")<<endl;
	}
	
	return 0;
}