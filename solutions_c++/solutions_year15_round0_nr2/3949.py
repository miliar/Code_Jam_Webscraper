//B
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
typedef vector<int> vi;
int r;
int result[10]={0,1,2,3,3,4,4,5,5,5};

void rec(priority_queue<int> pq,int q){			
	r = min(r,pq.top()+q);
	if(pq.top()<=3)return;
	for(int i=1;i<(pq.top()/2+1);i++){
		int n = pq.top()-i;
		int m = i;
		priority_queue<int> p(pq);
		p.pop();
		p.push(n);
		p.push(m);
		if(!(((p.top()%2)+p.top())/2+q>r))
		rec(p,q+1);
	}
}

int main(){
	int t;
	cin>>t;
	int n=t;
	while(t--){
		int d;
		cin>>d;
		priority_queue<int>pq;
		int m=0,x;				
		for(int i=0;i<d;i++){
			cin>>x;
			m = max(x,m);
			pq.push(x);
		}
		r = m;
		
		rec(pq,0);
		
		cout<<"Case #"<<n-t<<": "<<r<<endl;
	}
}
