#include <iostream>
#include <fstream>
#include <string>
#include<stdio.h>
#include<stdlib.h>
#include <vector>

using namespace std;

unsigned int split(const std::string &txt, std::vector<std::string> &strs, char ch)
{
    unsigned int pos = txt.find( ch );
    unsigned int initialPos = 0;
    strs.clear();

    // Decompose statement
    while( pos != std::string::npos ) {
        strs.push_back( txt.substr( initialPos, pos - initialPos ) );
        initialPos = pos + 1;

        pos = txt.find( ch, initialPos );
    }

    // Add the last one
    strs.push_back( txt.substr( initialPos, std::min( pos, txt.size() ) - initialPos ) );

    return strs.size();
}

int main () {
	int T;
	int it;
	int Smax;
	int i;
	int invitedFriends;
	int clappingAudience;
	
	std::vector<std::string> S;
	
	string line;
	ifstream in ("A-large.in");
	if(!in.is_open()){
		cout << "Unable to open file"; 
		return 0;                 
	}
	ofstream out("A-large.out", ios::out);
    
	getline (in,line);
    T=atoi(line.c_str());
    for(it=1;it<=T;it++){
        getline(in,line);
        split(line,S,' ');
        Smax=atoi(S[0].c_str());
        
        invitedFriends=0;
		clappingAudience=S[1][0]-'0';
        for(i=1;i<=Smax;i++){
            if((int)(S[1][i]-'0')!=0){
                if(i>(clappingAudience+invitedFriends)){
                     invitedFriends+=i-(clappingAudience+invitedFriends);
                }
                clappingAudience+=S[1][i]-'0';               
            }
        }
        out<<"Case #"<<it<<": "<<invitedFriends<<endl;
    }
    
	in.close();
    out.close();

	return 1;
}
