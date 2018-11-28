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
				
		double c,f,x;
        
        fin >> c >> f >> x;
        
        double ret = x/2.0;
        
        double rate = 2.0;
        
        double t = 0.0;
        
        while(c < f*(ret-t) )
        {
            t+=c / rate;
            rate+=f;
            
            double d = t + x/rate;
            if(d<ret)
                ret = d;
        }
        
		
		cout << "Case #" << ct << ": ";
		fout << "Case #" << ct << ": ";
		
       
            cout << ret;
            fout << ret;
        
        
		
		
		
		fout << endl;
		cout << endl;
		
	}
	
	
	return 0;
}

