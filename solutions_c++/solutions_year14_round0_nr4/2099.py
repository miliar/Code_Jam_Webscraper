#include <iostream>
#include <algorithm>
#include <list>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
//t1 is tianji
int deceive(list<double> t1,list<double> t2){
	int p=0;
	for(list<double>::iterator i=t1.begin();i!=t1.end();i++){
		double s=*i;
		double t=*(t2.begin());
		if(s>t){
			p++;
			t2.pop_front();
		}else{
			t2.pop_back();
		}
	}
	return p;
}
//t1 is tianji
int opti(list<double> t1,list<double> t2){
	int p=0;
	for(list<double>::iterator i=t1.begin();i!=t1.end();i++){
		double s=*i;
		bool win=false;
		for(list<double>::iterator j=t2.begin();j!=t2.end();j++){
			double t=*j;
			if(t>s){
				win=true;t2.erase(j);break;}
		}
		if(!win) {p++; t2.pop_front();}
	}
	return p;
}

int main(){
	int cases;cin>>cases;
	for(int caseI=1;caseI<=cases;caseI++){
		list<double> p1,p2;
		int T;double tmp;cin>>T;
		rep(i,T) {cin>>tmp;p1.push_back(tmp);}
		rep(i,T) {cin>>tmp;p2.push_back(tmp);}
		p1.sort();//p1.begin(),p1.end());
		p2.sort();//p2.begin(),p2.end());
		int win1=deceive(p1,p2);
		int win2=opti(p1,p2);
		cout<<"Case #"<<caseI<<": "<<win1<<" "<<win2<<endl;
	}
	return 0;
}

