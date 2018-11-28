#include<iostream>
#include<queue>
#include<algorithm>
using namespace std;
#define st first
#define nd second
long double last(vector<long double>&a){
	return a[a.size()-1];	
}
void f(){
	int n,w1=0,w2=0;
	cin>>n;
	vector<long double>nao,ken,tmp1,tmp2;
	long double x;
	for(int i=0;i<n;i++){cin>>x;nao.push_back(x);}
	for(int i=0;i<n;i++){cin>>x;ken.push_back(x);}
	sort(nao.begin(),nao.end());
	sort(ken.begin(),ken.end());
	tmp1=nao;
	tmp2=ken;
	for(int i=0;i<n;i++){
		if(last(nao)>last(ken)){
			w1++;
			nao.pop_back();	
		}
		else{
			nao.pop_back();
			ken.pop_back();
		}
	}
	nao=tmp1;
	ken=tmp2;
	int kon=0;
	for(int i=0;i<nao.size();i++){
		if(nao[i]>ken[kon]){
			w2++;
			kon++;
		}
	}
	cout<<w2<<" "<<w1<<"\n";
}
main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		cout<<"Case #"<<i+1<<": ";
		f();
	}
}
