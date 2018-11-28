#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
using namespace std;

int done(set<pair<int,int> > &arr){
	int d=1;
	for(auto i : arr){
		if(i.first > 0)	d =0;
	}	
	return d;
}
void rem(set<pair<int,int> > &arr){
	auto i = arr.end();
	i--;
	int a = i->first;
	a--;
	int b = i->second;
	arr.erase(i);
	arr.insert({a,b});
	cout<<(char)('A'+b);
	return;
}
void stable(set<pair<int,int> > &arr){
	auto i = arr.end();
	i--;
	int maxfreq = i->first;
	int tot = 0;
	i--;
	int next = i->first;
	i++;
	for(auto j : arr) tot+=j.first;
	tot-=maxfreq;
	maxfreq--;
	if(maxfreq<=tot && next<=(tot+maxfreq-next)){
		int a = i->first;
		a--;
		int b = i->second;
		arr.erase(i);
		arr.insert({a,b});
		cout<<(char)('A'+b);
	}
	return;
}
int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int T=1; T<=t; T++){
		cout<<"Case #"<<T<<": ";
		set<pair<int,int> > arr;
		int n;
		cin>>n;
		for(int i = 0 ; i< n ; i++){
			int temp;
			cin>>temp;
			arr.insert({temp,i});
		}
		while(!done(arr)){
			if(!done(arr))
				rem(arr);
			if(!done(arr))
				stable(arr);
			cout<<" ";
		}
		cout<<"\n";
	}
	return 0;
}