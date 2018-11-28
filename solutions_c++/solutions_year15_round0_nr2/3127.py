/*#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

typedef __int64 ll;
ll dp[55];

int main()
{
	int t;
	scanf("%d",&t);
	while(t--){
        memset(dp,0,sizeof(dp));
        int a,b;
        scanf("%d%d",&a,&b);
        dp[a]=1;
        for(int i=a+1;i<=b;i++){
            dp[i]=dp[i-1]+dp[i-2];
        }
        printf("%I64d\n",dp[b]);
	}
	return 0;
}*/

/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

int get(int a,int b)
{
    if(a>b)swap(a,b);
    for(int i=a;;i+=a){
        if(i%b==0)return i;
    }
}

int main()
{
    int n;
    while(scanf("%d",&n)!=EOF){
        int pre=1;
        for(int i=0;i<n;i++){
            int v;
            scanf("%d",&v);
            pre=get(pre,v);
        }
        printf("%d\n",pre);
    }
    return 0;
}*/
/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

typedef __int64 ll;
ll dp[55][2];

int main()
{
    memset(dp,0,sizeof(dp));
    dp[1][1]=dp[1][0]=1;
    for(int i=2;i<=50;i++){
        dp[i][1]=dp[i-1][0]+dp[i-1][1];
        dp[i][0]=dp[i-1][1];
    }
    int n;
    while(scanf("%d",&n)!=EOF){
            printf("%I64d\n",dp[n][1]);
    }
    return 0;
}*/
/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

const double eps=1e-5;

int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        double n;
        scanf("%lf",&n);
        double si=1;
        double ans=0;
        int cnt=0;
        for(int i=0; ; i++){
            cnt++;
            double temp=pow(n,i*2+1);
            double mu=1;
            for(int j=1;j<=i*2+1;j++)mu*=j;
            temp=temp/mu;
            ans+=si*temp;
            si=-si;
            if(fabs(temp)<eps){
                break;
            }
        }
        printf("%.2lf\n",ans);
        printf("%d\n",cnt);
    }
    return 0;
}*/

/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        double r;
        scanf("%lf",&r);
        printf("%.6lf\n",3.141592653*r*r);
    }
    return 0;
}*/
/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        double n;
        scanf("%lf",&n);
        double ans=0;
        if(n<=100000){
            ans=n*0.1;
        }
        else if(n<=200000){
            ans=100000*0.1+(n-100000)*0.075;
        }
        else if(n<=400000){
            ans=100000*0.1+100000*0.075+(n-200000)*0.05;
        }
        else if(n<=600000){
            ans=100000*0.1+100000*0.075+200000*0.05+(n-400000)*0.03;
        }
        else if(n<=1000000){
            ans=100000*0.1+100000*0.075+200000*0.05+200000*0.03+(n-600000)*0.015;
        }
        else {
            ans=100000*0.1+100000*0.075+200000*0.05+200000*0.03+400000*0.015+(n-1000000)*0.01;
        }
        printf("%.2lf\n",ans);
    }
    return 0;
}*/

/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){

        int ans=0;
        for(int j=1;j<i;j++){
            if(i%j==0){
                ans+=j;
            }
        }
        if(ans==i){
            printf("%d\n",ans);
        }
    }
    return 0;
}*/


/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=0;j<n-i;j++)printf(" ");
        for(int j=1;j<i*2;j++)printf("#");
        printf("\n");
    }
    return 0;
}*/
/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    double n;
    scanf("%lf",&n);
    double ans1=n;
    for(int i=2;i<=10;i++){
        n/=2;
        ans1+=n*2;
    }
    n/=2;
    printf("%.8lf %.8lf\n",ans1,n);
    return 0;
}*/
/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

typedef long long ll;
ll k,n;
ll goal;

