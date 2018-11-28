#include<bits/stdc++.h>
using namespace std;
 vector< pair <int,int> >  board;
int arr[1001],n,ans=INT_MAX;
void  bfs(){
	set<  vector< pair<int,int> > > s;
	queue< pair<vector< pair<int,int> >,int> > q;
	q.push(make_pair(board,0));
	s.insert(board);
	int cl;
	vector< pair<int,int> > p;
	p.clear();
	while(!q.empty()){
		 p.clear();
		 p=q.front().first;
		 cl=q.front().second;
		 q.pop();
		 int mx=0;
		 //printf("%d\n",n);
		 for(int i=1;i<10;i++){
			 if(p[i].second>0)
			 mx=max(p[i].first,mx);

		 }
		 if(mx==0)return;
		 // printf("%d %d %d\n",mx,cl,p[mx].second);
		 ans=min(ans,mx+cl);
		 vector< pair<int,int> > ne;
		 ne=p;
		 for(int i=1;i<10;i++){
			 ne[i-1].second=ne[i].second;
		 }
		 if(s.find(ne)==s.end()){
			s.insert(ne);
			q.push(make_pair(ne,cl+1));

		}


		 for(int i=1;i<(10);i++){
			 if(p[i].second>0)
			 for(int j=p[i].first-1;j>=((p[i].first/2)+(p[i].first)%2) && j>0;j--){
			 vector< pair<int,int> > ne;
			 ne=p;
			 ne[j].second+=(ne[i].second);
			 (ne[p[i].first-j].second)+=(ne[i].second);
			 int add=ne[i].second;
			 ne[i].second=0;


			 if(s.find(ne)==s.end()){
				 s.insert(ne);
				 q.push(make_pair(ne,cl+add));

			 	 }
			 }
		 }
		/* vector< pair<int,int> > ne;
		 for(int i=0;i<10;i++){
			 ne.push_back(make_pair(p[i].first,p[i].second-1));
		 }
		 if(s.find(ne)==s.end()){
		 	s.insert(ne);
		 	q.push(make_pair(ne,cl+1));

		 }
		 */
	}

}
int main(){
	int t;
	scanf("%d",&t);
	int y=1;
	while(t--){
		scanf("%d",&n);
		board.clear();
		for(int i=0;i<10;i++){
			board.push_back(make_pair(i,0));
		}
		for(int i=0;i<n;i++){
			scanf("%d",&arr[i]);
			board[arr[i]].second++;
			//printf("%d",board[i]);
		}

		ans=INT_MAX;
		bfs();
		printf("Case #%d: %d\n",y,ans);
		y++;
	}
}
