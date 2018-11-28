#include<iostream>
#include<list>
using namespace std;
int Deceitful_War(list<float> b1,list<float>b2);
int War(list<float> b1,list<float>b2);
int main(){
	int T,N,i,j;
	float w;
	list<float> b1,b2;
	cin>>T;
	for(i=1;i<=T;i++){
		cin>>N;
		for(j=1;j<=N;j++){//ifput of Naomi's blocks
			cin>>w;
			b1.push_back(w);
		}
		for(j=1;j<=N;j++){//input of Ken's blocks
			cin>>w;
			b2.push_back(w);
		}
		b1.sort();
		b2.sort();
		cout<<"Case #"<<i<<": "<<Deceitful_War(b1,b2)<<" "<<War(b1,b2)<<endl;

		b1.clear();
		b2.clear();
	}
}
int Deceitful_War(list<float> b1,list<float>b2){
	int score=0;
	while(!b1.empty())
		if(b1.back()<b2.back()){
			b1.pop_front();
			b2.pop_back();
		}
		else{
			b1.pop_back();
			b2.pop_back();//core
			score++;
		}
	return score;
}
int War(list<float> b1,list<float>b2){
	int score=0;
	while(!b1.empty())
		if(b1.back()<b2.back()){
			b1.pop_back();
			b2.pop_back();
		}
		else{
			b1.pop_back();
			b2.pop_front();
			score++;
		}
	return score;
}