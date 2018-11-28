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
#include <string>
#include <fstream>
using namespace std;

int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	int n;
	in>>n;
	int asd[n];
	int insom[n];
	for (int i=0;i<n;i++)in>>asd[i];
	for (int i=0;i<n;i++)
	{
		int digits[10];
		for(int j=0;j<10;j++)digits[j]=0;
		int count=0;
		int insomnia=0;
		int number=0;
		while(
		digits[0]==0||digits[1]==0||digits[2]==0||digits[3]==0||digits[4]==0||
		digits[5]==0||digits[6]==0||digits[7]==0||digits[8]==0||digits[9]==0		
		){
			number=number+asd[i];
			if(count>100){
				insomnia=1;
				break;
			}
			int temp=number;
			while(temp>0){
				digits[temp%10]=1;
				temp/=10;
			}
			count++;
			
		}
		if(insomnia==1){
			insom[i]=-1;
		}
		else insom[i]=number;
		
	}
	for(int i=0;i<n;i++){
		out<<"Case #"<<i+1<<": ";
		if(insom[i]==-1) out<<"INSOMNIA"<<endl;
		else out<<insom[i]<<endl;
	}
	
		
	return 0;
}
