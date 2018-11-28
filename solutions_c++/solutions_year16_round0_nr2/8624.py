#include <bits/stdc++.h>
using namespace std;
bool yoyo(string str){
	for(int i=0;i<(int)str.length();i++)if(str[i]!='+')return false;
	return true;
	}
int fin(string str){
	for(int i=(int)str.length();i>=0;i--)if(str[i]=='-')return i;
	return -1;
	}

int main(){
	//file hadling sucks . . .
	ifstream cin("B-large.in");
	ofstream cout("output2.txt");
	int t,tc=1;
	//scanf("%d",&t);
	cin>>t;
	while(t--){
		string str;
		cin >> str;
		cout<<"Case #"<<tc<<": ";
		++tc;
		int i=0,len=str.length();
		int ln=len,ans=0;
		while(ln--){
			if(yoyo(str))break;
			int k=fin(str);
			for(i=0;i<=k;i++)if(str[i]=='+')str[i]='-';else str[i]='+';
			ans++;
			}
		cout<<ans<<"\n";
		}
	}
