#include <fstream>
#include <iostream>
using namespace std;


int main(){
	ifstream read;
    read.open("input", ios::in);
    ofstream write;
    write.open ("output");

    int size;
    read>>size;
    int count = 0;
    int cases = 1;
    int x, y;
    read>>x>>y;
    while (!read.eof()) {
    	
    	
    	for(int i = x; i<=y; i++){
    		if(i == 1)
    			count++;
    		else if(i == 4)
    			count++;
    		else if(i == 9)
    			count++;
    		else if(i == 121)
    			count++;
    		else if(i == 484)
    			count++;
    	}
    	write<<"Case #"<<cases<<": "<<count<<endl;
    	count = 0;
    	cases++;
    	read>>x>>y;
    }

    read.close();
    write.close();


}