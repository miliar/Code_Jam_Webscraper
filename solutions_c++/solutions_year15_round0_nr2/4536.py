#include <iostream>
#include <set>
#include <algorithm>
using namespace std;
multiset <int> p;

int find(multiset <int> q){
	int cnt=0;
	for(multiset <int>::iterator itr=q.begin();itr!=q.end();itr++){
		if(*itr==(*q.rbegin())){
			cnt+=1;
		}
	}
	if(cnt==6 && (*q.rbegin())>6){
		return (*q.rbegin());
	}else if(cnt==5 && (*q.rbegin())>7){
		return (*q.rbegin());
	}
	int min_val;
	multiset <int>::iterator itr_tmp;
	itr_tmp=q.end();
	itr_tmp--;
	int val = *itr_tmp;
	min_val=val;
	if(val==1){
		return 1;
	}
	for(int i=2;i<val;i++){
		multiset <int> tmp=q;
		itr_tmp=tmp.end();
		itr_tmp--;
		tmp.erase(itr_tmp);
		for(int j=0;j<(i-1);j++){
			tmp.insert((val)/i);
		}
		tmp.insert(val-((i-1)*(val/i)));
		min_val=min(min_val,i-1+find(tmp));
	}
	return min_val;
}

int main(){
	int t;
	cin>>t;
	int min_val;
	for(int i=1;i<=t;i++){
		p.clear();
		int d;
		cin>>d;
		int tot=0;
		for(int j=0;j<d;j++){
			int tmp;
			cin>>tmp;
			tot+=tmp;
			p.insert(tmp);
		}
		cout<<"Case #"<<i<<": "<<find(p)<<"\n";
	}
}
