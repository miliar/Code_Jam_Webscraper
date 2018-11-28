#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;


long best( string s ){

if( s.size()==1 ){
	if(s[0]=='+')
		return 0;
	else
		return 1;
}

if( s.back()=='+'){
	s.pop_back(); 
	return best(s);
}else if( s.front()=='-'){
	long bufa;
	long bufb;
	string sa=s;
	string sb=s;
	reverse( sa.begin(), sa.end());
	for( int j=0; j<sa.size() ; j++){
		if(sa[j]=='+')
			sa[j]='-';
		else
			sa[j]='+';
	}
	bufa = best(sa)+1;

	sb.pop_back();
	for( int j=0; j<sb.size() ; j++){
		if(sb[j]=='+')
			sb[j]='-';
		else
			sb[j]='+';
	}
	bufb = best(sb)+1;
	
	return min( bufa, bufb ); 
}else{
	string sc = s;
	sc.pop_back();
	for( int j=0; j<sc.size() ; j++){
		if(sc[j]=='+')
			sc[j]='-';
		else
			sc[j]='+';
	}
	return ( best(sc) +1); 
}



}

int main( int argc, char** argv){


ofstream output;
ifstream input;
cout<< " start "<<endl;
input.open(argv[1]);
output.open("ans.txt");


if(input.fail()){
  cout<<" error opening file"<<endl;
  return -1;
}


int cases;
long ans;
input >> cases;

string os;
string currents;

for(int i=0; i< cases ; i++){

os.clear();

input >> os;

cout<<"case "<<i+1<<" "<<os<<endl;

ans = best( os );

output<<"Case #"<<i+1<<": "<<ans<<endl;  
cout<<"Case #"<<i+1<<": "<<ans<<endl;  

}

input.close();
output.close();
return 0;
}
