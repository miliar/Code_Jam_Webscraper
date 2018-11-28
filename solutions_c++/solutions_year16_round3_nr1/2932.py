#include<bits/stdc++.h>
#define endl "\n"
using namespace std;
typedef long long ll;
int main(){
	ios_base::sync_with_stdio(0);
	int T;
	cin>>T;
	
	for(int x=1;x<=T;x++){
		int N;
		priority_queue<pair<int,char> > pq;
		cin>>N;
		ll tot=0;
		for(int i=1;i<=N;i++){
			int temp;
			cin>>temp;
			pq.push(make_pair(temp,'A'+i-1));
			tot+=temp;
		}
		cout<<"Case #"<<x<<": ";
		while(!pq.empty()){
			pair<int,char> ans=pq.top();
			pq.pop();
			if(!pq.empty()){
				pair<int,char> b=pq.top();
				pq.pop();
				double f2,ff2;
				if(tot>2)f2=(double)(b.first)/(tot-2);
				if(tot>1)ff2=(double)(b.first)/(tot-1);
				if(tot>2 && f2<=0.5){
					if(ans.first>=2){
						ans.first-=2;
						cout<<ans.second<<ans.second<<" ";
						if(ans.first>0)pq.push(ans);
						pq.push(b);
						tot-=2;
					}
					
				}
				else if(tot>1 && ff2<=0.5){
					if(ans.first>=1){
						ans.first-=1;
						cout<<ans.second<<" ";
						if(ans.first>0)pq.push(ans);
						tot-=1;
						pq.push(b);
					}
					
				}
				else{
					if(ans.first>=1 && b.first>=1){
						ans.first-=1;
						b.first-=1;
						tot-=2;
						if(ans.first>0)pq.push(ans);
						if(b.first>0)pq.push(b);
						cout<<ans.second<<b.second<<" ";
						}
					
				}

			}
			else{
				if(ans.first>=2){
					ans.first-=2;
					cout<<ans.second<<ans.second<<" ";
					if(ans.first>0)pq.push(ans);
					tot-=2;
				}
				else{
					ans.first-=1;
					cout<<ans.second<<" ";
					if(ans.first>0)pq.push(ans);
					tot-=1;
				}
			}

		}
		cout<<"\n";
		
	}
	return 0;
}