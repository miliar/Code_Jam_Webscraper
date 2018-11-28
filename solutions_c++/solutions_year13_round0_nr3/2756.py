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
const int maxn = 10000;
bool pf[maxn];

bool par(int i)
{
  if (i < 10)
    return true;
  if (i < 100 && (i / 10 == i % 10))
    return true;
  if (i < 1000 && (i / 100 == i % 10))
    return true;
  return false;
}

int main(int argc, char ** argv)
{
	fstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open(argv[2]);
    int n,i,j,k,a,b;
    fin  >> n;
    memset(pf,false,sizeof(pf));
    for (i = 1;i < maxn;i ++)
    {

        if (i * i > maxn)
            break;
        if (par(i) && par(i * i))
            pf[i * i] = true;
    }
    for (i = 1;i <=n;i ++)
    {
		fin >> a >> b;
		k = 0;
		for (j = a;j <= b;j ++)
		{
			if (pf[j])
				k ++;
		}
		fout << "Case #" << i << ": ";
		fout << k << endl;
    }
	fin.close();
	fout.close();
	return 0;
}
