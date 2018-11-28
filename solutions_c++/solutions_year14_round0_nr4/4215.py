#include<iostream>
#include<stdio.h>
#include<list>
#include<algorithm>

using namespace std;

int main(){
int T;
cin>>T;
for(int t=1; t<=T; t++){
	int N;
	cin>>N;
	list<float> naomi;
	list<float> ken;
	for(int i=0;i<N;i++){
		float wt;
		cin>>wt;
		naomi.push_back(wt);
	}
	for(int i=0;i<N;i++){
		float wt;
		cin>>wt;
		ken.push_back(wt);
	}
	
	naomi.sort();
	ken.sort();
	
	//original game
	list<float> naomi1=naomi;
	list<float> ken1=ken;
	
	int naomiscore=0;
	for (list<float>::iterator it=naomi1.begin(); it!=naomi1.end(); ++it){
		 list<float>::iterator jt;
		 bool b=false;
		 for (jt=ken1.begin(); jt!=ken1.end(); ++jt){
			if(*jt<*it) continue;
			else {b=true; break;}
		 }
		 if(b){
			ken1.erase(jt);
		 }
		 else{
			ken1.pop_front();
			naomiscore+=1;
		 }
	 }
	 
	int deceitscore=0;
	for (list<float>::iterator jt=ken.begin(); jt!=ken.end(); ++jt){
		 list<float>::iterator it;
		 bool b=false;
		 for (it=naomi.begin(); it!=naomi.end(); ++it){
			if(*jt<*it) {b=true; break;}
			else continue;
		 }

		 if(b){
			naomi.erase(it);
			deceitscore+=1;
		 }
		 else break;
	 } 
	 
	 cout<<"Case #"<<t<<": "<<deceitscore<<" "<<naomiscore<<endl;
	
}
}

