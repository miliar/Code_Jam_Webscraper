#include <bits/stdc++.h>
using namespace std;
#define LL long long
#define INF 1000000000
#define pii pair<int,int>
#define vi vector<int>
#define mp make_pair
#define fi first
#define se second
#define pu push
#define pb push_back

int orang[1005];

int go(int pos){
	if(pos == 0)
		return 0;
	if(orang[pos] == 0)
		return go(pos-1);
	int ret = pos;
	int temp;
	for(int i = 1; i < pos; i++){
		temp = orang[pos];
		orang[pos-i]+=temp;
		orang[i]+=temp;
		orang[pos] = 0;
		ret = min(ret,go(pos-1)+temp);
		orang[pos-i]-=temp;
		orang[i]-=temp;
		orang[pos]=temp;
	}
	return ret;
}

int main(){
	int tc,n,temp,maks;
	cin>>tc;
	for(int zz=1; zz<=tc; zz++){
		memset(orang,0,sizeof(orang));
		maks=0;
		cin>>n;
		for(int i=0; i<n; i++){
			cin>>temp;
			orang[temp]++;
			maks=max(maks,temp);
		}
		cout<<"Case #"<<zz<<": "<<go(maks)<<endl;
	}
}
/*
1
10
6 6 6 6 6 6 6 6 6 16
*/