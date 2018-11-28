#include<iostream>
#include<algorithm>

using namespace std;

int main()
{

	long long i,j,k,t,m,n,c,flag,f,sz2,ans,sz,a[1000]={0},prev,minprev,term;

	cin>>t;
	k=t;
	while(t--) {
		
		cin>>sz>>n;
		f=0;c=0;ans=0;prev=0;term=99999;

		for(i=0;i<n;i++) {

			cin>>a[i];
		}
			sort(a,a+n);

			for(i=0;i<n;i++) {
				c=0;prev= -1;f=0;
				term = min(term,ans+n-i);

				if(sz>a[i]) {
					sz += a[i];
				}
				else {
				
					sz2=sz;
					//cout<<sz<<" a[i] "<<a[i]<<endl;
					while(sz2<=a[i]) {
						sz2 += (sz2-1);
						if(sz2==prev) { f=1; break; }
						c++;
						prev=sz2;
					}
				//	cout<<i<<" "<<c<<" n: "<<n-i<<" sz "<<sz<<endl;
					if(c>(n-i)) {ans += n-i;break;}
					else{ sz =sz2+a[i]; ans+=c; if(f==1) sz -= a[i]; }
					minprev = ans;

				}
			}
			
				cout<<"Case #"<< k-t <<": "<<min(term,ans)<<endl;
				for(i=0;i<=n;i++)
					a[i]=0;
			}

	return 0;
}

