#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../../../../output.txt");
ifstream fin("../../../../../input.txt");



int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	cout.precision(9);
	fout.precision(9);
    
    cout << "HELLO" <<  " " << ttt << endl;
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int i,j,k;
		
		int vals[17];
        
        for(i=0; i<17; i++)
            vals[i]=0;
        int a;
        fin >> a;
        
        for(i=0; i<16; i++)
        {
            fin >> j;
            if(a-1 == i/4)
            {
                vals[j]++;
            }
        }
        fin >> a;
        
        for(i=0; i<16; i++)
        {
            fin >> j;
            if(a-1 == i/4)
            {
                vals[j]++;
            }
        }
        
        int opts = 0;
        int ans = -1;
        
        for(i=1; i<17; i++)
        {
            if(vals[i]>=2)
            {
                opts++;
                ans= i;
            }
        }
		
		
		
		cout << "Case #" << ct << ": ";
		fout << "Case #" << ct << ": ";
		
        
		if(opts==1)
        {
            cout << ans;
            fout << ans;
        }
        else if(opts==0)
        {
            cout << "Volunteer cheated!";
            fout << "Volunteer cheated!";
        }
        else{
            cout << "Bad magician!";
            fout << "Bad magician!";
        }
        
		
		
		
		fout << endl;
		cout << endl;
		
	}
	
	
	return 0;
}

