#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");
#define cin fin
#define cout fout

string s;
vector<long long> v;

void work(int dep)
{
	if(dep==0){
		string t;
		t=s;
		s.assign(s.rbegin(),s.rend());
		t+=s;
		s.assign(s.rbegin(),s.rend());
		if(t[0]!='0'){
			istringstream ist(t);
			long long a;
			ist>>a;
			a=a*a;
			ostringstream ost;
			ost<<a;
			t=ost.str();
			string tmp=t;
			tmp.assign(tmp.rbegin(),tmp.rend());
			if(tmp==t) v.push_back(a);
		}
		t=s;
		s.assign(s.rbegin(),s.rend());
		t.erase(t.length()-1,1);
		t+=s;
		s.assign(s.rbegin(),s.rend());
		if(t[0]!='0'){
			istringstream ist(t);
			long long a;
			ist>>a;
			a=a*a;
			ostringstream ost;
			ost<<a;
			t=ost.str();
			string tmp=t;
			tmp.assign(tmp.rbegin(),tmp.rend());
			if(tmp==t) v.push_back(a);
		}
	}else{
		s+='0';work(dep-1);
		s[s.length()-1]='1';work(dep-1);
		s[s.length()-1]='2';work(dep-1);
		s.erase(s.length()-1,1);
	}
}

int main()
{
	int n;
	cin>>n;
	v.push_back(9);
	work(1);
	work(2);
	work(3);
	work(4);
	sort(v.begin(),v.end());
	for(int x=1;x<=n;x++){
		long long p,q;
		cin>>p>>q;
		int y=0,z=0;
		while(v[y]<p) y++;
		while(v[z]<=q) z++;
		cout<<"Case #"<<x<<": ";
		cout<<z-y<<endl;
	}
}