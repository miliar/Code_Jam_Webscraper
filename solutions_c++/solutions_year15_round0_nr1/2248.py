#include <cstdio>
#include <iostream>

using namespace std;

int n,m;
string str; 

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	cin>>n;
	for (int Case=1;Case<=n;Case++){
		cin>>m;
		cin>>str; 
		int now=0,ans=0;
		for (int i=0;i<=m;i++)
			if (str[i]>'0'){
				if (i>now){
					int t=i-now;
					ans+=t;
					now+=t;
				}
				now+=str[i]-'0';
			}
		cout<<"Case #"<<Case<<": "<<ans<<endl;
	} 
} 
