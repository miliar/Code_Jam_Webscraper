#include<iostream>
#include<algorithm>
using namespace std;

int s[1000],p[1000];

bool cmp(int x,int y){
	return s[x]<s[y];
}

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int n;
		cin>>n;
		for(int j=0;j<n;j++)
			cin>>s[j];
		for(int j=0;j<n;j++)
			p[j]=j;
		sort(p,p+n,cmp);
		int ans=0;
		for(int j=0;j<n;j++){
			int x=0;
			for(int k=0;k<p[j];k++) //slow
				if(s[k]>s[p[j]])
					x++;
			if(x < n-1-j-x)
				ans+=x;
			else
				ans+=n-1-j-x;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
