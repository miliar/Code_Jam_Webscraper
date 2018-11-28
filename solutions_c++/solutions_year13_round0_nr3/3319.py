#include<queue>
#include<vector>
#include<string>
#include<utility>
#include<iostream>
#include<fstream>

bool less(std::string a, std::string b){//true if a<b
	if(a.size()==b.size()){
		for(int i=0;i<a.size();i++) if(a[i]!=b[i]) return a[i]<b[i];
		return false;
	}else return a.size()<b.size();
}

bool less_eq(std::string a, std::string b){//true if a<=b
	if(a.size()==b.size()){
		for(int i=0;i<a.size();i++) if(a[i]!=b[i]) return a[i]<b[i];
		return true;
	}else return a.size()<b.size();
}

std::vector<std::string> good;
//std::priority_queue<std::string> good;
std::vector<std::pair<std::string,std::string > > cases;

void parse_good(){
	std::ifstream list("ok.list");
	std::string n;
	
	while(list>>n) good.push_back(n);
}

void parse_input(std::istream& input){
	int cases_n; 	input>>cases_n; 
	cases.resize(cases_n);
	for(std::pair<std::string,std::string>& p:cases){
		input>>p.first;
		input>>p.second;
	}
}

int main(){
	parse_good();
	parse_input(std::cin);
	for(int i=0;i<cases.size();i++){
		int count=0;
		for(auto n:good) if(less_eq(n,cases[i].second) && less_eq(cases[i].first,n)) {
			count++;
			//std::cerr<<n<<std::endl;
		}
		
		std::cout<<"Case #"<<i+1<<": "<<count<<std::endl;
	}

	return 0;
}