void dfs(ll pre,int now,int cent)
{
    if(k==0)return;
    if(now>=cent){
        if(pre%n==0){
            k--;
            if(k==0)goal=pre;
        }
        return;
    }

    if(now<=1){
        ll tem=pre%10;
        for(int i=1-now;i<10;i++)if(i!=tem)dfs(pre*10+i,now+1,cent);
    }
    else {
        ll tem1=pre%10;
        ll tem2=pre/10%10;
        int ok = tem1>tem2 ? 1:0;
        if(ok)
        for(int i=0;i<tem1;i++)dfs(pre*10+i,now+1,cent);
        else for(int i=tem1+1;i<10;i++)dfs(pre*10+i,now+1,cent);
    }
}

int main()
{
    cin>>n>>k;

    for(int i=1;i<=13;i++){
        printf("%d\n",i);
        dfs(0,0,i);
        if(k==0)break;
    }
    cout<<goal<<endl;
    return 0;
}
*/
/*
#include <iostream>
using namespace std;

int main()
{
    int a[15],t,x,i,j,temp;
    cin>>t;
    while(t--){
        for(i=0;i<10;i++)
            cin>>a[i];
        cin>>x;
        int issame=-1;
        int isodd= (x%2==0 ? 0 : 1);
        for(i=0;i<10;i++)
            if(a[i]==x){
                issame=i;
                break;
            }
        if(isodd==1&&issame!=-1){
            a[issame]=a[9];
            for(i=0;i<8;i++){
                for(j=0;j<8-i;j++){
                if(a[j]>a[j+1]){
                    temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
                }
            }
            for(i=0;i<8;i++)
                cout<<a[i]<<' ';
            cout<<a[8]<<endl;
        }
        else if(isodd==0&&issame==-1){
            a[10]=x;
            for(i=0;i<10;i++){
                for(j=0;j<10-i;j++){
                if(a[j]<a[j+1]){
                    temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
                }
            }
            for(i=0;i<10;i++)
                cout<<a[i]<<' ';
            cout<<a[10]<<endl;
        }
        else {
            for(i=0;i<9;i++){
                for(j=0;j<9-i;j++){
                if(a[j]<a[j+1]){
                    temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
                }
            }
            int ans[15],sz=0;
            for(i=0;i<10;i++){
                if(a[i]%2!=0)   //注意:负奇数%2=-1
                    ans[sz++]=a[i];
            }
            for(i=0;i<10;i++){
                if(a[i]%2==0)
                    ans[sz++]=a[i];
            }
            for(i=0;i<9;i++)
                cout<<ans[i]<<' ';
            cout<<ans[9]<<endl;
        }
    }
    return 0;
}*/


/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

int a[105];

int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%d",&a[i]);
        a[i]=a[i]+a[i-1];
    }
    int L,R;
    scanf("%d%d",&L,&R);
    printf("%d\n",a[R]-a[L-1]);
    return 0;
}*/

/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

const int INF = (~0U>>1);

int main()
{
    int n,id,mx=-INF;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        int val;
        scanf("%d",&val);
        if(mx<val){
            mx=val;
            id=i;
        }
    }
    printf("%d %d\n",mx,id);
    return 0;
}*/

/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

const int INF = ~0U>>1;  //这个值其实是2^31-1,int能存储的最大的值
const int MAXN = 1005;  //点的最大数量,可以调整
const int MAXM = 1005;  //边的最大数量,可以调整
int head[MAXN];
int edgefrom[MAXM<<1];
int edgeto[MAXN<<1];
int w[MAXM<<1];
int next[MAXN<<1];
int esz;
int fa[MAXN];
int n,m;
vector< pair<int,int> >q;
vector<int>res;

void init()   //初始化
{
    memset(head,-1,sizeof(head));  //边的存储是用邻接表实现的,保证高效
    esz=0;
    q.clear();
    res.clear();
    for(int i=1;i<=n;i++)   //初始化并查集
        fa[i]=i;
}

void addedge(int u,int v,int val)
{
    edgefrom[esz]=u;
    edgeto[esz]=v;
    w[esz]=val;
    next[esz]=head[u];
    head[u]=esz++;
}

int mfind(int x)
{
    if(x==fa[x])return x;
    return fa[x]=mfind(fa[x]);
}

