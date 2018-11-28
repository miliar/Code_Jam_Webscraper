#include<iostream>
#include<algorithm>
#include<queue>
#include<utility>
#include<cstdio>

using namespace std;

struct comparator{
	bool operator()(pair<int,int> i,pair<int,int> j){
		return (i.second<j.second);
	}
};

pair<int,int> pt,p1,p2,p3;
priority_queue<pair<int,int>,vector< pair<int,int> >,comparator > pq;

int T,N,P[26];

int main(){
	cin>>T;
	for(int i=0;i<T;i++){
		fill_n(P,26*sizeof(int),0);
		cin>>N;
		for(int j=0;j<N;j++){
			cin>>P[j];
			pt.first=j;
			pt.second=P[j];
			pq.push(pt);
		}
		cout<<"Case #"<<i+1<<": ";
		/*while(!pq.empty()){
			pt=pq.top();
			pq.pop();
			cout<<pt.first<<":"<<pt.second<<" ";
		}*/
		while(!pq.empty()){
			if(pq.size()>=3){
				p1=pq.top();
				pq.pop();
				p2=pq.top();
				pq.pop();
				p3=pq.top();
				pq.pop();
				if(p1.second<p2.second)
					cout<<"ERROR";
				if(p1.second>p2.second){
					p1.second-=2;
					cout<<(char)(65+p1.first)<<(char)(65+p1.first)<<" ";
					if(p1.second>0)
						pq.push(p1);
					pq.push(p2);
					pq.push(p3);
				}
				else{
					if(p1.second>p3.second){
						p1.second--;
						p2.second--;
						cout<<(char)(65+p1.first)<<(char)(65+p2.first)<<" ";
						if(p1.second>0)
							pq.push(p1);
						if(p2.second>0)
							pq.push(p2);
						pq.push(p3);
					}
					else{
						if(p1.second==1){
							p1.second--;
							cout<<(char)(65+p1.first)<<" ";
						}
						else{
							p1.second-=2;
							cout<<(char)(65+p1.first)<<(char)(65+p1.first)<<" ";
						}
						if(p1.second>0)
							pq.push(p1);
						pq.push(p2);
						pq.push(p3);
					}
				}
			}
			else{
				if(pq.size()==2){
					p1=pq.top();
					pq.pop();
					p2=pq.top();
					pq.pop();
					if(p1.second>p2.second){
						p1.second-=2;
						cout<<(char)(65+p1.first)<<(char)(65+p1.first)<<" ";
						if(p1.second>0)
							pq.push(p1);
						pq.push(p2);
					}
					else{
						p1.second--;
						p2.second--;
						cout<<(char)(65+p1.first)<<(char)(65+p2.first)<<" ";
						if(p1.second>0)
							pq.push(p1);
						if(p2.second>0)
							pq.push(p2);
					}
				}
				else{
					p1=pq.top();
					pq.pop();
					if(p1.second>1){
						p1.second-=2;
						cout<<(char)(65+p1.first)<<(char)(65+p1.first)<<" ";
						if(p1.second>0)
							pq.push(p1);
					}
					else{
						cout<<(char)(65+p1.first)<<" ";
					}
				}
			}
		}
		cout<<"\n";
	}
	return 0;
}