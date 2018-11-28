#include <cstdlib>
#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <string>
#include <math.h>

using namespace std;

 int mote[101];


int main(){

	ifstream in;
	in.open("A-large.in");
	//in.open("A-large.in");
	
	ofstream out;
	out.open("out.txt");
	
	int T;
	in>>T;
	

	
	for(int u=0;u<T;u++){
				
		unsigned long long A;
		unsigned long long N;
		
		in>>A>>N;
		//cout<<A<<" "<<N<<endl;
		
		for(unsigned long long i=0;i<N;i++){
			in>>mote[i];
		}
		
		sort(mote,mote+N);
		
		
		unsigned long long cur = A;
		unsigned long long op = 0;
		unsigned long long cant = 0;
		
		unsigned long long curC = A;
		unsigned long long opC = 0;
		for(unsigned long long i=0;i<N;i++){
			if(curC <= mote[i]){
				break;
			}
			else{
				opC++;
				curC++;
			}
		}

		
		for(unsigned long long i=0;i<N;i++){
			if(cur>mote[i]){
				cur += mote[i];
			}
			else{
				unsigned long long es = 0;
				while(cur <= mote[i]){
				
					if(cur - 1 == 0){
						cant = 1;
						break;
					}
					cur += cur - 1;
					
					//cout<<"cur"<<cur<<endl;
					
					es++;
				}
				
				if(es >= N - i ){
					//cout<<"val"<<op;
					op = op + N - i;
					//cout<<"val"<<op;
					break;
				}
				else{
					op += es;
				}
				
				if(cant){
					op = N;
					break;
				}
				
				//cout<<"temp"<<op<<endl;
				
				cur += mote[i];
				
			}
		}
		
		if(op > N - opC) op=N-opC;
		
		//cout<<op<<endl;
		cout<<"Case #"<<(u+1)<<": "<<op<<endl;
		out<<"Case #"<<(u+1)<<": "<<op<<endl;
		
		
    }
	in.close();
	out.close();
	
    return 0;
}