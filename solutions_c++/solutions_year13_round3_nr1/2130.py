#include<iostream>
#include<fstream>
#include<string>

#include<vector>
//#include<cstdio>
using namespace std;

class VV{
public:
	vector<int> d;
};

vector<VV> v;
VV ins;
unsigned long t,cas,n,count,con;
bool consonent(char c){
	switch(c){
	case 'a':
	case 'e':
	case 'i':
	case 'o':
	case 'u':
	case 'A':
	case 'E':
	case 'I':
	case 'O':
	case 'U':
				return false;
	default:	return true;
	}
}

void insert(int b,int e){
	if(b <= v.size())
		v.push_back(ins);
	v[b].d.push_back(e);
}
bool exist(int b,int e){
	if(b < v.size()){
		for(int i=0;i<v[b].d.size();i++){
			if(v[b].d[i] == e)
				return true;
		}
	}
	else
		return false;
	return false;
}
void chk(string s,int b, int e){
	if(exist(b,e))
		return;
	//cout<<s<<endl;
	con=0;
	for(int i=0;i< s.size();i++)
		if( consonent(s[i]) ){
			con++;
			if(con >= n)
				break;
		}
		else
			con = 0;
	if(con < n)
		return;
	count++;
	insert(b,e);
	chk( s.substr(1),b+1,e );
	//cout<<tmp<<endl;
	chk( s.substr(0,s.size()-1), b,e-1);
	//cout<<tmp<<endl;

}
int main(){
	ifstream in("A-small-attempt1.in");
	ofstream out("outputl.out");
	string str;
	
	in>>t;
	for(cas=1;cas<=t;cas++){
		in>>str>>n;
		count=0;
		v.clear();
		chk(str,0,str.size());
		out<<"Case #"<<cas<<": "<<count<<endl;
	}
	return 0;
}
	
