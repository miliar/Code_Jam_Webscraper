#include <cstdio>
#include <iostream>

using namespace std;

int n,m;
int a[1001]; 

int main()
{
	freopen("Q2.in","r",stdin);
	freopen("Q2.out","w",stdout);
	cin>>m;
	for (int Case=1;Case<=m;Case++){
		cin>>n;
		for (int i=0;i<n;i++)
			cin>>a[i];
		int ans=1000;
		for (int i=1;i<=1000;i++){
			int maxn=0;
			int nowtot=0;
			for (int j=0;j<n;j++){
				int now=a[j]/i;
				int now2;
				if (a[j]-now*i==0) now--;
				nowtot+=now;
				if (i>a[j]) now2=a[j];else now2=i;
				if (now2>maxn) maxn=now2;
			}
			
			if (nowtot+maxn<ans) ans=nowtot+maxn;
		
		}
		cout<<"Case #"<<Case<<": "<<ans<<endl;
	}
} 
