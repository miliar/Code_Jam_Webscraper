//============================================================================
// Name    	: google.cpp
// Author  	: Maciej Michalak
// Version 	:
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <list>
using namespace std;

int main() {

    ifstream f;
    ofstream ff;
    
    ff.open("test.out");
    f.open("test.in.cpp");
    
    int num;
    f>>num;
    
    for(int i=0; i<num; i++){
    	int x;
    	f>>x;
    	
    	int res=0;
    	int card=0;
    	int skipper=0;
    	int tab[4] = {0,0,0,0};
    	
    	for(int skip=0; skip<x*4; skip++){
    		f>>tab[skip%4];
    	}
    		
    	for(int skip=0; skip<(4-x)*4; skip++){
    		f>>skipper;
    	}
    		
    	f>>x;
    	
    	for(int skip=0; skip<(x-1)*4; skip++)
    		f>>skipper;
    		
    	for(int skip=0; skip<4; skip++){
    		f>>skipper;
    		for(int last=0; last<4; last++)
    			if(skipper==tab[last]){
    				res++;
    				card = skipper;
    			} 
    	}
    	
    	for(int skip=0; skip<(4-x)*4; skip++)
    		f>>skipper;
    	
    	switch(res){
    		case 0:
    			ff<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
    			break;
    		case 1:
    			ff<<"Case #"<<i+1<<": "<<card<<endl;
    			break;
    		default:
    			ff<<"Case #"<<i+1<<": Bad magician!"<<endl;
    	}
    	
    }
    return 0;
}



