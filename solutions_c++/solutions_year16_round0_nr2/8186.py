#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <map>
#include <string>
using namespace std;


int T;
int n;
string st;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("out4.txt","w",stdout);
	cin>>T;
	for(int j=1;j<=T;j++){
		cin>>st;
		n=st.length();
		int cur=1;
		for(int i=1;i<n;i++){
			if(st[i]!=st[i-1]){
				cur++;
			}
		}
		if(st[n-1]=='+'){
			cur--;
		}
		cout<<"Case #"<<j<<": "<<cur<<endl;
	}
}