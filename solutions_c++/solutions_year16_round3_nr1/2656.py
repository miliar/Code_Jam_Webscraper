/*헤더 선언*/
#include <iostream>
#include <fstream>
#include <assert.h>

using namespace std;

#define SIZE 1001

int main()
{ 
	ifstream in; in.open("A-large.in"); //A-large.in
	assert(in.is_open());
	ofstream out; out.open("A-large.out");//A-large.out
	int T; //number of test cases
	int N;
	in>>T;

	for(int i=1;i<=T;i++){
		int P[SIZE]={0};
		int max_num=0;
		int ind=0;
		int total=0;
		int two=0;

		in>>N;
		for(int j=1;j<=N;j++){
			in>>P[j];	total+=P[j];}

		out<<"Case #"<<i<<": ";

		if(total%2!=0) {
			max_num=0;
			for(int j=1;j<=N;j++){
			int mid=max_num;
			max_num=max(max_num,P[j]);
			if(mid!=max_num)
				ind=j;
			}
			P[ind]=P[ind]-1;
			out<<char('A'-1+ind)<<" ";
			total--;

		}

		while(total>0) {
			max_num=0;
		for(int j=1;j<=N;j++){
			int mid=max_num;
			max_num=max(max_num,P[j]);
			if(mid!=max_num)
				ind=j;
		}

		P[ind]=P[ind]-1;	
		out<<char('A'-1+ind);
		total--;
		two++;
		if(two==2){
			two=0;
			out<<" ";
		}

		}
		if(i==T)
			break;
		out<<endl;
			
	}
		in.close(); out.close();
  return 0;
}