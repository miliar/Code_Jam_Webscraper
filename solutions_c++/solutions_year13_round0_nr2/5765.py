#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <list>
#include <map>
#include <set>

using namespace std;

typedef list<int> row;
typedef list<row> table;

bool checkTable(table *t, int n){

	table t1 = *t;
	
	list<table::iterator> for_removal;
	
	map<unsigned, table::iterator> for_removal_t;
	map<unsigned, row::iterator> for_removal_r;
	int rem = 0;
	
	//cout << "n IS NOW: " << n << endl;
	
	row::iterator cri;
	int remove;
	for(table::iterator it = t1.begin(); it != t1.end(); it++){
    	//cout << "greska na pocetku" << endl;
    	cri = it->begin();
    	if(*cri == n){
    		remove = 1;
    		//cout << *cri << " == " << n << endl;
    		for(++cri; cri != it->end(); cri++){
    			if(*cri != n){
    				remove = 0;
    				break;
    			}
    		}
    		if(remove)
    			for_removal.push_back(it);
    	}
    	else{
    		//cout << "cri = " << *cri << " so just continue..." << endl;
    		continue;
    	}
    }
    
    for(list<table::iterator>::iterator fri = for_removal.begin(); fri != for_removal.end(); fri++)
    	t1.erase(*fri);
    	
    if(t1.empty())
    	return true;
    
    /*cout << "t now looks like: " << endl;
    
    for(table::const_iterator cit = t1.begin(); cit != t1.end(); cit++){
    	for(row::const_iterator cjt = cit->begin(); cjt != cit->end(); cjt++)
    		cout << *cjt;
     	cout << endl;
    }*/
    
    
    table::iterator it = t1.begin();
    row::iterator cri1;
   	int i;
    for(cri = it->begin(), i = 0; cri != it->end(); cri++, i++){
    	//cout << "checking " << *cri << endl;
    	if(*cri == n){
    		for_removal_t.insert(make_pair(rem, it));
    		for_removal_r.insert(make_pair(rem, cri));
    		rem++;
    		//cout << *cri << " == " << n << endl;
    		//cout << "i = " << i << endl;
    		for(table::iterator it1 = ++(t1.begin()); it1 != t1.end(); it1++){
    			cri1 = it1->begin();
    			for(int j = 0; j < i; j++)
    				cri1++;
    			if(*cri1 != n){
    				//cout << *cri1 << " != " << n << endl;
    				return false;
    			}
    			for_removal_t.insert(make_pair(rem, it1));
    			for_removal_r.insert(make_pair(rem, cri1));
    			rem++;
    			//cout << "brisem " << *cri1 << endl;
    		}
    	}
    	else{
    		//cout << *cri << " != " << n << endl;
    		//continue;
    	}
    }
    
    map<unsigned, table::iterator>::iterator tim;
    map<unsigned, row::iterator>::iterator rim;
    for(tim = for_removal_t.begin(), rim = for_removal_r.begin(); tim != for_removal_t.end(); tim++, rim++){
    	(tim->second)->erase((rim->second));
    }
    
    /*cout << "and now t looks like: " << endl;
    
    for(table::const_iterator cit = t1.begin(); cit != t1.end(); cit++){
    	for(row::const_iterator cjt = cit->begin(); cjt != cit->end(); cjt++)
    		cout << *cjt;
     	cout << endl;
    }*/
    
    if(t1.empty())
    	return true;
    
    for(table::const_iterator cit = t1.begin(); cit != t1.end(); cit++){
    	for(row::const_iterator cjt = cit->begin(); cjt != cit->end(); cjt++)
    		if(*cjt == n)
     			return false;
    }
    
    return true;
	
}

int main(){
	
	string line;
	bool result;
  	ifstream myfile("small.in");
  	if(myfile.is_open()){
  		getline(myfile,line);
  		int test_cases = atoi(line.c_str());
  		//cout << "Test cases: " << test_cases << endl;
    	for(int i = 1; i <= test_cases; i++){
    		
    		result = true;
      		
      		cout << "Case #" << i << ": ";
      		
      		getline(myfile, line);
      		istringstream iss(line);
      		vector<string> tokens;
			copy(istream_iterator<string>(iss),
        	istream_iterator<string>(),
        	back_inserter<vector<string> >(tokens));
        	int N, M;
        	
        	N = atoi(tokens[0].c_str());
        	M = atoi(tokens[1].c_str());
        	
        	
        	table lawn;
        	      		
      		for(int j = 0; j < N; j++){
      			row tmp_r;
      			getline(myfile,line);
      			for(int i = 0; i < 2*M; i++)
      				tmp_r.push_back(line[i++] - '0');
      			lawn.push_back(tmp_r);
      		}
      		
      		list<int> nivoi;
      		
      		for(table::const_iterator cit = lawn.begin(); cit != lawn.end(); cit++){
      			for(row::const_iterator cjt = cit->begin(); cjt != cit->end(); cjt++){
      				list<int>::iterator ni = find(nivoi.begin(), nivoi.end(), *cjt);
      				if(ni == nivoi.end())
      					nivoi.push_back(*cjt);
      			}
      		}
      		
      		nivoi.sort();
      		
      		
      		int prethodni;
      		int prva_iteracija = 1;
      		for(list<int>::const_iterator ni = nivoi.begin(); ni != nivoi.end(); ni++){
      			
      			//cout << "Pocinjem za nivo: " << *ni << endl;
      			
      			if(prva_iteracija){
      				if(!checkTable(&lawn, *ni)){
      					result = false;
      				}
      				prethodni = *ni;
      				prva_iteracija = 0;
      			}
      			else{
      				for(table::iterator cit = lawn.begin(); cit != lawn.end(); cit++){
    					for(row::iterator cjt = cit->begin(); cjt != cit->end(); cjt++)
    						if(*cjt == prethodni)
     							*cjt = *ni;
    				}
    				
    				
    				/*cout << "Promenio sam tabelu na: " << endl;
    				for(table::iterator cit = lawn.begin(); cit != lawn.end(); cit++){
    					for(row::iterator cjt = cit->begin(); cjt != cit->end(); cjt++)
    						cout << *cjt;
    					cout << endl;
    				}*/
    				
    				
    				
    				if(!checkTable(&lawn, *ni)){
      					result = false;
      				}
      				prethodni = *ni;
      			}
      		}
      		
      		if(result)
      			cout << "YES" << endl;
      		else
      			cout << "NO" << endl;
      		
      		/*for(table::const_iterator cit = lawn.begin(); cit != lawn.end(); cit++){
      			for(row::const_iterator cjt = cit->begin(); cjt != cit->end(); cjt++)
      				cout << *cjt;
      			cout << endl;
      		}*/
      		
      		/*char res = result();
      		if(res == 'X' || res == 'O')
      			cout << "Case #" << i << ": " << res << " won" << endl;
      		else if(res == 'D')
      			cout << "Case #" << i << ": " << "Draw" << endl;
      		else if(res == 'N')
      			cout << "Case #" << i << ": " << "Game has not completed" << endl;*/
      			
      	
    	}
    	myfile.close();
  	}
  	else cout << "Unable to open file";
	
	return 0;
}
