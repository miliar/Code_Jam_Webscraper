#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <functional>
using namespace std;

bool okay(vector<pair<int,int> > p){
		for(int i=0;i<p.size();++i){
			if(p[i].first>0)return false;
		}
		return true;
	}
	bool majority(vector<pair<int,int> > parties){
		double sum=0;
		for(int i=0;i<parties.size();++i){
			sum+=parties[i].first;
		}
		sum--;
		for(int i=0;i<parties.size();++i){
			if(parties[i].first == 0)continue;
			if(sum == 0)continue;
			if((double)(parties[i].first / sum) * 100 > 50){
				return true;
			}
		}
		return false;
	}

	class index{
	public:
		bool operator()(const pair<int,int> & a, const pair<int,int> & b){
			return a.second < b.second;
		}
	};

int main(){
	int T = 0;
	cin>>T;
	for(int times = 1; times <= T; ++times){
		int N;
		cin>>N;
		vector<pair<int,int> > parties(N);
		string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		for(int i=0;i<N;++i){
			int s;
			cin>>s;
			parties[i]=make_pair(s, i);
		}
		string res="";
		while(!okay(parties)){
			sort(parties.begin(),parties.end());
			reverse(parties.begin(), parties.end());
			if(majority(parties)==false){
				if(parties[0].first>0){res += alphabet[parties[0].second];
					parties[0].first--;
					res+=' ';
				}
			}
			else{
				if(parties[0].first>0){res += alphabet[parties[0].second];
					parties[0].first--;

				}
				if(parties[1].first>0){
					res += alphabet[parties[1].second];
					parties[1].first--;
				}
				else{
					cout<<"*************"<<endl;
				}
				res+=' ';
			}
			sort(parties.begin(), parties.end(), index());			
		}
		cout<<"Case #"<<times<<": "<<res<<endl;
	}
	return 0;
}
