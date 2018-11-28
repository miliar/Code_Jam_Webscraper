#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i,j;
	cin>>t;
	for (i=0;i<t;i++){
		string s;
		cin>>s;
		int count=0;
		char temp=s[0];
		int s_length=s.length();
		for(j=1;j<s_length;j++){
			if(temp!=s[j])
				count++;
			temp=s[j];
		}
		if(temp == '-')
			count++;
		cout<<"case #"<<i+1<<": "<<count<<endl;
	}
}
