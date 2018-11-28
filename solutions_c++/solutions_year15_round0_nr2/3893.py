#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main(int argc, char *argv[]) {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) { 
		int d;
		vector<int> diners;
		cin>>d;
		for(int j=0;j<d;j++) { 
			int aux;
			cin>>aux;
			diners.push_back(aux);}
		sort(diners.begin(),diners.end());
		int cantidad,contador=0,total=0,mayor=0,anterior=0;
		cantidad=diners.size();
		vector<int>::iterator it;
		for(it=diners.begin();it!=diners.end();it++,cantidad--,total+=contador){
			if(*it!=anterior&&(*it)!=anterior+1){
		while((contador+1)*cantidad<(float)*it/(contador+2)){
			contador++;
			if(ceil((float)*it/(contador+1))<=mayor) break;
		}}
		if(mayor<ceil((float)*it/(contador+1)))mayor=ceil((float)*it/(contador+1));
		anterior=*it;
		}
		total+=mayor;
		cout<<"Case #"<<i<<": "<<total<<endl; 
	}
	return 0;
}

