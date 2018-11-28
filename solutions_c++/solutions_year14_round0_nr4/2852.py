#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int n,re[2];
double a[1001],b[1001];
vector <double> v;
vector <double>::iterator it;
int tc,tcn;
int main(void){
	//freopen("D-large.in","r",stdin);
	//freopen("output.txt","w",stdout);
	scanf("%d",&tc);
	while(tc--){
		scanf("%d",&n);
		for(int i=0; i<n; i++)
			scanf("%lf",&a[i]);
		for(int i=0; i<n; i++)
			scanf("%lf",&b[i]);
		re[0]=re[1]=0;
		sort(a,a+n);
		sort(b,b+n);
		for(int i=0; i<n; i++)
			v.push_back(b[i]);
		for(int i=0; i<n; i++){
			it=lower_bound(v.begin(),v.end(),a[i]);
			if( it != v.begin() )
				it--;
			if( (*it) < a[i] ){
				re[0]++;
				v.erase(it);
			}
		}
		v.clear();
		for(int i=0; i<n; i++)
			v.push_back(b[i]);
		for(int i=0; i<n; i++){
			it=upper_bound(v.begin(),v.end(),a[i]);
			if( it == v.end() )
				re[1]++;
			else{
				v.erase(it);
			}
			
		}
		v.clear();
		printf("Case #%d: %d %d\n",++tcn,re[0],re[1]);
	}
	return 0;

}