int main()
{
    int t;
    scanf("%d",&t);  //测试组数
    while(t--){
        scanf("%d%d",&n,&m);  //n为点数, m为边数
        init();
        for(int i=0;i<m;i++){
            int u,v,val;
            scanf("%d%d%d",&u,&v,&val);   //输入每条边的两个端点u和v,以及边的权值val
            addedge(u,v,val);    //将边加入图中
            addedge(v,u,val);     //由于图是双向图,所以v也能到u,要加入反向边
        }
        int ans=0;
        for(int u=1;u<=n;u++){    //对图中的每个点，选一个与其关联且最小权值的边加入MST
            int Min=INF;    //先默认边的权值为无穷大
            int id=-1;     //默认边的id为-1
            for(int j=head[u];j+1;j=next[j]){   //遍历与u关联的所有边，这里的j为边的id
                int v=edgeto[j];          //访问边u,v
                int val=w[j];             //读取边的权值val
                if(Min>val){    //如果当前的边权比我之前的要小，则更新为当前较小的
                    Min=val;      //更新
                    id=j;         //同时标记最小边的id
                }
            }
            if(id==-1)continue;     //如果id为-1,则不存在任何与u关联的边,后面的也不用做了
            int fa_u=mfind(edgefrom[id]);   //并查集,可以不理解,其实就是判断边id的两个端点在不在MST里
            int fa_v=mfind(edgeto[id]);
            if(fa_u!=fa_v){   //不在MST
                fa[fa_u]=fa_v;   //将边id的两个端点加入MST
                ans+=Min;         //MST的权值加Min
                res.push_back(id);   //存储MST的边id,res为最小生成树的边的集合
            }
        }
        for(int u=1;u<=n;u++){      //遍历整张图的所有边
            for(int j=head[u];j+1;j=next[j]){
                int v=edgeto[j];
                int fa_u=mfind(u);
                int fa_v=mfind(v);
                if(fa_u!=fa_v)    //找到可以连接两颗不同子树的边
                    q.push_back(make_pair(w[j],j));  //q是一个可以连接两颗不同子树的边的集合
            }
        }
        sort(q.begin(),q.end());  //将边从小到大排序
        int L=q.size();
        for(int i=0;i<L;i++){
            pair<int,int>temp=q[i];
            int id=temp.second;
            int u=edgefrom[id];
            int v=edgeto[id];
            int fa_u=mfind(u);
            int fa_v=mfind(v);
            if(fa_u!=fa_v){     //依次从小到大选取q中的边加入MST
                fa[fa_u]=fa_v;
                ans+=w[id];
                res.push_back(id);  //存储MST的边id,res为最小生成树的边的集合
            }
        }
        L=res.size();
        if(L!=n-1){     //如果MST中的边数不是n-1,则一定不存在最小生成树
            printf("最小生成树不存在!\n");
            continue;
        }
        printf("最小生成树的权值是: %d\n",ans);
        printf("最小生成树的边是:\n");
        for(int i=0;i<n-1;i++){
            printf("%d %d %d\n",edgefrom[res[i]],edgeto[res[i]],w[res[i]]);  //输出MST的每条边
        }
    }
    return 0;
}*/

/*
#include <iostream>
using namespace std;

int isprime(int x)
{
    if(x<2)return 0;
    int i;
    for(i=2;i<x;i++)
        if(x%i==0)return 0;
    return 1;
}

int fx(int x)
{
    int i,j,cnt=0;
    for(i=2;i<x;i++){
        if(isprime(i)==0)continue;
        j=x-i;
        if(j<i)break;
        if(isprime(j)==1)
                cnt++;
    }
    return cnt;
}

int main()
{
    int x;
    cin>>x;
    cout<<fx(x)<<endl;
    return 0;
}
*/

