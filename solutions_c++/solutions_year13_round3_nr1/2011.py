#include<iostream>
#include<string>
#include <cstdlib>
#include<fstream>
#include<vector>
using namespace std;
int yes(string v , int q){
	for(int i = 0 ; i<v.size() ;i++ ){
		int f =0;
		int c =0;
		if(v.size() - i>= q){
			for(int j = i ; j <i+q ; j++ ){
				if(v[j] == 'a' || v[j] == 'e' ||v[j] == 'i' ||v[j]== 'o' ||v[j] == 'u' )
					f =1;
				if(f == 0){
					c++;
					continue;
				}
				if(f ==1)
					break;
			}
			
			if(c ==q)
				return 1;
		}
	}
	 return 0;
}
int main(){
	ifstream in ("A-small-attempt0 (4).in");
	ofstream out("aque.txt");
	int t,m,count,o;
	string s,d;
	int q;
	
	in >>t;
	for(int i = 0 ; i < t ; i++){
		count =0;
		vector <string> v;
		in >> s>>q;
		m = s.size();
		o = s.size()-1;
		for(int j = 0 ; j< s.size(); j++){
			string str = "";
			for(int z = j; z<s.size() ; ++z)
				str += s[z];
			v.push_back(str);
			for(int z = str.size() - 1; z >=q ; z--){
				d = str.substr(0,z);
				v.push_back(d);
			}
		}
		for(int k=0 ; k<v.size();k++){
		//	cout<<v[k]<<endl;
			if(yes(v[k] ,q) == 1){
				count++;
			}
				

	}
		out<<"Case #"<<i+1<<": "<<count<<endl;
	}
	
	
	return 0;
}
