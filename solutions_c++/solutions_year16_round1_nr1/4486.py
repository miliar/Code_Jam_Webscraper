#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	int e=1;
	freopen("A-large.in", "r", stdin);
	freopen("output3.txt", "w", stdout);
	cin>>t;
	char s[1000];
	while(e<=t){
		vector <char> v;
		cin>>s;
		int len=strlen(s);
		int i=0,j=1;
		v.insert(v.begin(),s[0]);
		for(int k=1;k<len;k++){
			i=0;
			if(s[k]<v[i]){
				v.push_back(s[k]);
				j++;
			}
			else if(s[k]>v[i]){
				v.insert(v.begin(),s[k]);
				j++;
			}
			else if(v[i]==s[k]){
				while(v[i]==s[k]&&i<j)
					i++;
					if(v[i]>s[k]&&i<len)
						v.push_back(s[k]);
					else
						v.insert(v.begin(),s[k]);
					j++;
			}
		}
		cout<<"Case #"<<e<<": ";
		for(i=0;i<len;i++)
			cout<< v[i];
			cout<<endl;
				e++;
	}
	return 0;
}
