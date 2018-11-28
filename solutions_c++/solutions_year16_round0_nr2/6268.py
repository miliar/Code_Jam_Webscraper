#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;
int T;
char check;
string x;
int tell(int point,char sign);
ifstream f("B-large.in");
ofstream f2("output.txt");
int main(){
	f >>T;
	for(int j=1;j<=T;j++){
		f>>x;
		reverse(x.begin(),x.end());
		stringstream buffer;
		buffer<<"Case #"<<j<<": "<<tell(0,'+')<<endl;
		f2 <<buffer.str();
		
		
	}
f.close();
f2.close();

	return 0;
}

int tell(int point,char sign){
if(point == x.length() -1){
	if(x[point] ==sign)
		return 0;
	else
		return 1;	
}
		
if(x[point] == sign)
	return tell(point+1,sign);
else{
	if(sign =='+')
		return tell(point+1,'-')+1;	
	else
		return tell(point+1,'+')+1;	
}
}
