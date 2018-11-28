#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;

string to_string(int num){
	string res="";
	while(num>0){
		res+=(num%10+'0');
		num/=10;
	}
	reverse(res.begin(),res.end());
	return res;
}

int func(int num){
	if (num==0) return -1;
	vector<bool> table(10,false);
	int count=0;
	int cur=num;
	while(1){
		int runner=cur;
		while(runner>0){
			if (table[runner%10]==false) count++;
			table[runner%10]=true;
			runner/=10;
		}
		if (count==10) break;
		cur+=num;
	}
	return cur;
}

int main(){
	ofstream myfile;
  	myfile.open ("output.txt");
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;++i){
		int num;
		scanf("%d",&num);
		myfile<<"Case #"<<i<<": ";
		int res=func(num);
		if (res==-1) myfile<<"INSOMNIA\n";
		else myfile<<res<<endl;
	}
  	myfile.close();
  	return 0;
}
