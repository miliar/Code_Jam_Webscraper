#include<bits/stdc++.h>
using namespace std;
struct q{
	int x;
	int y;
};
bool comp(struct q q1,struct q q2){
	return q1.x>q2.x;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("outputAlarge.in","w",stdout);
	int t,i,j,T,n,m;
	string mm;
	string d="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	cin>>T;
	for(t=1;t<=T;++t){
		cin>>n;
		struct q a[n];
		vector<string> v;
		int sum=0;
		for(i=0;i<n;++i){
			cin>>a[i].x;
			a[i].y=i;
			sum+=a[i].x;
		}
		sort(a,a+n,comp);
		while(sum!=0)
		{
			i=0;
			mm="";
				if(sum%2!=0 && (a[1].x)<=(sum-1)/2 && (a[0].x-1)<=(sum-1)/2)
                 {
                 	mm+=d[a[0].y];
                	a[0].x-=1;
                	sum-=1;
                 }
				else if((a[0].x-1)>(sum-2)/2)
                {
                	mm+=d[a[0].y];
                	mm+=d[a[0].y];
                	a[0].x-=2;
                	sum-=2;
                }
                else{
                	mm+=d[a[0].y];
                	mm+=d[a[1].y];
                	a[0].x-=1;
                	a[1].x-=1;
                	sum-=2;
                }
			//cout<<mm<<" ";
			sort(a,a+n,comp);
			v.push_back(mm);
		}
		cout<<"Case #"<<t<<": ";
		for(i=0;i<v.size();++i)
		{
			cout<<v[i]<<" ";
		}
		cout<<endl;
	}
	return 0;
}
