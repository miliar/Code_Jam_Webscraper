#include <iostream>
#include <math.h>
#include <string>
using namespace std;
bool f(string s){
    int c=0;
	for (int i=0;i<s.size();i++){
	    if (s[i]=='+')c++;}
	if (c==s.size())return true;
	return false;}
string fs(string s,int n){
	for (int i=0;i<n;i++){
	    if (s[i]=='+')s[i]='-';
		else {s[i]='+';}
	}
	return s;
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
    int t;
	cin >> t;
	for (int j=1;j<=t;j++){
	   string s;
	   cin >> s;
	   int c=0;
	   while (!f(s)){
	       bool r=false;
		   for (int i=0;;i++){
		       if (s[i]=='-')r=true;
			   if (s[i]=='-'&&i==s.size()-1){s=fs(s,s.size());c++;break;}
			   if (s[i]=='+'&&r==true){s=fs(s,i);c++;break;}}}
		   
	   cout << "Case #" << j << ": " << c << endl;
	   
	   
	}
 
	return 0;
}