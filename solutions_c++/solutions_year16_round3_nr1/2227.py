#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <fstream>
using namespace std;

int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	int n;
	in>>n;
	for(int i=0;i<n;i++){
		int r;
		in>>r;
		int asd[r];
		for(int j=0;j<r;j++){
			in>>asd[j];
		}
		out<<"Case #"<<i+1<<": ";
		int flag=0;
		while(flag==0){
			int max=0;
			int maxindex=0;
			int max2index=-1;
			int max2=0;
			for(int j=0;j<r;j++){
				if(asd[j]>max){
					max2=max;
					max2index=maxindex;
					max=asd[j];
					maxindex=j;
				}
				else if(asd[j]>max2){
					max2=asd[j];
					max2index=j;
				}
			}
			if(max==1){
					flag=1;
				}
				else if(max>max2){
					if(max!=2){
						
						out<<(char)('A'+maxindex)<<(char)('A'+maxindex)<<" ";
						asd[maxindex]-=2;
					}
					else{
						out<<(char)('A'+maxindex)<<" ";
						asd[maxindex]-=1;
					}
				}
				else{
					out<<(char)('A'+maxindex)<<(char)('A'+max2index)<<" ";
					asd[maxindex]-=1;
					asd[max2index]-=1;
				}
			
		}
		char current='A';
		while(r>0){
			if(r%2==1){
				out<<current<<" ";
				r--;
				current++;
			}
			else{
				out<<current<<(char)(current+1)<<" ";
				r-=2;
				current+=2;
			}
		}
		out<<endl;
		
	}
	
	return 0;
}
