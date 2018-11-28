#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,p;
	scanf("%d",&t);
	for(p=1;p<=t;p++) {
		string st;
		scanf("\n");
		cin>>st;
		int l=st.length();
		int i,j,c=0;
		for(i=l-1;i>=0;i--) {
			if(st[i]=='-') {
				int j;
				c++;
				for(j=i;j>=0;j--) {
					if(st[j]=='+')
						st[j]='-';
					else
						st[j]='+';
				}	
			}
		}
		cout<<"Case #"<<p<<": "<<c<<endl;
	}
	return 0;
}