/*
#include <iostream>
using namespace std;

void my_sort(int a[],int l,int r)
{
    int i,j,temp;
    for(i=l;i<r-1;i++){
        for(j=l;j<r-(i-l+1);j++)
        if(a[j]>a[j+1]){
            temp=a[j];
            a[j]=a[j+1];
            a[j+1]=temp;
        }
    }
}

int main()
{
    int a[1005];
    int n,i;
    cin>>n;
    for(i=0;i<n;i++)
        cin>>a[i];
    my_sort(a,0,n);
    for(i=0;i<n-1;i++)
        cout<<a[i]<<' ';
    cout<<a[n-1];
    return 0;
}
*/
/*
#include <iostream>
using namespace std;

int fx(int x)
{
    if(x<0)return x;
    return x*x;
}

int main()
{
    int t,x;
    cin>>t;
    while(t--){
        cin>>x;
        cout<<fx(x)<<endl;
    }
    return 0;
}*/

/*
#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
void Josegf(int m,int n,int a[30])
{
   int i,k,j;
   int b[30];
   i=-1;
   k=1;
   while(1)
   {
     for(j=0;j<n;)
	 {
	    i=(i+1)%m;
		if(a[i]!=0)
			j++;
	 }
	if(k==m) break;
		 printf("%d ",a[i]);
			 a[i]=0;

		 k++;
   }

}

int main()
{
 int m,n,i,j,t;
 int a[30],b[30];
 scanf("%d",&t);
 for(j=0;j<t;j++)
 {
	 scanf("%d%d",&m,&n);
 for(i=0;i<m;i++)
	 a[i]=i+1;
Josegf(m,n,a);

for(i=0;i<m;i++)if(a[i]!=0){
 printf("%d\n",a[i]);
 break;
}
 }
return 0;

}*/

/*
#include <iostream>
#include <cstring>
using namespace std;

void mstrcpy(char s2[],char s1[])
{
    int i,L=strlen(s1);
    for(i=0;i<L;i++)s2[i]=s1[i];
    s2[i]='\0';
}

int main()
{
    char s1[100],s2[100];
    int t;
    cin>>t;
    while(t--){
    cin>>s1;
    mstrcpy(s2,s1);
    cout<<s2<<endl;
    }
    return 0;
}*/

/*
#include <iostream>
#include <cstring>
using namespace std;

int mstrlen(char s[])
{
    int i,cnt=0;
    for(i=0;s[i]!='\0';i++)
        cnt++;
    return cnt;
}

int main()
{
    int t;
    char s[100];
    cin>>t;
    while(t--){
    cin>>s;
    cout<<mstrlen(s)<<endl;
    }
    return 0;
}*/

/*
#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    char s[100];
    int t,i;
    cin>>t;
    getchar(); //过滤掉t之后的回车
    while(t--){
    gets(s);
    int lettercnt=0,numcnt=0,othercnt=0;
    for(i=0;s[i];i++){
        if(s[i]>='0' && s[i]<='9')numcnt++;
        else if(s[i]>='A' && s[i]<='Z' || s[i]>='a' && s[i]<='z')lettercnt++;
        else othercnt++;
    }
    cout<<lettercnt<<' '<<numcnt<<' '<<othercnt<<endl;
    }
    return 0;
}
*/

/*
#include <iostream>
using namespace std;

int main()
{
    int i,j,n,m,a[100][100];
    cin>>n>>m;
    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
            cin>>a[i][j];
    for(i=0;i<m;i++){
        for(j=0;j<n-1;j++)
            cout<<a[j][i]<<' ';
        cout<<a[j][i]<<endl;
    }
    return 0;
}
*/
/*
#include <iostream>
using namespace std;

int main()
{
    int i,j,n,m,a[100][100],b[100][100];
    cin>>n>>m;
    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
            cin>>a[i][j];
    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
            cin>>b[i][j];
    for(i=0;i<n;i++){
        for(j=0;j<m-1;j++)
            cout<<a[i][j]+b[i][j]<<' ';
        cout<<a[i][j]+b[i][j]<<endl;
    }
    return 0;
}*/

/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

typedef long long ll;
const int MOD = (int)1e9+7;
int dp[55][55];
int C[55][55];
int po[55];

int add(int x,int y)
{
    x+=y;
    if(x>=MOD)x-=MOD;
    return x;
}

int sub(int x,int y)
{
    x-=y;
    if(x<0)x+=MOD;
    return x;
}

