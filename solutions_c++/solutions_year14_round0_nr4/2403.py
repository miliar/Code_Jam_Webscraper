#include <bits/stdc++.h>
using namespace std;
int main()
{
//	freopen("in4.txt","r",stdin);
//	freopen("out4.txt","w",stdout);
	int test,it;
	scanf("%d",&test);
	for( it = 1; it <= test; it++ ){
		int n,i,j,x,ans1 = 0,ans2 = 0;
		scanf("%d",&n);
		double a[n],b[n],c[n];
		for(i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for(i=0;i<n;i++)
			scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		for(i=0;i<n;i++){
			c[i]=b[i];
		}
		/*cout<<endl;
		for(i=0;i<n;i++)
		cout<<a[i]<<" ";
		cout<<endl;
		for(i=0;i<n;i++)
		cout<<b[i]<<" ";
		cout<<endl;
		cout<<endl;*/
		
		for(i=n-1;i>=0;i--){
			bool found = false;
			int idx=-1;
			for(j=n-1;j>=0;j--){
				if(c[j]!=-1&&c[j]>a[i]){
					found = true;
					idx = j;
				}
				else if(c[j]!=-1){
					break;
				}
			}
			ans2++;
			if(found){
				c[idx] = -1;
				ans2--;
			}
			else{
				j = 0;
				while(j<n&&c[j]!=-1)
				j++;
				c[j]=-1;
			}
		}
		j = 0;
		i = 0;
		while(i<n&&j<n){
			if(a[i]>b[j]){
				i++;
				ans1++;
				j++;
			}
			else i++;
		}
		
		printf("Case #%d: %d %d\n",it,ans1,ans2);
	}
	return 0;
}
