#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	FILE *f1, *f2;
	int i, j, k;
	char s[2001];
	int t;
	int cn = 1;
	int cnt = 1;
	int n;
	f1 = fopen("A-large (1).in","r");
	f2 = fopen("output.txt","w");
	fscanf(f1,"%d", &t);
	int a;
	pair <int,char> t1, t2;
	while(t--) {
		priority_queue <pair <  int, char> > pq;
		fscanf(f1, "%d", &n);
		for(i = 0; i < n; i++) {
			fscanf(f1, "%d", &a) ;
			pq.push(make_pair(a,(char)(i+65)));
		}
		fprintf(f2, "Case #%d: ", cnt++);
	/*	while(!pq.empty()) {
			cout<<pq.top().first<<pq.top().second<<" ";
			pq.pop();
					}*/
		while(!pq.empty()) {
			t1 = pq.top();
			pq.pop();
			if(t1.first == 1 && pq.size() == 2) {
				fprintf(f2, "%c ", t1.second);	
			}
			else {
			
			if(!pq.empty()) {
				
				t2 = pq.top();
				//pq.pop();
				
		//	cout<<"h";
		//	cout<<t1.first<<t1.second<<" ";
			if(t1.first == t2.first) {
				pq.pop();
				if(t1.first > 1)
					pq.push(make_pair(t1.first-1, t1.second));
				if(t2.first > 1)
					pq.push(make_pair(t2.first-1, t2.second));
				fprintf(f2, "%c%c ", t1.second,t2.second);
			}	else {
				if(t1.first > 1)
				pq.push(make_pair(t1.first-1, t1.second));
				fprintf(f2, "%c ", t1.second);
			}
			}
			else {
				
			}
			}
		}
		
		fprintf(f2,"\n");
	}
	
	return 0;
}
