#include<cstdio>
using namespace std;
int c[5][5]={0};
int change(char ch){
    if(ch=='i') return 2;
    if(ch=='j') return 3;
    if(ch=='k') return 4;
}
int main(){
    freopen("a.in","r",stdin);
    freopen("b.txt","w",stdout);
    int T,L,X,kase=0;
    char s[10010],ts[10010];
    int a[10010],b[10010],aa[10010],bb[10010];
    c[1][1]=1; c[1][2]=2; c[1][3]=3; c[1][4]=4;
    c[2][1]=2; c[2][2]=-1; c[2][3]=4; c[2][4]=-3;
    c[3][1]=3; c[3][2]=-4; c[3][3]=-1; c[3][4]=2;
    c[4][1]=4; c[4][2]=3; c[4][3]=-2; c[4][4]=-1;
    scanf("%d",&T);
    while(T--){
	int cnt1=0,cnt2=0;
	scanf("%d%d%s",&L,&X,ts);
	for(int i=0,j=0;i<L*X;i++){
	    s[i]=ts[j];
	    j++;
	    if(j==L) j=0;
	}//copy
	
	a[0]=change(s[0]);
	if(a[0]==2) aa[cnt1++]=0;
        for(int i=1;i<L*X;i++){
            int num=change(s[i]);
	    if(a[i-1]<0){
		a[i]=-c[-a[i-1]][num];
	    }else{
		a[i]=c[a[i-1]][num];
	    }
	    if(a[i]==2) aa[cnt1++]=i;
	}//prefix
	
	b[L*X-1]=change(s[L*X-1]);
	if(b[L*X-1]==4) bb[cnt2++]=L*X-1;
	for(int i=L*X-2;i>=0;i--){
	    int num=change(s[i]);
	    if(b[i+1]<0){
		b[i]=-c[num][-b[i+1]];
	    }else{
		b[i]=c[num][b[i+1]];
	    }
	    if(b[i]==4) bb[cnt2++]=i;
	}//suffix
        bool flag=false;
        for(int i=0;i<cnt1;i++)
	    for(int j=0;j<cnt2;j++){
		int num1=aa[i],num2=bb[j]-1;
		int node=1;
		if(a[num1]<0){
		    a[num1]=-a[num1];
		    node*=-1;
		}
		if(num1+1<=num2 && c[a[num1]][3]==a[num2]*node){
	             flag=true;
	             break;	
		}
	    }
	if(flag) printf("Case #%d: YES\n",++kase);
	else printf("Case #%d: NO\n",++kase);
    }
    return 0;
}
