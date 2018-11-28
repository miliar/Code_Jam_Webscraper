/*
 * =====================================================================================
 *
 *       Filename:  b.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/12/2013 11:30:06 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
#include <fstream>
#include <string.h>
#include <iomanip>


using namespace std;

const int maxlen = 200;
const int maxm = 101;

int h[maxm][maxm];
bool check(int k, int m)
{
    int i,j;
	int rmax[maxm],lmax[maxm];
	for (i = 0; i < k;i ++)
		rmax[i] = h[i][0];
	for (j = 0;j < m;j ++)
		lmax[j] = h[0][j];
	for (i = 0;i < k;i ++)
		for (j = 0;j < m;j ++)
		{
			if (rmax[i] < h[i][j])
				rmax[i] = h[i][j];
			if (lmax[j] < h[i][j])
				lmax[j] = h[i][j];
		}
    for (i = 0;i < k;i ++)
        for (j = 0;j < m;j ++)
        {
			if (h[i][j] < rmax[i] && h[i][j] < lmax[j])
				return false;
        }
    return true;
}

int main(int argc, char ** argv)
{
	fstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open(argv[2]);
    int i,n;
    int x,y,k,m;
    fin  >> n;
    for (i = 1;i <=n;i ++)
    {
        fin >> k >> m;
        for (x = 0;x < k;x ++)
            for (y = 0;y < m;y++)
                fin >> h[x][y];
	    	
        for (x = 0;x < k;x ++)
		{
            for (y = 0;y < m;y++)
			   cout << h[x][y] << " ";
			cout << endl;
		}
		cout << "Case #" << i << ": ";
        if (check(k,m))
            cout << "YES";
        else
            cout << "NO";
        cout << endl;

		fout << "Case #" << i << ": ";
        if (check(k,m))
            fout << "YES";
        else
            fout << "NO";
        fout << endl;
    }
	fin.close();
	fout.close();
	return 0;
}
