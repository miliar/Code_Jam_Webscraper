/*
 * Gary Ferrao
 * https://plus.google.com/u/0/110619450313015458698
 * 16:21:51 13 April 2013 IST
 * Lawnmower

Problem
Alice and Bob have a lawn in front of their house, shaped like an N metre by M
metre rectangle. Each year, they try to cut the lawn in some interesting
pattern. They used to do their cutting with shears, which was very time-
consuming; but now they have a new automatic lawnmower with multiple settings,
and they want to try it out.

The new lawnmower has a height setting - you can set it to any height h between
1 and 100 millimetres, and it will cut all the grass higher than h it encounters
to height h. You run it by entering the lawn at any part of the edge of the
lawn; then the lawnmower goes in a straight line, perpendicular to the edge of
the lawn it entered, cutting grass in a swath 1m wide, until it exits the lawn
on the other side. The lawnmower's height can be set only when it is not on the
lawn.

Alice and Bob have a number of various patterns of grass that they could have on
their lawn. For each of those, they want to know whether it's possible to cut
the grass into this pattern with their new lawnmower. Each pattern is described
by specifying the height of the grass on each 1m x 1m square of the lawn.

The grass is initially 100mm high on the whole lawn.

Input

The first line of the input gives the number of test cases, T. T test cases
follow. Each test case begins with a line containing two integers: N and M. Next
follow N lines, with the ith line containing M integers ai,j each, the number
ai,j describing the desired height of the grass in the jth square of the ith
row.

Output

For each test case, output one line containing "Case #x: y", where x is the case
number (starting from 1) and y is either the word "YES" if it's possible to get
the x-th pattern using the lawnmower, or "NO", if it's impossible (quotes for
clarity only).

Limits

1 ≤ T ≤ 100.

Small dataset

1 ≤ N, M ≤ 10.
1 ≤ ai,j ≤ 2.
Large dataset

1 ≤ N, M ≤ 100.
1 ≤ ai,j ≤ 100.

 */
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <climits>
#define MAX 102
using namespace std;

bool check_all(int,int,int,int,int [MAX][MAX]);
bool check_left(int,int,int,int,int [MAX][MAX]);
bool check_right(int,int,int,int,int [MAX][MAX]);
bool check_top(int,int,int,int,int [MAX][MAX]);
bool check_bottom(int,int,int,int,int [MAX][MAX]);

int main ()
{
	ifstream ipfile;
	ofstream opfile;
	ipfile.open("B-large.in");
	opfile.open("B-large.op");
	if(! ipfile.is_open())
	{
  		cout << "Input file not found. Exiting..." << endl;
		ipfile.close();
		opfile.close();
		return -1;
	}
	int t, countt=0, lawn[MAX][MAX],n,m;
	for(int i=0; i<MAX; i++)
	{
		lawn[0][i]=INT_MIN;
		lawn[i][0]=INT_MIN;
		lawn[MAX-1][i]=INT_MIN;
		lawn[i][MAX-1]=INT_MIN;
	}
	ipfile >> t;
	while(++countt <= t)
	{
		ipfile >> n >> m;
		int countn=0, countm;
		//inputting the lawn into 2D array surrounded by minimum value
		//of integer
		while(++countn <= n)
		{
			countm = 0;
			while(++countm <= m)
			ipfile >> lawn[countn][countm];
			lawn[countn][countm] = INT_MIN;
		}
		countm = 0;
		while(++countm <= m)
			lawn[countn][countm] = INT_MIN;
		lawn[countn][countm] = INT_MIN;
		bool validlawn = true;
		//loop for height levels 1 to 100
		for(int i=1; i<=MAX-2; i++)
		{
			//try to fill up each height level incrementally
			bool validcells[MAX][MAX];
			for(int j=1; j<=n; j++)
			{
				for(int k=1; k<=m; k++)
				{
					if(i==lawn[j][k])
					{
						//a cell at a given height is valid if only it can reach
						//either "left and right" or "top and bottom" boundaries.
						validcells[j][k] = check_all(j,k,countn, countm, lawn);
					}
					else
						validcells[j][k] = false;
				}
			}
			//fill up valid cells. while doing so, if lawn still has lower cell
			//heights, then it is invalid
			for(int j=1; j<=n; j++)
			{
				for(int k=1; k<=m; k++)
				{
					if(validcells[j][k])
						lawn[j][k]++;
					else if(lawn[j][k]<i)
					{
						validlawn = false;
						goto printresult;
					}
				}
			}
		}
		printresult:
		opfile << "Case #" << countt << ": " << (validlawn?"YES":"NO") << endl;
	}
	ipfile.close();
	opfile.close();
	return 0;
}

bool check_all(int i, int j, int rowend, int columnend, int lawn[MAX][MAX])
{
	return (   (check_top(i,j,rowend,columnend,lawn) &&
	            check_bottom(i,j,rowend,columnend,lawn))
	        || (check_left(i,j,rowend,columnend,lawn) &&
	            check_right(i,j,rowend,columnend,lawn)) );
}
bool check_left(int i, int j, int rowend, int columnend, int lawn[MAX][MAX])
{
	int countj = j;
	int minvalue = lawn[i][j];
	while(--countj >= 0)
	{
		if(INT_MIN==lawn[i][countj])
			return true;
		minvalue = min(lawn[i][countj],minvalue);
		if(lawn[i][countj]>minvalue)
			return false;
	} 		
}
bool check_right(int i, int j, int rowend, int columnend, int lawn[MAX][MAX])
{
	int countj = j;
	int minvalue = lawn[i][j];
	while(++countj <= columnend)
	{
		if(INT_MIN==lawn[i][countj])
			return true;
		minvalue = min(lawn[i][countj],minvalue);
		if(lawn[i][countj]>minvalue)
			return false;
	} 		
}
bool check_top(int i, int j, int rowend, int columnend, int lawn[MAX][MAX])
{
	int counti = i;
	int minvalue = lawn[i][j];
	while(--counti >= 0)
	{
		if(INT_MIN==lawn[counti][j])
			return true;
		minvalue = min(lawn[counti][j],minvalue);
		if(lawn[counti][j]>minvalue)
			return false;
	} 		
}
bool check_bottom(int i, int j, int rowend, int columnend, int lawn[MAX][MAX])
{
	int counti = i;
	int minvalue = lawn[i][j];
	while(++counti <= rowend)
	{
		if(INT_MIN==lawn[counti][j])
			return true;
		minvalue = min(lawn[counti][j],minvalue);
		if(lawn[counti][j]>minvalue)
			return false;
	} 		
}
