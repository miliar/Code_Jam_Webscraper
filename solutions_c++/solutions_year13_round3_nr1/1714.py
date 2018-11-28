#include <cstdio>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
vector <int> v;
vector <int>::iterator it;
int tc,cn=1,n,len,k,cnt;
long long re;
char s[1000001],vw[]={'a','e','i','o','u'};
int main(void){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&tc);
	while(tc--){
		scanf("%s %d",s,&n);
		len=strlen(s);
		for(int i=0; i+n-1<len; i++){
			cnt=0;
			for(int j=0; j<n; j++){
				if(binary_search(vw,vw+5,s[i+j])==0)
					cnt++;
				else
					break;
			}
			if(cnt==n)
				v.push_back(i+n-1);
		}
		for(int i=0; i<len; i++){
			it=lower_bound(v.begin(),v.end(),i+n-1);
			if(it!=v.end()){
				re+=(long long)(len-*it);
			}
		}
		printf("Case #%d: %lld\n",cn,re);
		cn++;
		re=0;
		v.clear();
	}
	return 0;
}