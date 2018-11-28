#include<bits/stdc++.h>
using namespace std;

struct node{
	char index;
	int value;
};

bool cmpr(node a, node b)
{
	return a.value<b.value;
}

node p[26];

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("C:/Users/HP/Desktop/codejam/1A_input.txt","r",stdin);//redirects standard input
	freopen("C:/Users/HP/Desktop/codejam/1A_output.txt","w",stdout);//redirects standard output
	int t,n;
	cin>>t;
	for(int tc=1; tc<=t; tc++)
	{
		for(int i=0; i<26; i++)
		{
			p[i].value=0;
		}
		cin>>n;
		for(int i=0; i<n; i++)
		{
			cin>>p[i].value;
			p[i].index=char(i+65);
		}
		sort(p,p+n,cmpr);
		cout<<"Case #"<<tc<<": ";
		for(int i=n-1; i>=2; i--)
		{
			for(int j=i; j<n; j++)
			{
				while(p[j].value!=p[i-1].value) {
					cout<<p[j].index<<" ";
					p[j].value--;
				}
			}
		}
		/*for(int i=2; i<n; i++)
		{
			while(p[i].value!=0) {
				cout<<p[i].index<<" ";
				p[i].value--;
			}
		}*/
		if(n%2==0) {
			for(int i=n-1; i>=2; i-=2)
			{
				while(p[i].value!=0 && p[i-1].value!=0) {
					cout<<p[i].index<<p[i-1].index<<" ";
					p[i].value--;
					p[i-1].value--;
				}
			}
		}
		else {
			/*while(p[n-1].value!=0) {
				cout<<p[n-1].index<<" ";
				p[n-1].value--;
			}*/
			for(int i=n-1; i>=2; i-=2)
			{
				while(p[i].value!=0 && p[i-1].value!=0) {
					if(i==2) {
						if(p[i-1].value==p[0].value) break;
					}
					cout<<p[i].index<<p[i-1].index<<" ";
					p[i].value--;
					p[i-1].value--;
					
				}
			}
			while(p[2].value!=0) {
				cout<<p[2].index<<" ";
				p[2].value--;
			}
		}
		while(p[1].value!=p[0].value) {
			cout<<(p[1].index)<<" ";
			p[1].value--;
		}
		while(p[0].value!=0) {
			cout<<(p[0].index)<<(p[1].index)<<" ";
			p[0].value--;
		}
		cout<<endl;
	}
	
	return 0;
}
