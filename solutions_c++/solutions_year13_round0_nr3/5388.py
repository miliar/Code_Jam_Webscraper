#include<iostream>
#include<sstream>
#include<string>
#include <fstream>
using namespace std;
int revr(int);

int main() {
	int i,j,num,k,total_count,case_no,num_cases;
	stringstream st;
  	ifstream b_file ( "C-small-attempt0.in" );
  	ofstream b_out ("sol_small.out");
  	b_file>>num_cases;
	total_count = 0;
	case_no=0;
	while(case_no<num_cases){
	b_file>>i;
	b_file>>j;	
	total_count=0;
	while(i<=j){
		if(i==revr(i)){
//			cout<<i<<"->"<<revr(i)<<"\n";
			//palindromes
			for(k=1;k<=i;k++){				
				if((k*k) == revr(i)) {
					if(k==revr(k)){					
					total_count=total_count+1;
					
					break;
					}
				}
			}
		}
		i++;		
	}
	
	b_out<<"Case #"<<case_no+1<<": "<<total_count<<"\n";
	case_no++;
	}
	return 0;
}

int revr(int num) {
	int mulfact;
	if (num<10){
		return num;
	}else {
		if(num<100){
			mulfact = 10;
		} else if (num<1000) {
			mulfact = 100;
		}
		return ((num%10)*mulfact + revr(num/10));
	}	
}
