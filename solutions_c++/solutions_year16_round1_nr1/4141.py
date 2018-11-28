#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <climits>
#include <cstring>
#include <string>

using namespace std;

int main(){
	freopen("A-large (1).in","r",stdin);
	freopen("ssss.out","w",stdout);
	
	int c;
	cin>>c;
	for(int z=1;z<=c;z++){
		string s,tmp="";
		cin>>s;
		cout<<"Case #"<<z<<": ";
		tmp=tmp+s[0];
		for(int i=1;i<s.size();i++)
		{
			if(s[i]>=tmp[0])
			tmp=s[i]+tmp;
			else
			tmp=tmp+s[i];
	}
		cout<<tmp<<endl;
	}
	return 0;
}