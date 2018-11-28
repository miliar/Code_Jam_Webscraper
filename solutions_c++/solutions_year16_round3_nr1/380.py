#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<int,int>
#define F first
#define S second
#define MAXN 100005
#define MOD 1000000007


priority_queue<pair <int,char> > pq;

int a[MAXN];
int main(){
	int tt,t,n,i,sum;
	int tp;
	char ch;
	cin >>tt;
	for(t=1;t<=tt;t++) {
		cin >> n;
		while(!pq.empty())
			pq.pop();
		sum=0;
		for(i=0;i<n;i++){
			scanf("%d",a+i);
			sum+=a[i];
			pq.push(make_pair(a[i],'A'+i));
		}
		cout<<"Case #"<<t<<": ";
		while(!pq.empty()){
			ch=pq.top().second;
			tp=pq.top().first;
			printf("%c",ch);
			pq.pop();
			sum--;
			//printf(" --%d ",sum);
			if(tp>1)
				pq.push(make_pair(tp-1,ch));
			if(pq.empty())
				break;
			ch=pq.top().second;
			tp=pq.top().first;
			if(tp+tp>sum){
				printf("%c",ch);
				pq.pop();
				sum--;
				if(tp>1)
					pq.push(make_pair(tp-1,ch));
			}
			printf(" ");
		}
		puts("");
	}
	return 0;
}