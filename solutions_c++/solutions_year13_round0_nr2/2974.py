#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main(void)
{
	fstream input("lawnmover.in", fstream::in);
	fstream output("lawnmover.out", fstream::out);
	int times;
	input >> times;
	input.ignore();
	int** myLawn;
	for(int casenum=0; casenum<times; casenum++)
	{
		int x, y;
		input >> x >> y;//number of rows, number of columns
		input.ignore();
		
		myLawn = new int*[x];
		for(int xc=0; xc<x; xc++)
		{
			myLawn[xc] = new int[y];
			for(int yc=0;yc<y;yc++)
			{
				input >> myLawn[xc][yc];
			}
			input.ignore();
		}

		//impossible when a tile is surrounded by higher grass on 2 non-opposite sides, extending to an edge.
		bool possible = true;
		for(int xiter = 0; xiter < x; xiter++)
		{
			for(int yiter = 0; yiter < y; yiter++)
			{
				if(xiter<x-1&&yiter<y-1&&possible)
				{
					//get highest in y+ and x+ direction
					//y+
					int maxY = myLawn[xiter][yiter];
					for(int ypos = yiter; ypos < y; ypos++)
					{
						if(myLawn[xiter][ypos]>maxY)
							maxY = myLawn[xiter][ypos];
					}
					//x+
					int maxX = myLawn[xiter][yiter];
					for(int xpos = xiter; xpos < x; xpos++)
					{
						if(myLawn[xpos][yiter]>maxX)
							maxX = myLawn[xpos][yiter];
					}
					if(maxX>myLawn[xiter][yiter]&&maxY>myLawn[xiter][yiter])
						possible = false;
				}
				if(xiter<x-1&&yiter>0&&possible)
				{
					//get highest in y- and x+ direction
					//y-
					int maxY = myLawn[xiter][yiter];
					for(int ypos = 0; ypos < yiter; ypos++)
					{
						if(myLawn[xiter][ypos]>maxY)
							maxY = myLawn[xiter][ypos];
					}
					//x+
					int maxX = myLawn[xiter][yiter];
					for(int xpos = xiter; xpos < x; xpos++)
					{
						if(myLawn[xpos][yiter]>maxX)
							maxX = myLawn[xpos][yiter];
					}
					if(maxX>myLawn[xiter][yiter]&&maxY>myLawn[xiter][yiter])
						possible = false;
				}
				if(xiter>0&&yiter>0&&possible)
				{
					//get highest in y- and x- direction
					//y-
					int maxY = myLawn[xiter][yiter];
					for(int ypos = 0; ypos < yiter; ypos++)
					{
						if(myLawn[xiter][ypos]>maxY)
							maxY = myLawn[xiter][ypos];
					}
					//x-
					int maxX = myLawn[xiter][yiter];
					for(int xpos = 0; xpos < xiter; xpos++)
					{
						if(myLawn[xpos][yiter]>maxX)
							maxX = myLawn[xpos][yiter];
					}
					if(maxX>myLawn[xiter][yiter]&&maxY>myLawn[xiter][yiter])
						possible = false;
				}
				if(xiter>0&&yiter<y-1&&possible)
				{
					//get highest in y+ and x- direction
					//y+
					int maxY = myLawn[xiter][yiter];
					for(int ypos = yiter; ypos < y; ypos++)
					{
						if(myLawn[xiter][ypos]>maxY)
							maxY = myLawn[xiter][ypos];
					}
					//x-
					int maxX = myLawn[xiter][yiter];
					for(int xpos = 0; xpos < xiter; xpos++)
					{
						if(myLawn[xpos][yiter]>maxX)
							maxX = myLawn[xpos][yiter];
					}
					if(maxX>myLawn[xiter][yiter]&&maxY>myLawn[xiter][yiter])
						possible = false;
				}
			}
		}

		if(possible)
		{
			output << "Case #" << casenum+1 << ": YES" << endl;
		}
		else
		{
			output << "Case #" << casenum+1 << ": NO" << endl;
		}
		//output lawn for debugging
		/*
		for(int xc=0; xc<x; xc++)
		{
			for(int yc=0;yc<y;yc++)
			{
				cout << myLawn[xc][yc];
			}
			cout << endl;
		}
		cout << endl;*/




		//unallocate lawn pointers
		for(int xc=0; xc<x; xc++)
		{
			delete[] myLawn[xc];
		}
		delete[] myLawn;

	}
	

	return 0;
}