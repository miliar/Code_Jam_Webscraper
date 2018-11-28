#include<iostream>
#include<string>
#include<cstring>
#include<fstream> 
using namespace std; 

int main(){
	int times;
	ifstream filein;
	ofstream fileout;
	filein.open("B-large.in");
	fileout.open("B-large.out");
	filein>>times; 
	//cout<<times<<endl;
    int flag = 1;
    int turnnum[times];
    memset(turnnum,0,sizeof(int)*times);
    string pan[times];
    for (int j = 0 ; j < times; ++j){
        flag = 1;
    	filein>>pan[j];
    	//cout<<pan[j]<<endl;
	    int len = pan[j].length();
	    if (pan[j][0] == '-'){
		    turnnum[j] ++;
		    flag = 0;
            }
    
	    for (int i = 1; i < len; ++i){
		    if (flag == 1 && pan[j][i] == '-' ){
		    	turnnum[j] += 2;
			     flag = 0;
		    }
		    if (pan[j][i] == '+')
		         flag = 1;
	      }
    }
    for (int i = 0 ; i < times; ++i){
    	 //cout<<"Case #"<<i+1<<": "<<turnnum[i]<<endl;
	      fileout<<"Case #"<<i+1<<": "<<turnnum[i]<<endl;
	  }
	return 0;
}
