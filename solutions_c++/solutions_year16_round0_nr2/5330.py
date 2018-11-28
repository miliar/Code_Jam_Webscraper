/*
 * a.cpp
 *
 *  Created on: Mar 23, 2016
 *      Author: kathrine
 */
#include <iostream>
#include<set>
#include<vector>
#include<cmath>
#include<iterator>
#include <fstream>
using namespace std;

int main()
{
	ifstream in;
	in.open("B-large.in");
	ofstream out;
	out.open("B-large.out");
int t;
in>>t;
string s;
long long ans;
char tmp;
for(int k=0;k<t;k++){
	in>>s;
	ans=0;
	out<<"Case #"<<k+1<<": ";
	tmp = s[0];
	for(int i=0;i<s.length();i++){
		if(tmp!=s[i]){
			ans++;
			tmp=s[i];
		}
	}
	if(tmp=='-')
		ans++;
	out<<ans<<endl;

}
in.close();
out.close();
  return 0;
}


