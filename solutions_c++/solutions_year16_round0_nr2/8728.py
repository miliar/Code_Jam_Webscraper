#include <bits/stdc++.h>
using namespace std;
ifstream fin("textin.txt");
ofstream fout("testout.txt");
int main(){
	int t;
	cin>>t;
   for(int l = 1; l <= t; l++){
   	string s;
   	cin>>s;
    int i=0,count=0;
   	while(i<=(int)s.size()-2){
        if(s[i]!=s[i+1])
        	count++;
        i++;
   	}
   	if(s[s.size()-1]=='-'){
   		fout<<"Case #"<<l<<": "<<count+1<<endl;
   	}else{
   		fout<<"Case #"<<l<<": "<<count<<endl;
   	}
   }
}