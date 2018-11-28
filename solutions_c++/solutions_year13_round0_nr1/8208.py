#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <climits>
#include <cctype>
#include <cmath>
#include <sstream>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <deque>
#include <queue>
#include <stack>
#include <iomanip>
#include <complex>
#include <list>
#include <bitset>
#include <fstream>
#include <limits>
#include <memory.h>

using namespace std;

#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

//vector<string> YES(int testCase,int )

int main()
{
    READ("A-Small.in");    // esm l downloaded file ay 7aga 
    WRITE("dsa.txt");  // esm l output file w dah hn3melo upload m3 l source pp
    
    int TestCases=0,counter=1;
    vector<string>re;
    cin>>TestCases;
    
    while(TestCases>0){
		vector<string>mystr(4);
		string temp="Case #",s;
		stringstream ss;
		ss<<counter;
		ss>>s;
		temp+=s;
		bool xWin=false,oWin=false,end=false;
		cin>>mystr[0];
		cin>>mystr[1];
		cin>>mystr[2];
		cin>>mystr[3];
		
		for(int i=0;i<mystr.size();i++){ // horizontally checking
			int countX=0,countO=0,countT=0,countD=0;
				for(int j=0;j<mystr[i].size();j++){
					if(mystr[i][j]=='O')countO++;
					else if(mystr[i][j]=='X')countX++;
				//	else if(mystr[i][j]=='.')countD++;
				
					if(j<mystr.size()-1 && mystr[i][j]=='X' && mystr[i][j+1]=='T') countX++;
					if(j<mystr.size()-1 && mystr[i][j]=='O' && mystr[i][j+1]=='T') countO++;
				}
				if(countO==4){
					oWin=true;
					break;
				}
				else if(countX==4){
					xWin=true;
					break;
				}
		}
		
		if(!xWin&&!oWin)
		for(int i=0;i<mystr.size();i++){  // vertically checking
			int countX=0,countO=0,countT=0,countD=0;
		//	cout<<"temp is "<<temp<<endl;
			//bool xWin=false,oWin=false,draw=false;
				for(int j=0;j<mystr[i].size();j++){
					if(mystr[j][i]=='O')countO++;
					else if(mystr[j][i]=='X')countX++;
				//	else if(mystr[j][i]=='.')countD++;
					
					if(j<mystr.size()-1 && mystr[j][i]=='X' && mystr[j+1][i]=='T') countX++;
					if(j<mystr.size()-1 && mystr[j][i]=='O' && mystr[j+1][i]=='T') countO++;
				}
				if(countO==4){
					oWin=true;
					break;
				}
				else if(countX==4){
					xWin=true;
					break;
				}
		}
		
		if(!xWin&&!oWin){
			int countX=0,countO=0;
			
			for(int i=0;i<mystr.size();i++){ // clockwise diagonal checking
				
					if(mystr[i][i]=='X')countX++;
					else if(mystr[i][i]=='O')countO++;
					
					if(i<mystr.size()-1 && mystr[i][i]=='X' && mystr[i+1][i+1]=='T') countX++;
					if(i<mystr.size()-1 && mystr[i][i]=='O' && mystr[i+1][i+1]=='T') countO++;
					
					if(countO==4){
						oWin=true;
						break;
					}
					else if(countX==4){
						xWin=true;
						break;
					}
			}
		}
		
		if(!xWin&&!oWin){
			int countX=0,countO=0;
			
			for(int i=0;i<mystr.size();i++){ // ANTIclockwise diagonal checking
				
					if(mystr[i][mystr.size()-1-i]=='X')countX++;
					else if(mystr[i][mystr.size()-1-i]=='O')countO++;
				//	cout<<i<<" "<<mystr.size()-1-i<<" TTT " <<i<<" "<<mystr.size()-i-1<<endl;
					//cout<<"COUNT X "<<countX<<endl;
					if(i<mystr.size()-1 && mystr[i][mystr.size()-1-i]=='X' && mystr[i+1][mystr.size()-i-1-1]=='T') countX++;
					if(i<mystr.size()-1 && mystr[i][mystr.size()-1-i]=='O' && mystr[i+1][mystr.size()-i-1-1]=='T') countO++;
					
					if(countO==4){
						oWin=true;
						break;
					}
					else if(countX==4){
					//	cout<<"dsa"<<endl;
						xWin=true;
						break;
					}
			}
		}

		if(!xWin&&!oWin)
		for(int i=0;i<mystr.size();i++){
			int DOT=0;
			for(int j=0;j<mystr[i].size();j++){
				if(mystr[i][j]=='.')DOT++;
			}
			if(DOT>0){end=true;break;}
		}
		
		
		if(xWin){
			string ko=temp,XX="X won";
			ko+=": "+XX;
			re.push_back(ko);
		}
		else if(oWin){
			string ko=temp,OO="O won";
			ko+=": "+OO;
			re.push_back(ko);
		}
		else if(end){
			string ko=temp,DD="Game has not completed";
			ko+=": "+DD;
			re.push_back(ko);
		}
		else {
			string ko=temp,DD="Draw";
			ko+=": "+DD;
			re.push_back(ko);
		}
		
	
	counter++;	
    TestCases--;
	}
   	
   	for(int i=0;i<re.size();i++){
		cout<<re[i]<<endl;
   	}
    
    return 0;
}
