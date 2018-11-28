#include<iostream>
#include<sstream>
#include<fstream>
using namespace std;
 bool PerfectSquare(_int64 n)
{
    int h = n & 0xF; 
    if (h > 9)
        return false; 
    if ( h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8 )
    {
        _int64 t = (_int64) floor( sqrt((double) n) + 0.5 );
            return t*t == n;
    }
    return false;

}
bool palidrome(_int64 x){
	
	string s1,s1r;
	stringstream ss;
	ss<<x;
	s1=ss.str();
	ss.flush();
	
	s1r=string(s1.rbegin(),s1.rend());
	if(s1==s1r){
	
		return true;
	
	}
	else
		return false;


}
void main(void){
	fstream in,out;
	in.open("input.in",ios::in||ios::binary);
	out.open("output.txt",ios::out);
	if(in.fail()){
	cout<<"cant"<<endl;
	}
	int test_cases=0;
	double min=0,max=0;
	in>>test_cases;
	for(int j=0;j<test_cases;j++){
		in>>min;
		in>>max;
		int count=0;
		for(_int64 i=min;i<=max;i++){
		
			if(PerfectSquare(i)){
				
				if(palidrome(i) && palidrome((_int64)sqrt(double(i)))){

					count++;
	
				}
			
			}	
		
		}

		out<<"Case #"<<j+1<<": "<<count<<endl;

	}
	out.close();
	in.close();
}

