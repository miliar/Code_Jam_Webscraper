#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define pci pair<char, int>


void printall(vector<pci> v){
	for (int i = 0; i < v.size(); ++i)
	{
		cout<<"<"<<v[i].first<<","<<v[i].second<<"> ";
	}
	cout<<endl;
}

bool allzero(vector<pci> m){
	for (vector<pci>::iterator i = m.begin(); i != m.end(); ++i)
	{
		if(i->second != 0){
			return false;
		}
	}
	return true;
}


bool myf(pci a, pci b){
	return a.second > b.second;
}

int getsum(vector<pci> m){
	int sum = 0;
	for (int i = 0; i < m.size(); ++i)
	{
		sum += m[i].second;
	}
	return sum;
}

bool clearmaj(vector<pci> m, int i){
	m[i].second--;
	//printall(m);
	sort(m.begin(), m.end(), myf);
	if(m[0].second > (getsum(m)-m[0].second))
		return true;
	return false;
}

bool taketwo(vector<pci> m){
	if(m[0].second>0){
		//cout<<m[0].first;
		m[0].second --;
		
	}else{
		return false;
	}
	if(m.size() > 1 && m[1].second>0 && !clearmaj(m,1)){
		//cout<<m[1].first;
		m[1].second --;
		
	}else{
		return false;
	}
	return true;
}

bool takeone(vector<pci> &m){
	if(m[0].second>0){
		cout<<m[0].first;
		m[0].second --;
			}else{
		return false;
	}
	return true;
}

void printbothorfirst(vector<pci> &m){
	
	int two = 2;
	
	if(!taketwo(m))
		takeone(m);
	else{
		cout<<m[0].first;
		m[0].second --;
		
		cout<<m[1].first;
		m[1].second --;
	}
	
	cout<<" ";
}

void solve(){
	int N;
	cin>>N;
	vector<int> arr(N);
	vector<pci> par;
	for (int i = 0; i < N; ++i)
	{
		cin>>arr[i];
	}
	
	for (int i = 0; i < N; ++i)
	{
		char c = (char)('A'+i);
		par.push_back(make_pair(c, arr[i]));
	}

	//printall(par);
	while(!allzero(par)){
	//	printall(par);
		sort(par.begin(), par.end(), myf);
		printbothorfirst(par);
	}
}


int main(){
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		cout<<"Case #"<<t+1<<": ";
		solve();
		cout<<endl;
	}
	return 0;
}