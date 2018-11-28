//g:\tech\c++\microsoft\microsoft\microsoft\

#include "stdafx.h"
#include<iostream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <sstream>
#include <fstream>

using namespace std;

int main(){
	int T;
	ifstream in("d://test//G//B-large.in");
	ofstream out("d://test//G//output.txt");
	in>>T;
	for(int i=1;i<=T;i++)
	{
		int n,m;
		in>>n>>m;
		bool flag=false;
		int **data=new int*[n];
		for(int a=0;a<n;a++){
			data[a]=new int[m];
			for(int b=0;b<m;b++){
				in>>data[a][b];
			}
		}
		for(int a=0;a<n;a++){
			for(int b=0;b<m;b++){
				flag=true;
				for(int c=0;c<n;c++){
					if(data[c][b]>data[a][b]){
						flag=false;
						break;
					}
				}
				if(!flag){
					flag=true;
					for(int d=0;d<m;d++){
						if(data[a][d]>data[a][b]){
							flag=false;
							break;
						}
					}
				}
				if(!flag)
					break;
			}
			if(!flag)
				break;
		}
		out<<"Case #"<<i<<": "<<(flag?"YES":"NO")<<endl;
	}
	return 0;
}