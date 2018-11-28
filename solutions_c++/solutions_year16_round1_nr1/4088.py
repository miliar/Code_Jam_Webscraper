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
	FILE *fin=freopen("a.txt","r",stdin);
	assert(fin!=NULL);
	FILE *fout=freopen("ans.txt","w",stdout);
    int T,n;
    string s,ans;
    string c,x,y;
    cin>>T;
    for(int t=1;t<=T;++t){
    	cin>>s;
    	n=s.length();
    	x=s[0];
    	y=s[0];
    	ans=x;
    	for(int i=1;i<n;++i){
    		c=s[i];
    		if(c>=x){
    			ans.insert(0,c);
    			x=c;
    		}
    		else{
    			ans.insert(i,c);
    			y=c;
    		}
    	}
    	cout<<"Case #"<<t<<": "<<ans<<endl;
    }
	return 0;
}
