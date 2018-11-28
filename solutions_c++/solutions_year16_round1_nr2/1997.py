#include <iostream>
#include <cstring>
using namespace std;

bool odd[3000];
bool v[3000];
int T,n,p1;

int main() {
#ifdef ONLINE_JUDGE

#else
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
#endif
	cin>>T;
	for (int ii=1; ii<=T; ii++) {
		cin>>n;
		memset(odd,0,sizeof(odd));
		memset(v,0,sizeof(v));
		for (int j=1; j<=2*n-1; j++)
			for (int i=1; i<=n; i++) {
				cin>>p1;
				if (!v[p1]) v[p1]=true;
				odd[p1]=!odd[p1];
			}
		cout<<"Case #"<<ii<<": ";
		for (int i=1; i<=2500; i++)
			if (v[i]&&odd[i]) cout<<i<<" ";
		cout<<endl;
	}

}
