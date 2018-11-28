/*
ID: Nadim_Ul_Abrar
PROG:
LANG: C++
*/

#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main ()
{
	ofstream fout ("A.out");
    ifstream fin ("A-small-attempt0 (1).in");
    string s1,s2;
    vector <char> c1,c2;
    vector <int> v1,v2;
    int T,c=1,x;
    fin>>T;
    while (T--){
    	fin>>x;
    	fin>>s1>>s2;
    	int sz1=s1.size(),sz2=s2.size();
    	v1.push_back(0);
    	v2.push_back(0);
    	c1.push_back(s1[0]);
    	c2.push_back(s2[0]);
    	for (int i=1;i<sz1;i++){
    		if (s1[i]!=s1[i-1]){
    			c1.push_back(s1[i]);
    			v1.push_back(i);
    		}
    	}
    	v1.push_back(sz1);
    	for (int i=1;i<sz2;i++){
    		if (s2[i]!=s2[i-1]){
    			c2.push_back(s2[i]);
    			v2.push_back(i);
    		}
    	}
    	v2.push_back(sz2);
    	fout<<"Case #"<<c++<<": ";
    	if (c1!=c2){
    		fout<<"Fegla Won"<<endl;
    	}	
    	else{
    		int s=v1.size(),ans=0;
    		for (int i=1;i<s;i++){
    			ans+=abs((v1[i]-v1[i-1])-(v2[i]-v2[i-1]));
    		}
    		fout<<ans<<endl;
    	}
    	v1.clear();
    	v2.clear();
    	c1.clear();
    	c2.clear(); 
    }
}

