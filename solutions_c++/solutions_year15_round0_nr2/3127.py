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
                if(a[i]%2!=0)   //ע��:������%2=-1
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

const int INF = ~0U>>1;  //���ֵ��ʵ��2^31-1,int�ܴ洢������ֵ
const int MAXN = 1005;  //����������,���Ե���
const int MAXM = 1005;  //�ߵ��������,���Ե���
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

void init()   //��ʼ��
{
    memset(head,-1,sizeof(head));  //�ߵĴ洢�����ڽӱ�ʵ�ֵ�,��֤��Ч
    esz=0;
    q.clear();
    res.clear();
    for(int i=1;i<=n;i++)   //��ʼ�����鼯
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
    scanf("%d",&t);  //��������
    while(t--){
        scanf("%d%d",&n,&m);  //nΪ����, mΪ����
        init();
        for(int i=0;i<m;i++){
            int u,v,val;
            scanf("%d%d%d",&u,&v,&val);   //����ÿ���ߵ������˵�u��v,�Լ��ߵ�Ȩֵval
            addedge(u,v,val);    //���߼���ͼ��
            addedge(v,u,val);     //����ͼ��˫��ͼ,����vҲ�ܵ�u,Ҫ���뷴���
        }
        int ans=0;
        for(int u=1;u<=n;u++){    //��ͼ�е�ÿ���㣬ѡһ�������������СȨֵ�ı߼���MST
            int Min=INF;    //��Ĭ�ϱߵ�ȨֵΪ�����
            int id=-1;     //Ĭ�ϱߵ�idΪ-1
            for(int j=head[u];j+1;j=next[j]){   //������u���������бߣ������jΪ�ߵ�id
                int v=edgeto[j];          //���ʱ�u,v
                int val=w[j];             //��ȡ�ߵ�Ȩֵval
                if(Min>val){    //�����ǰ�ı�Ȩ����֮ǰ��ҪС�������Ϊ��ǰ��С��
                    Min=val;      //����
                    id=j;         //ͬʱ�����С�ߵ�id
                }
            }
            if(id==-1)continue;     //���idΪ-1,�򲻴����κ���u�����ı�,�����Ҳ��������
            int fa_u=mfind(edgefrom[id]);   //���鼯,���Բ����,��ʵ�����жϱ�id�������˵��ڲ���MST��
            int fa_v=mfind(edgeto[id]);
            if(fa_u!=fa_v){   //����MST
                fa[fa_u]=fa_v;   //����id�������˵����MST
                ans+=Min;         //MST��Ȩֵ��Min
                res.push_back(id);   //�洢MST�ı�id,resΪ��С�������ıߵļ���
            }
        }
        for(int u=1;u<=n;u++){      //��������ͼ�����б�
            for(int j=head[u];j+1;j=next[j]){
                int v=edgeto[j];
                int fa_u=mfind(u);
                int fa_v=mfind(v);
                if(fa_u!=fa_v)    //�ҵ������������Ų�ͬ�����ı�
                    q.push_back(make_pair(w[j],j));  //q��һ�������������Ų�ͬ�����ıߵļ���
            }
        }
        sort(q.begin(),q.end());  //���ߴ�С��������
        int L=q.size();
        for(int i=0;i<L;i++){
            pair<int,int>temp=q[i];
            int id=temp.second;
            int u=edgefrom[id];
            int v=edgeto[id];
            int fa_u=mfind(u);
            int fa_v=mfind(v);
            if(fa_u!=fa_v){     //���δ�С����ѡȡq�еı߼���MST
                fa[fa_u]=fa_v;
                ans+=w[id];
                res.push_back(id);  //�洢MST�ı�id,resΪ��С�������ıߵļ���
            }
        }
        L=res.size();
        if(L!=n-1){     //���MST�еı�������n-1,��һ����������С������
            printf("��С������������!\n");
            continue;
        }
        printf("��С��������Ȩֵ��: %d\n",ans);
        printf("��С�������ı���:\n");
        for(int i=0;i<n-1;i++){
            printf("%d %d %d\n",edgefrom[res[i]],edgeto[res[i]],w[res[i]]);  //���MST��ÿ����
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
    getchar(); //���˵�t֮��Ļس�
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
