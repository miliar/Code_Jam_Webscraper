#include <iostream>
#include <cstdio>
#include <string.h>
#include <map>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[]) {
	string matrix[4][4];
	matrix[0][0]="1";
	matrix[0][1]="i";
	matrix[0][2]="j";
	matrix[0][3]="k";
	
	matrix[1][0]="i";
	matrix[1][1]="-1";
	matrix[1][2]="k";
	matrix[1][3]="-j";
	
	matrix[2][0]="j";
	matrix[2][1]="-k";
	matrix[2][2]="-1";
	matrix[2][3]="i";
	
	matrix[3][0]="k";
	matrix[3][1]="j";
	matrix[3][2]="-i";
	matrix[3][3]="-1";
	
	map<string, int> values;
	
	values.insert( pair<string, int> ("1", 0) );
	values.insert( pair<string, int> ("i", 1) );
	values.insert( pair<string, int> ("j", 2) );
	values.insert( pair<string, int> ("k", 3) );
	
	
	freopen( "input_s.txt", "r", stdin );
	freopen( "output_s.txt", "w", stdout );
	int cases;
	
	cin>>cases;
	
	for(int i=0;i<cases;i++){
		string characters="";
		string answer="";
		int length=0, xtimes=0;
		int signo=1;
		int check_index=0;
		cin>>length>>xtimes;
		cin>>characters;
		
		string temp="1";
		
		for(int j=0;j<xtimes;j++){
			for(int k=0;k<length;k++){
				string str=string(1,characters[k]);
				
				if((matrix[values[temp]][values[str]]).size()==1){
					
					temp=matrix[values[temp]][values[str]];
					//cout<<temp<<" ";
				}else{
					signo*=-1;
					temp=matrix[values[temp]][values[str]][1];	
					//cout<<temp<<" ";
				}
				
				if(check_index==0){ //searching i
					if(temp=="i" && signo==1){
						check_index++; //i was found
						temp="1";
					}
				}else if(check_index==1){//searching j
					
					if(temp=="j" && signo==1){
						check_index++; //j was found
						temp="1";
					}
				}			
			}
		}
		
		if(temp=="k" && signo==1 && check_index==2)
			answer="YES";
		else 
			answer="NO";
		cout<<"Case #"<<i+1<<": "<<answer<<"\n";
		
	}
	return 0;
}

