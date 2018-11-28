#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int m,s[500001],r[500001],h[500001];
int ans;
void msort(int st,int ed){
    int i,mid=(st+ed)/2,p,q;
    if(st>=ed)
        return;
    msort(st,mid),msort(mid+1,ed);
    p=st,q=mid+1;
    for(i=st;i<=ed;i++)
        if(p>mid)
            r[i]=s[q++];
        else if(q>ed)
            r[i]=s[p++];
        else if(s[p]<s[q])
            r[i]=s[p++];
        else r[i]=s[q++],ans+=mid-p+1;
    for(i=st;i<=ed;i++)
        s[i]=r[i];
}
int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%d",&h[i]);
		
		int fin = 1e9;
		int p[20];
		for(int i=0;i<n;i++) p[i]=i;
		do{
			int a,b;
			for(a=1;a<n && h[p[a]]>h[p[a-1]];a++);
			for(b=n-2;b>=0 && h[p[b]]>h[p[b+1]];b--);
			if(a<=b) continue;
			ans = 0;
			for(int i=0;i<n;i++) s[i]=p[i];
			msort(0,n-1);
			if(fin>ans) fin =ans;
				
		} while ( std::next_permutation(p,p+n) );
		
		
		/*
		for(int i=0,j,k;i<=n;i++){
			int tmp = 0;
			ans = 0;
			for(j=0;j<i;j++)
				s[j] = h[j];
			msort(0, j-1);
			tmp += ans;
			ans = 0;
			for(j=0,k=n-1;k>=i;j++,k--)
				s[j] = h[k];
			msort(0, j-1);
			tmp += ans;
			
			if(fin > tmp) fin = tmp;
			int tmp1 = tmp;

			if( i>0 && i<n ){
				tmp = 1;
				ans = 0;
				for(j=0;j<i;j++)
					s[j] = h[j];
				s[j-1] = h[j];
				msort(0, j-1);
				tmp += ans;
				ans = 0;
				for(j=0,k=n-1;k>=i;j++,k--)
					s[j] = h[k];
				s[j-1] = h[k];
				msort(0, j-1);
				tmp += ans;
				if(fin > tmp) fin = tmp;
			}

			printf("%d: %d, %d\n", i, tmp1, tmp);
		}
		*/
        
        printf("Case #%d: %d\n", tt, fin);
    }
    return 0;
}