int mul(int x,int y)
{
    x=(ll)x*y%MOD;
    return x;
}

void getC(int n)
{
    memset(C,0,sizeof(C));
    C[0][0]=1;
    for(int i=0;i<=n;i++){
        C[i][0]=C[i][i]=1;
        for(int j=1;j<i;j++){
            C[i][j]=add(C[i-1][j] , C[i-1][j-1]);
        }
    }
}

void getpow()
{
    po[0]=1;
    for(int i=1;i<=50;i++)po[i]=po[i-1]*2%MOD;
}

int main()
{
    int n,m;
    getC(50);
    getpow();
    while(scanf("%d%d",&n,&m)!=EOF){
        memset(dp,0,sizeof(dp));
        dp[0][0]=1;
        for(int i=1;i<=n;i++)
            for(int j=0;j<=m;j++)
                for(int k=0;k<=m-j;k++){
                        if(k==0)dp[i][j]=add(dp[i][j] , mul(dp[i-1][j],sub(po[j],1)));
                        else dp[i][j+k]=add(dp[i][j+k],mul( mul(dp[i-1][j] , C[m-j][k]) , po[j]));
                }
        printf("%d\n",dp[n][m]);
    }
    return 0;
}
*/

/*
#include <iostream>
using namespace std;

int gcd(int a,int b)
{
    if(a<b)swap(a,b);
    if(b==0)return a;
    return gcd(b,a%b);
}

int main()
{
    int t;
    cin>>t;
    while(t--){
        int a,b;
        cin>>a>>b;
        cout<<gcd(a,b)<<endl;
    }
    return 0;
}*/

