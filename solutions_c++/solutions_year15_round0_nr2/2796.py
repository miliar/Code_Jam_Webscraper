#include<bits/stdc++.h>
#define ll long long

using namespace std;

bool checksol(vector<int> & vec, int p, int t)
{
	int req = 0;
	for(int i=0;i<vec.size();++i)
	{
		if(vec[i]>p-t){
			if(vec[i]%(p-t) == 0){
				req+=(vec[i]/(p-t))-1;
			}
			else{
				req+=(vec[i]/(p-t));
			}
		}
	}
	return req<=t;
}

bool isPoss(vector<int> & vals, int p)
{
	for(int t=0;t<p;++t)
	{
		if(checksol(vals,p,t)){return true;}
	}
	return false;
}

int main()
{
	int cases;
	cin>>cases;
	int d,p,ans;
	vector<int> vals;
	int l,r,mid;
	for(int i=0;i<cases;++i)
	{
		cin>>d;
		vals.clear();
		for(int j=0;j<d;++j){cin>>p; vals.push_back(p);}
		sort(vals.begin(), vals.end());
		r = vals[d-1];
		l = 0;
		while(l<r){
			mid = (l+r)/2;
			if(isPoss(vals,mid)){r=mid;}
			else l=mid+1;
		}
		cout<<"Case #"<<i+1<<": "<<r<<endl;
	}
	return 0;
}
