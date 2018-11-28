/*
ID: k.kamal1
PROG: test
LANG: C++     
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip> 
#include <set>

using namespace std;

vector<double> no;
vector<double> en;

//set<double>::iterator noTr;
//set<double>::iterator enTr;

int main() {
    ofstream fout ("o.out");
    ifstream fin ("in.in");
    int tetC;
    fin >> tetC;
    //fout << fixed << setprecision(7);
    for(int cnt = 0; cnt < tetC; cnt++)
    {
    	fout << "Case #" << cnt + 1 << ": ";
    	int num;
    	fin >> num;
    	no.clear();
    	en.clear();
    	for(int ct = 0; ct < num; ct++)
    	{
   			double n5;
			fin >> n5;
			//no.insert(n5*1000000);
			//en.insert(e5*1000000); 
			no.push_back(n5);
		}
		for(int ct = 0; ct < num; ct++)
    	{
   			double e5;
			fin >> e5;
			//no.insert(n5*1000000);
			//en.insert(e5*1000000); 
			en.push_back(e5);
		}
		
    	sort(no.begin(), no.end());
		sort(en.begin(), en.end());
    	vector<double> noTm;
    	vector<double> enTm;
    	
    	int w = 0;
    	int enVl = 0;
    	for(int ctc = 0; ctc < no.size(); ctc++)
		{
			for(int tc = enVl; tc < en.size(); tc++)
			{
				if( en[tc] - no[ctc]> .000001)
				{
					enVl = tc + 1;
					w++;
					break;
				} 
						
			}
    		
		    /*else
    		{
    			noTm.push_back(no[ctc]);
    			enTm.push_back(en[ctc]);
    		}*/
    	}
		int nWV = num - w;
		
		w = 0;
    	enVl = 0;
    	for(int ctc = 0; ctc < en.size(); ctc++)
		{
			for(int tc = enVl; tc < no.size(); tc++)
			{
				if( no[tc] - en[ctc]> .000001)
				{
					//cout << " en[tc] "  << en[tc] << " no[ctc] " << no[ctc] << endl;
					enVl = tc + 1;
					w++;
					break;
				} 
						
			}
    		
		    /*else
    		{
    			noTm.push_back(no[ctc]);
    			enTm.push_back(en[ctc]);
    		}*/
    	}

		fout << w << " " << nWV << endl;
		
		/*sort(noTm.begin(), noTm.end());
		sort(enTm.begin(), enTm.end());
		reverse(enTm.begin(), enTm.end());
		
		for(int ctc = 0; ctc < noTm.size(); ctc++)
		{
			if(noTm[ctc] - enTm[ctc] > .000001) 
				w++;
				
		}
		
		cout << w << " nw " << endl;*/	 		
			
			
			
		
		

    	
    	
    	
    	
		//fout << prv << endl;
    }
    //fout << a+b << endl;
    return 0;
}
