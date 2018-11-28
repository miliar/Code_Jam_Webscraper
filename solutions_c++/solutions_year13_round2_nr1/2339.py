#include <iostream>
#include <algorithm>

using namespace std;

int main() {

//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);

	int i,j,l,t,res,a,n,sum,k,isum,c,ik;
	int m[101];

	cin>>t;
	for(i=0;i<t;i++) {
		res=0;
		cin>>a>>n;
		for (j=0;j<n;j++) cin>>m[j];
		if (a==1) {
			cout<<"Case #"<<i+1<<": "<<n<<endl;
			continue;
		}
		sort(m,m+n);
		sum=a;
		k=sum-1;
		j=0;
		while (j<n) {
			if (sum>m[j]) {
				sum+=m[j];
				j++;
				k=sum-1;
			}
			else
			{
				isum=sum;
				ik=k;
				c=0;
				while (isum<=m[j])
				{
					isum+=ik;
					c++;
					ik=isum-1;
				}
				if (c>n-j) {
					res+=(n-j);
					break;
				}
				else
				{
					res+=c;
					sum=isum;
					k=ik;
//					j++;
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}

	return 0;
}