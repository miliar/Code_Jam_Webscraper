#include <iostream>
#include <list>
#include <algorithm>
using namespace std;

void insert_sort(list<int> &diners, int val){
	list<int>::iterator iter = diners.begin();
	while(iter!=diners.end())
	{
		if(val > *iter){
			diners.insert(iter, val);
			return;
		}
		iter++;
	}
	if(val)
		diners.push_back(val);
}
void insert_sort(list<int> &diners, int val1, int val2){
	if(val1 < val2){
		int tmp = val1;
		val1 = val2;
		val2 = tmp;
	}
	list<int>::iterator iter = diners.begin();
	while(iter!=diners.end())
	{
		if(val1 > *iter){
			diners.insert(iter, val1);
			val1=0;
		}
		if(val2 > *iter){
			diners.insert(iter, val2);
			val2=0;
		}
		if(val1==0 && val2==0){
			return;
		}
		iter++;
	}
	if(val1)
		diners.push_back(val1);
	if(val2)
		diners.push_back(val2);
}

void decrease_list(list<int> &diners){
	for(list<int>::iterator iter=diners.begin(); iter!=diners.end(); iter++)
		(*iter)--;
}
void increase_list(list<int> &diners){
	for(list<int>::iterator iter=diners.begin(); iter!=diners.end(); iter++)
		(*iter)++;
}

list<int> dup(const list<int> &l){
	list<int> res;
	for(list<int>::const_iterator iter = l.begin(); iter != l.end(); iter++){
		res.push_back(*iter);
	}
	return res;
}

int solve(list<int> diners){
	if(diners.size()==0)
		return 0;
	list<int>::iterator iter = diners.begin();
	int head = *iter;
	if(head<4)
		return head;
	//do nothing
	decrease_list(diners);
	int option1 = solve(diners);
	increase_list(diners);
	
	int option2 = 1000*1000;
	//divide
	for(int i = 2;i <= head/2; i++){
		list<int> d = dup(diners);
		d.erase(d.begin());
		insert_sort(d, head-i, i);
		int tmp = solve(d);
		if(tmp<option2)
			option2=tmp;
	}
	return option1<option2?option1+1:option2+1;
}

int main(){
	int T = 0;
	cin>>T;
	for(int i = 0; i < T; i++){
		list<int> diners;
		int num;
		cin>>num;
		for(int j = 0; j < num; j++){
			int cur;
			cin>>cur;
			insert_sort(diners, cur);
		}
		cout<<"Case #"<<i+1<<": "<<solve(diners)<<endl;
	}
	return 0;
}
