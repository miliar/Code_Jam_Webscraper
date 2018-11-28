#include <iostream>
#include <cmath>
#include <cstdlib>
#include <map>
#include <algorithm>
#include <sstream>
#include <set>
#include <cstring>
#include <vector>
using namespace std;

map< pair<string, string> , string> product;

void set_table(){
	string rowStrings[8] = {"-1","1","i","j","k","-i","-j","-k"};
	string colStrings[8] = {"i","j","k","-i","-j","-k","1","-1"};
	string table[8][8] = {
		{"-i","-j","-k","i","j","k","-1","1"},
		{"i","j","k","-i","-j","-k","1","-1"},
		{"-1","k","-j","1","-k","j","i","-i"},
		{"-k","-1","i","k","1","-i","j","-j"},
		{"j","-i","-1","-j","i","1","k","-k"},
		{"1","-k","j","-1","k","-j","-i","i"},
		{"k","1","-i","-k","-1","i","-j","j"},
		{"-j","i","1","j","-i","-1","-k","k"}
	};
	for(int i=0;i<8;i++)
		for(int j=0;j<8;j++)
			product[make_pair(rowStrings[i],colStrings[j])] = table[i][j];
}

string findPower(string &x, long long times){
	if(times == 0)
		return "1";
	if(times == 1)
		return x;

	string half = findPower(x,times/2);

	if(times%2 == 0)
		return product[make_pair(half,half)];

	return product[make_pair(product[make_pair(half,half)],x)];
}


int main(){
	long long t,c=1, n , x, i,testDistance;
	string str,str2,val;

	freopen("gcj3.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	set_table();
	while(t--){
		cout<<"Case #"<<c++<<": ";
		cin>>n>>x>>str;
		str2=""; val="1";
		testDistance = min(n*x, n*70);

		for(i=0;i<testDistance;i++)
			str2 += str[i%n];
		for(i=0;i<n;i++)
		{
			val = product[make_pair(val, string(1,str2[i]))];
		}

		if(findPower(val,x)!="-1"){
			cout<<"NO\n";
			continue;
		}

		val="1";

		for(i=0;i<testDistance-1;i++)
		{
			val = product[make_pair(val, string(1,str2[i]))];
			if(val == "i")
				break;
		}

		if(val != "i"){
			cout<<"NO\n";
			continue;
		}
	
		for(i++;i<testDistance;i++)
		{
			val = product[make_pair(val, string(1,str2[i]))];
			if(val == "k")
				break;
		}

		if(val != "k")
			cout<<"NO\n";		
		else cout<<"YES\n";
	}

	return 0;
}