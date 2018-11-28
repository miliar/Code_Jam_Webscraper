#include<bits/stdc++.h>
using namespace std;

int main()
{
	FILE *fp1,*fp2;
	fp1 = fopen("A-large.in","r");
	fp2 = fopen("output.txt","w");
	int t,n,cnt,mx;
	int p[30];
	priority_queue<pair<int,int> >que;
	pair<int,int>q,s;
	fscanf(fp1,"%d",&t);
	for(int j=1;j<=t;j++){
		fscanf(fp1,"%d",&n);
		cnt = 0;
		for(int i=0;i<n;i++){
			fscanf(fp1,"%d",&p[i]);
			que.push(make_pair(p[i],i));
			cnt += p[i];
		}
		fprintf(fp2,"Case #%d: ",j);
		//cnt = n;
		//cout<<"test "<<j<<endl;
		while(!que.empty()){
			q = que.top();
			que.pop();
			s = que.top();
			que.pop();
			cnt  =  cnt - 2;
			mx = max(q.first-1,s.first-1);
			if(!que.empty()){
			if(max(mx,que.top().first)>(cnt/2)){
				q.first = q.first-1;
				fprintf(fp2,"%c ",q.second+'A');
				cnt++;
				//cout<<q.second<<endl;
			}
			else{
				q.first = q.first-1;
				s.first = s.first - 1;	
				fprintf(fp2,"%c%c ",q.second+'A',s.second+'A');
				//cout<<q.second<<" "<<s.second<<endl;
			}
			}	
			else{
				if(mx>(cnt/2)){
					q.first = q.first-1;
				fprintf(fp2,"%c ",q.second+'A');
				cnt++;
				//cout<<q.second<<endl;
				}
				else{
				
				q.first = q.first-1;
				s.first = s.first - 1;	
				fprintf(fp2,"%c%c ",q.second+'A',s.second+'A');
				//cout<<q.second<<" "<<s.second<<endl;
			}
			}
			if(q.first!=0)
				que.push(q);
			if(s.first!=0)
				que.push(s);
		}
		fprintf(fp2,"\n");
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}
