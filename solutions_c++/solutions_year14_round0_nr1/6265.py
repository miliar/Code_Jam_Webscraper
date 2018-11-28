/*
ID: Nadim_Ul_Abrar
PROG:
LANG: C++
*/

#include <fstream>
#include <iostream>
#include <vector>
#define ll long long

using namespace std;

int main ()
{
	ofstream fout ("A-small-attempt2.out");
    ifstream fin ("A-small-attempt2.in");
    int T,c=1,r1,r2,a;
    vector <int> f,s,ans;
    fin>>T;
    while (T--){
    	fin>>r1;
    	for (int i=0;i<16;i++){
    		fin>>a;
    		int k=(i/4);
    		if (k==(r1-1)){
    			f.push_back(a);
    		}
    	}
    		fin>>r2;
    	for (int i=0;i<16;i++){
    		fin>>a;
    		int k=(i/4);
    		if (k==(r2-1)){
    			s.push_back(a);
    		}
    	}
    	for (int i=0;i<4;i++){
    		for (int j=0;j<4;j++){
    			if (f[i]==s[j]){
    				ans.push_back(i);
    				break;
    			}
    		}
    	}
    	fout<<"Case #"<<c++<<": ";
    	if (ans.empty()){
    		fout<<"Volunteer cheated!"<<endl;
    	}
    	else if (ans.size()==1){
    		fout<<f[ans[0]]<<endl;
    	}
    	else{
    		fout<<"Bad magician!"<<endl;
    	}
    	f.clear();
    	ans.clear();
    	s.clear();
    }
}