/*
#pragma comment(linker,"/STACK:102400000,102400000")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

const int MAXN = 50005;
vector<int> b[MAXN<<1];
vector<int> a[MAXN];
int head[MAXN];
int edge[MAXN<<1];
int next[MAXN<<1];
int esz;
int ans[MAXN];
int n,m;
int head1[MAXN];
int edge1[500005];
int next1[500005];
int esz1;
int Fa[MAXN];
int vis[MAXN];

void init()
{
    for(int i=1;i<=n;i++){
        vis[i]=0;
        Fa[i]=i;
        head1[i]=head[i]=-1;
        ans[i]=0;
    }
    esz=esz1=0;
}

void addedge(int u,int v)
{
    edge[esz]=v;
    next[esz]=head[u];
    head[u]=esz++;
}

void dfs(int u,int p)
{
    int L=a[u].size();
    for(int i=0;i<L;i++)
        b[a[u][i]].push_back(u);
    for(int i=head[u];i+1;i=next[i]){
        int v=edge[i];
        if(v==p)continue;
        dfs(v,u);
    }
}

void dfs2(int u,int p)
{
    for(int i=head[u];i+1;i=next[i]){
        int v=edge[i];
        if(v==p)continue;
        dfs2(v,u);
    }
    ans[p]+=ans[u];
}

void addedge1(int u,int v)
{
    edge1[esz1]=v;
    next1[esz1]=head1[u];
    head1[u]=esz1++;
}

int mfind(int x)
{
    if(x==Fa[x])return x;
    return Fa[x]=mfind(Fa[x]);
}

void Tarjan(int u,int p)
{
    vis[u]=1;
    for(int i=head[u];i+1;i=next[i]){
        int v=edge[i];
        if(v==p)continue;
        Tarjan(v,u);
        Fa[v]=u;
    }
    for(int i=head1[u];i+1;i=next1[i]){
        int v=edge1[i];
        ans[mfind(v)]--;
    }
}

inline int get(){
    int ret=0;
    char c=getchar();
    while(!isdigit(c)) c=getchar();
    while(isdigit(c)){
        ret=ret*10+(int)(c-'0');
        c=getchar();
    }
    return ret;
}

int main()
{
    while(scanf("%d%d",&n,&m)!=EOF){
        init();
        for(int i=1;i<n;i++){
            int u,v;
            u=get(),v=get();
            addedge(u,v);
            addedge(v,u);
        }
        int mx=0;
        for(int i=0;i<m;i++){
            int u,v;
            u=get(),v=get();
            mx=max(mx,v);
            a[u].push_back(v);
        }
        dfs(1,0);
        for(int i=1;i<=mx;i++){
            int L=b[i].size();
            if(L==0||L==1){
                if(L==1){
                ans[b[i][0]]++;
                b[i].clear();
                }
                continue;
            }
            int pre=b[i][0];
            ans[pre]++;
            for(int j=1;j<L;j++){
                int v=b[i][j];
                ans[v]++;
                addedge1(v,pre);
                pre=v;
            }
            b[i].clear();
        }
        Tarjan(1,0);
        dfs2(1,0);
        for(int i=1;i<=n;i++)if(a[i].size()>0)a[i].clear();
        for(int i=1;i<n;i++)
            printf("%d ",ans[i]);
        printf("%d\n",ans[n]);
    }
    return 0;
}
*/
/*
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char s[12][22];

int main()
{
    int t,n,i,j;
    cin>>t;
    while(t--){
        cin>>n;
        for(i=0;i<n;i++)cin>>s[i];
        for(i=0;i<n-1;i++)
            for(j=0;j<n-i-1;j++)
                if(strcmp(s[j],s[j+1])<0)
                    swap(s[j],s[j+1]);
        for(i=0;i<n-1;i++)
            cout<<s[i]<<' ';
        cout<<s[n-1]<<endl;
    }
    return 0;
}*/
/*
#include <iostream>
using namespace std;

int a[12][12];

int main()
{
    int t,n,i,j;
    cin>>t;
    while(t--){
        cin>>n;
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                cin>>a[i][j];
        for(j=0;j<n;j++){
            int mx=0,sum=0;
            for(i=0;i<n;i++){
                mx=max(mx,a[i][j]);
                sum+=a[i][j];
            }
            cout<<mx<<' '<<sum<<endl;
        }
    }
    return 0;
}*/
/*
#include <iostream>
using namespace std;

char s[100];

int fx(char s[])
{
    int i,d,to=0;
    for(i=0;s[i]!='\0';i++){
        if(s[i]>='A' && s[i]<='F')
            d=s[i]-'A'+10;
        else d=s[i]-'0';
        to=to*16+d;
    }
    return to;
}

int main()
{
    int t;
    cin>>t;
    while(t--){
        cin>>s;
        cout<<fx(s)<<endl;
    }
    return 0;
}*/
/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
using namespace std;

typedef long long ll;
const int MAXN = 100005;
int a[MAXN];

int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        int sz=0;
        while(n){
            a[sz++]=n%26;
            if(a[sz-1]==0)a[sz-1]=26;
            n/=26;
            if(a[sz-1]==26)n--;
            if(n==0 && a[sz-1]==26)break;
        }
     //   printf("%d\n",sz);
        for(int j=sz-1;j>=0;j--)
        printf("%c",a[j]-1+'A');
        printf("\n");
    }
    return 0;
}*/

/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
using namespace std;

class A{

public:
    ~A(){
    printf("A");
    };
};

class C{
public:
    ~C(){
    printf("C");
    };
};

class B:public A{
    public:
    ~B(){
        printf("B");
    };
    private:
        C hehe;
};

int main()
{
    B hehe;
    return 0;
}*/

/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
using namespace std;

#define LL(x)	 ((x)<<1)
#define RR(x)	 ((x)<<1|1)
#define FF(i,n)	 for(int i = 0 ; i < n ; i ++)

struct Seg_Tree{
	int left,right;
	int cnt;
	double sum;
	int mid() {
		return (left + right) >> 1;
	}
}tt[6666];
struct Seg{
	double high;
	double left,right;
	int side;
}ss[2222];
bool cmp(Seg a, Seg b) {
	return a.high < b.high;
}
double pos[2222];

void build(int l,int r,int idx) {
	tt[idx].left = l;
	tt[idx].right = r;
	tt[idx].cnt = 0;
	tt[idx].sum = 0;
	if(l == r)	return ;
	int mid = tt[idx].mid();
	build(l,mid,LL(idx));
	build(mid+1,r,RR(idx));
}

