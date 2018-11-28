#include<iostream>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
using namespace std;

bool correctWar(vector<double> &v, vector<double> &w){
	return v[0] > w[int(w.size())-1];
}

bool correctDWar(vector<double> &v, vector<double> &w){
	for(int i=0;i<int(v.size());i++){
		if(w[i] > v[i] ) return false;
	}
	return true;
}

int main(){
	int T; cin>>T;
	for(int kases = 1;kases<=T;kases++){
		int N; cin>>N;
		vector<double> f1(N,0.0),f2(N,0.0),d1(N,0.0),d2(N,0.0);	
		for(int i=0;i<N;i++) cin>>f1[i];
		for(int i=0;i<N;i++) cin>>f2[i];
		sort(f1.begin(),f1.end());
		sort(f2.begin(),f2.end());
		d1 = f1;
		d2 = f2;
		int sd = 0, sw = 0;
		double cw;
		for(int round = 0;round<N;round++){
			if(correctWar(f1,f2) && sw == 0){
				sw = int(f1.size());
			}
			else{
				cw = f1[0];
				f1.erase(f1.begin());
				for(int p=0;p<int(f2.size());p++){
					if(f2[p] > cw){
						f2.erase(f2.begin()+p);
						break;
					}
				}
			}
			if(correctDWar(d1,d2) && sd == 0){
				sd = int(d1.size());
			}
			else{				
				d1.erase(d1.begin());
				d2.erase(--d2.end());
			}
		}
		cout<<"Case #"<<kases<<": "<<sd<<" "<<sw<<endl;
	}
}
