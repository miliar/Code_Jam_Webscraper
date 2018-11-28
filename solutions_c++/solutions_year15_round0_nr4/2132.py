//============================================================================
// Name        : second.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream ifs;
	ifs.open("D-small-attempt2.in");
	ofstream ofs;
	ofs.open("output.out");
	int x;
	ifs >> x;

	for(int y=0;y<x;y++)
	{
		if(ifs.good())
		{
		int n,r,c;
		ifs>>n>>r>>c;
		int cells=r*c;
		int res=cells%n;
		switch(n){
				case 1:
					ofs <<"Case #"<<y+1<<": "<<"GABRIEL" <<endl;
					//cout <<"Case #"<<y+1<<": "<<"GABRIEL" <<endl;
					break;
				case 2:
						if(res==0){
							ofs <<"Case #"<<y+1<<": "<<"GABRIEL" <<endl;
						//	cout <<"Case #"<<y+1<<": "<<"GABRIEL" <<endl;
						}else{
							ofs <<"Case #"<<y+1<<": "<<"RICHARD" <<endl;
							//cout <<"Case #"<<y+1<<": "<<"RICHARD" <<endl;
							}

					break;
				case 3:
					if(res==0){
						if(cells==3){
							ofs <<"Case #"<<y+1<<": "<<"RICHARD" <<endl;
							//cout <<"Case #"<<y+1<<": "<<"RICHARD" <<endl;
						}else{
							ofs <<"Case #"<<y+1<<": "<<"GABRIEL" <<endl;
							//cout <<"Case #"<<y+1<<": "<<"GABRIEL" <<endl;
						}
					}else{
						ofs <<"Case #"<<y+1<<": "<<"RICHARD" <<endl;
						//cout <<"Case #"<<y+1<<": "<<"RICHARD" <<endl;
					}

					break;
				case 4:
					if(res==0){
						if(cells==4||cells==8){
							ofs <<"Case #"<<y+1<<": "<<"RICHARD" <<endl;
							//cout <<"Case #"<<y+1<<": "<<"RICHARD" <<endl;
						}else{
							ofs <<"Case #"<<y+1<<": "<<"GABRIEL" <<endl;
							//cout <<"Case #"<<y+1<<": "<<"GABRIEL" <<endl;
						}
					}else{
						ofs <<"Case #"<<y+1<<": "<<"RICHARD" <<endl;
						//cout <<"Case #"<<y+1<<": "<<"RICHARD" <<endl;
					}

					break;
				default:
					break;}
		}
	}

	return 0;
}

