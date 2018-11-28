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
#include <cmath>

using namespace std;

bool check(char*str){
	int t=0;
	int length=strlen(str);
	while(2*t<length-1){
		if(str[t]!=str[length-1-t]){
			return false;
		}
		t++;
	}
	return true;
}

int main(){
	int T;
	ifstream in("d://test//G//C-small-attempt0.in");
	ofstream out("d://test//G//output.txt");
	in>>T;
	for(int n=1;n<=T;n++)
	{
		long a,b;
		long count=0;
		in>>a>>b;
		long x=(long)sqrt((double)a);
		long y=(long)sqrt((double)b);
		if(x*x<a)
			x++;
		for(int i=x;i<=y;i++){
			char*str=new char[200];
			sprintf(str, "%d", i);

			if(check(str)){
				sprintf(str,"%d",i*i);
				if(check(str))
					count++;
			}
		}
		out<<"Case #"<<n<<": "<<count<<endl;
	}
	return 0;
}