void update(int idx) {
	if(tt[idx].cnt) {
		tt[idx].sum = pos[tt[idx].right+1] - pos[tt[idx].left];
	} else if(tt[idx].left == tt[idx].right) {
		tt[idx].sum = 0;
	} else {
		tt[idx].sum = tt[LL(idx)].sum + tt[RR(idx)].sum;
	}
}

void update(int l,int r,int st,int idx) {
	if(l <= tt[idx].left && r >= tt[idx].right) {
		tt[idx].cnt += st;
		update(idx);
		return ;
	}
	int mid = tt[idx].mid();
	if(l <= mid) update(l,r,st,LL(idx));
	if(mid < r)	update(l,r,st,RR(idx));
	update(idx);
}

int Bin(double x,int hi) {
	int lo = 0;
	while(lo <= hi) {
		int mid = (lo + hi) >> 1;
		if(pos[mid] == x)	return mid;
		if(pos[mid] < x) {
			lo = mid + 1;
		} else {
			hi = mid - 1;
		}
	}
	return -1;
}

int main() {
	int n;
	int cas = 1;
	while(scanf("%d",&n) == 1) {
		if(n == 0)	break;
		int m = 0;
		FF(i,n) {
			double a,b,c,d;
			scanf("%lf%lf%lf%lf",&a,&b,&c,&d);
			pos[m] = ss[m].left = ss[m+1].left = a;
			ss[m].high = b;
			pos[m+1] = ss[m].right = ss[m+1].right = c;
			ss[m+1].high = d;
			ss[m].side = 1;
			ss[m+1].side = -1;
			m += 2;
		}
		sort(ss,ss+m,cmp);
		sort(pos,pos+m);
		int k = 0;
		FF(i,m) {
			if(i == 0 || pos[i] != pos[i-1]) {
				pos[k++] = pos[i];
			}
		}
		build(0,k-1,1);
		double ret = 0;
		FF(i,m-1) {
			int l = Bin(ss[i].left,k-1);
			int r = Bin(ss[i].right,k-1) - 1;
			if(l > r) {
				ret += tt[1].sum * (ss[i+1].high - ss[i].high);
				continue;
			}
			update(l,r,ss[i].side,1);
			ret += tt[1].sum * (ss[i+1].high - ss[i].high);
		}
		printf("Test case #%d\n",cas++);
		printf("Total explored area: %.2lf\n\n",ret);
	}
	return 0;
}*/


#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
using namespace std;

int a[1005];

int main()
{
    int t,tt=0;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        int ans=0;
        for(int i=1;i<=n;i++){
            scanf("%d",&a[i]);
            ans=max(ans,a[i]);
        }
        int mx=ans;
        for(int i=1;i<mx;i++){
            int res=0;
            for(int j=1;j<=n;j++)if(a[j]>i){
                int v=a[j]-i;
                int flag=0;
                if(v%i>0)flag=1;
                res+=v/i+flag;
            }
            ans=min(ans,i+res);
        }
        printf("Case #%d: %d\n",++tt,ans);
    }
    return 0;
}
/*

class A{

public:
    ~A(){
    printf("A");
    };

    int val;
};

class C{
public:
    C(int a){
    printf("%d",a);
    };
};

class D{
public:
    D(int a){
    printf("%d",a);
    };
};

class E{
public:
    E(int a){
    printf("%d",a);
    };
};

class F{
public:
    F(int a){
    printf("%d",a);
    };
};

class G{
public:
    ~G(){
        printf("G");
    };
};

class B:public A{
    public:
    B(int a,int b,int c,int d):hehe1(a),hehe2(b),hehe3(c),hehe4(d){
        printf("asdasd");
        val=a;
        printf("%d\n",val);
    }
    private:
        C hehe1;
        D hehe2;
        E hehe3;
        F hehe4;
        G hehe5;
};

int main()
{
    B hehe(1,2,3,4);
    return 0;
}
*/
