#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main(){
int T;
cin>>T;
string s;
for(int time=1;time<=T;time++){

cin>>s;
string ans="";
char x=s.at(0);

string cool ;
cool.push_back(x);
ans.append(cool);
for(int i=1;i<s.length();i++){
	if(s.at(i) >= ans.at(0)){
		string dum=ans;
		ans="";
		cool.clear();
		cool.push_back(s.at(i));
		ans.append(cool);
		ans.append(dum);		
		}
	else{
		cool.clear();
		cool.push_back(s.at(i));
		ans.append(cool);
		}
			

}
	cout<<"Case #"<<time<<": ";
	cout<<ans<<endl;
}
	return 0;
}
