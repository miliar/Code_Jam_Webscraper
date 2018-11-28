#include<cstdio>
#include<iostream>
#include<list>
#include<algorithm>
using namespace std;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w+",stdout);
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		cout<<"Case #"<<t+1<<": ";
		list<double> Naomi,Ken;
		int N;
		double aux;
		cin>>N;
		for(int i=0;i<N;i++){
			cin>>aux;
			Naomi.push_back(aux);
		} 
		for(int i=0;i<N;i++){
			cin>>aux;
			Ken.push_back(aux);
		}
		Naomi.sort();
		Ken.sort();
		Naomi.reverse();
		Ken.reverse();
		list<double> Naomi2,Ken2;
		Naomi2=Naomi;
		Ken2=Ken;
		//cout<<endl;
		int ptos=0;
		for(int i=0;i<N;i++){
			//for(list<double>::iterator it=Naomi2.begin();it!=Naomi2.end();it++) cout<<*it<<" ";
			//cout<<endl;
			//for(list<double>::iterator it=Ken2.begin();it!=Ken2.end();it++) cout<<*it<<" ";
			//cout<<endl;
			if(Naomi2.back()<Ken2.back()){
			    Naomi2.pop_back();
				Ken2.pop_front();
			}else{
				if(Naomi2.front()>Ken2.front()){
					Naomi2.pop_back();
					Ken2.pop_back();
					ptos++;
				}else{
					Naomi2.pop_back();
					Ken2.pop_front();
				}
			}
		}
		cout<<ptos<<" ";
		ptos=0;
		for(int i=0;i<N;i++){
			if(Naomi.front()>Ken.front()){
				ptos++;
				Naomi.pop_front();
				Ken.pop_back();
			}
			else{
				Naomi.pop_front();
				Ken.pop_front();
			}
		}
		cout<<ptos;
		cout<<endl;
	}
	fclose(stdin);
	fclose(stdout);
}
