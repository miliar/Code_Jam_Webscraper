#include <iostream>
#include <stdio.h>
#include <map>

using namespace std;

int n;
int x,times;
map<int,int> h;

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>times;
	for (int ti=1;ti<=times;ti++){
		cin >> n;
		h.clear();
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++){
				cin>>x;
				if (i==n) h[x]++;
			}
		cin >> n;
		int ans=0,cnt;
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++){
				cin>>x;
				if (i==n)
					if (h[x]){ans++;cnt=x;}
			}
		cout<<"Case #"<<ti<<": ";
		if (ans>1) cout<<"Bad magician!"<<endl;
		if (ans==0) cout<<"Volunteer cheated!"<<endl;
		if (ans==1) cout<<cnt<<endl;
	}
	return 0;
}
