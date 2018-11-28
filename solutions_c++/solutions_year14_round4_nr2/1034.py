#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
const int N=1010;
int n,x;
struct unit{
	int x,y;
	unit(int _x=0,int _y=0):x(_x),y(_y){}
	bool operator<(const unit &A)const{
		if(x==A.x)return y<A.y;
		return x<A.x;
	}
};
unit a[N];
unit b[N];
bool cmp(unit a,unit b)
{
	if(a.x==b.x)return a.y<b.y;
	else return a.x>b.x;
}
int main()
{
    int T;
    int index=0;
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&T);
    
	while(T--){
        index++;
        scanf("%d",&n);
        int tmp;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&tmp);
			a[i]=unit(tmp,i);
		}
		int sum=0;
		int l=0,r=n;
		for(int i=0;i<n;i++)b[i]=a[i];
		sort(a,a+n);
		for(int i=0;i<n;i++)
		{
			//for(int j=l;j<r;j++)printf("%d ",b[j].x);puts("");
			for(int j=l;j<r;j++){
				if(b[j].x==a[i].x)
				{
					//printf("%d\n",b[j].x);
					if(j-l<=(r-1-j)){
						for(int k=j;k>l;k--)swap(b[k],b[k-1]);
						
						//printf("!%d\n",j-l);
						sum+=j-l;
						l++;
					}
					else{
						for(int k=j;k<r-1;k++)swap(b[k],b[k+1]);
						
						sum+=r-1-j;//printf("~%d\n",r-1-j);
						r--;
					}
				}
			}
		}
		printf("Case #%d: %d",index,sum);
        puts("");
    }
}
