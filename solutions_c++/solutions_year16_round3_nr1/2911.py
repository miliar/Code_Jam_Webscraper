#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

bool compare(const pair<int,int> a ,const pair<int,int> b)
{
   return a.second>b.second ;
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
input >> cases;

vector< pair<int, int> > p;
int nump=0;
int total=0;

for(int i=0; i< cases ; i++){


p.clear();
total=0;

input >> nump;
cout<<"case "<<i+1<<" "<<nump<<endl;

for(int i=0; i< nump; i++){
	pair<int, int> t;
	t.first=i;
	input>>t.second;
	p.push_back(t);	
	total+=t.second;
}

cout<<" totoal "<<total<<endl;


output<<"Case #"<<i+1<<":";  
cout<<"Case #"<<i+1<<":";  

while( total !=0 ){

sort( p.begin(), p.end(), compare);

if( p.size() >= 2 ){
	if( (total == 3)&&( p.size()>=3 )&&( p[2].second==1 )){
		char a = (p[0].first+65);
		p[0].second-=1;
		output<<" "<<a;
		cout<<" "<<a;
		total-=1;
	}else if((p[1].second > ((total-2)/2)) || (total==2) ){
		p[0].second-=1;
		p[1].second-=1;
		char a = (p[0].first+65);
		char b = (p[1].first+65);
		output<<" "<<a<<b;
		cout<<" "<<a<<b;
		total-=2;
	}else if(p[0].second >=2 ){
		p[0].second-=2;
		char a = (p[0].first+65);
		output<<" "<<a<<a;
		cout<<" "<<a<<a;
		total-=2;
	}
}else{

	cout<<" soemthing wrong !"<<endl;
}


}

output<<endl;
cout<<endl;

}

input.close();
output.close();
return 0;
}
