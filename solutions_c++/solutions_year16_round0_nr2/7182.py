#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<stack>
using namespace std;
typedef long long ll;
#define endl '\n'
int main(){
	FILE *fin=freopen("b.txt","r",stdin);
	assert(fin!=NULL);
	FILE *fout=freopen("ans.txt","w",stdout);
  int T,n,i;
    string s;
    char c;
    cin>>T; 
   for(int t=1;t<=T;++t){ 
    	cin>>s;
    	n=s.length();
    	for( i=n-1;i>=0;--i){
    		if(char(s[i])=='+')continue;
    		else break;
    	}
    	n=i;
    	bool flag;
    	if(char(s[0])=='+')flag=1;
    	else flag=0;
    	if(n==(-1)){
    		cout<<"Case #"<<t<<": "<<"0"<<endl;
    	continue;
    	}int between=0;
    	for(i=0;i<n;++i){
    		if(char(s[i])=='+'){
    			while(char(s[i])=='+')++i;
    			between++;
    		}
    	}
    	if(flag==0)cout<<"Case #"<<t<<": "<<(2*between+1)<<endl;
    	else cout<<"Case #"<<t<<": "<<(2*between)<<endl;
     
    }
	return 0;
}
