#include<iostream>
#include<stdio.h> 
#include<stdlib.h>
#include<fstream>
#include<set>
#include<cmath>
using namespace std;
ifstream fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");
string input[101];
string order;
int numOfChar[101][101];
double needed[101];
int T,N;
string makeOrder(int k) {
	char t[101];
	char a = input[k][0];
	int p=0,count=1;
	t[p++] = a;
//	for(int i=0;i<input[k].length();i++) cout<<input[k][i]<<" ";
//	cout<<endl;
	for(int i=1;i<input[k].length();i++) {
		if(input[k][i] == a) {
			count++;
			continue;
		} else {
			numOfChar[k][p-1] = count; 
			count = 1;
			a = input[k][i];
			t[p++] = a;
		}
	}
	numOfChar[k][p-1] = count;
//	cout<<string(t,p)<<endl;
	return string(t,p);
}
int main() {
	string tOrder;
	bool win;
	int total=0;
	fin>>T;
	for(int k=0;k<T;k++) {
		fin>>N;
		win = 0;
		for(int i=0;i<N;i++)	fin>>input[i];
		order = makeOrder(0);
	//	cout<<k+1<<"Order: "<<order<<endl;
		for(int i=1;i<N;i++) {
			tOrder = makeOrder(i);
			if(tOrder.compare(order)!=0) {
				fout<<"Case #"<<k+1<<": "<<"Fegla Won"<<endl;
				win=1;
				break;
			}
		}
		if(win) continue;
		for(int i=0;i<order.length();i++) {
			needed[i] = 0;
			for(int j=0;j<N;j++) {
				needed[i] += numOfChar[j][i];
			}
			needed[i] = round(needed[i]/N);
//			cout<<needed[i]<<" ";
		}
//		cout<<endl;
//		cout<<"---"<<endl;
		total = 0;
/*		for(int i=0;i<N;i++) {
			for(int j=0;j<order.length();j++) {
				cout<<numOfChar[i][j]<<" ";
			}
			cout<<endl;
		}*/
		
		
		for(int i=0;i<order.length();i++) {
			for(int j=0;j<N;j++) {
				total += abs(needed[i] - numOfChar[j][i]);
			}
		}
		fout<<"Case #"<<k+1<<": "<<total<<endl;
	}
}

