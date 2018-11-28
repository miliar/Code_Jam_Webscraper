#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <set>
#include <algorithm>
#include <vector>
#include <map>
#include <cassert>
#include <string>
using namespace std;
int inp[4][4];

int main(int argc, char const *argv[]){
	int t,line,occur[20],num,flag;
	cin>>t;
	for(int test = 1;test<=t;test++){
		cin>>line;
		flag = 0;

		for(int i=0;i<20;i++)
			occur[i] = 0;

		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>inp[i][j];
			}
		}
		for(int i=0;i<4;i++){
			occur[inp[line-1][i]]++;
		}
		cin>>line;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>inp[i][j];
			}
		}
		for(int i=0;i<4;i++){
			if(occur[inp[line-1][i]]){
				if(flag == 0){ flag = 1; num = inp[line-1][i];}
				else if(flag == 1) flag = -1;
			}
		}
		if(flag == 1)
			cout<<"Case #"<<test<<": "<<num<<endl;
		else if(flag == 0)
			cout<<"Case #"<<test<<": Volunteer cheated!"<<endl;
		else if(flag == -1)
			cout<<"Case #"<<test<<": Bad magician!"<<endl;
	}
return 0;
}