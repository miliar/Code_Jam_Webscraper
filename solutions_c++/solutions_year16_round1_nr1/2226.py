#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	string a;
	deque<char> de;
	int top;
	for(int i=1;i<=t;i++){
		cin>>a;
		de.clear();
		de.push_back(a[0]);
		top=1;
		for(;top<a.size();top++){
			if(a[top]>=de.front()){
				de.push_front(a[top]);
			}else{
				de.push_back(a[top]);
			}
		}
		cout<<"Case #"<<i<<": ";
		for(auto it:de)
			cout<<it;
		cout<<endl;
	}
}
