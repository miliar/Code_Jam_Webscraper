#include<stdio.h>
#include<iostream>
#include<string>
#include<cstring>
#include <iomanip>
#include<stack>
#include<set>
#include<vector>
#include<algorithm>
#include<set>
#include<bitset>
#include<map>
#include<queue>
#include<math.h>
#include <time.h>
using namespace std;
//set<int>::iterator it;
#define mdlo 1000000007
#define maxERR 0.000000002
//#define minVal -10000000000000
#define maxBits 40
#define pi 3.1415926535897932384626433832795
#define INF 999999999999
#define lim 10000007
typedef long long ll;
long long mInv[41];
long long fact[41];
long long factInv[41];
map<string,long>cityId;
typedef vector<long>adjList;
typedef pair<long,long>edge;
vector<edge>criticalEdges;
adjList Graph[29];
ll heights[5];
ll segTree[3];
long nums[5005];
long g[5005];

ll S[1000006];
ll M[1000006];

ll as,cs,rs;
ll am,cm,rm;
ll N,D;
//ll dp[2][5002][5002];
vector<long>primes;
vector<long>badPrimes;
long funcVal[1];
long dfs_num[29],dfs_low[29],visited[29],parent[19],criticalNode[19];
set<string>dictionary;
set<string>::iterator it;
pair<set<string>::iterator,bool> ret;
typedef multiset<long> numset;
ll gcd(ll a,ll b){
    if(b==0)
        return a;
    if(a%b==0)
        return b;
    return gcd(b,a%b);
}
long long getmoduloInv(long long n){
    if(n==1)
        return 1;
    if(mInv[n]>0)
        return mInv[n];
    long long m=(-1*mdlo)/n;
    m+=mdlo;
    m*=getmoduloInv(mdlo%n);
    mInv[n]=(m%mdlo);
    return mInv[n];
}
vector< long> get_primes(unsigned long maxN){

    char *sieve;
    sieve = new char[maxN/8+1];
    // Fill sieve with 1
    long m=(maxN/8)+1;
    for(long long i=0;i<m;i++)
        sieve[i]=255;
    for(unsigned long x = 2; x <= maxN; x++)
        if(sieve[x/8] & (0x01 << (x % 8))){
            primes.push_back(x);
            // Is prime. Mark multiplicates.
            for(unsigned long j = 2*x; j <= maxN; j += x)
                sieve[j/8] &= ~(0x01 << (j % 8));
        }
    delete[] sieve;
    return primes;
}
ll getPow(ll b,ll p){
	if(b<2||p==1)
		return b;
	if(p==0)
		return 1;
	ll val=getPow(b,p/2);
	val*=val;
	val%=mdlo;
	if(p%2==1){
		val*=b;
		val%=mdlo;
	}
	return val;
}
void buildSegTree(long node,long b,long e){
    if(b==e)
        segTree[node]=b;
    else{
        long mid=(b+e)/2;
        buildSegTree(node*2,b,mid);
        buildSegTree(1+node*2,mid+1,e);
        if(heights[segTree[node*2]]<=heights[segTree[1+node*2]])
            segTree[node]=segTree[node*2];
        else
            segTree[node]=segTree[1+node*2];
    }
}
long long getMin(long node,long segBeg,long segEnd,long qBeg,long qEnd){
    if(segEnd<qBeg||segBeg>qEnd)
        return N+1;
    if(segBeg>=qBeg&&segEnd<=qEnd)
        return segTree[node];
    long mid=(segBeg+segEnd)/2;
    long fh=getMin(node*2,segBeg,mid,qBeg,qEnd);
    long sh=getMin(1+node*2,mid+1,segEnd,qBeg,qEnd);
    if(heights[sh]<heights[fh])
        return sh;
    return fh;
}
long bff[1100];
long inq[1010];
long source;
long oneEndBig=0,oneEndSmall=0,twoendans,zeroendans;
typedef pair<long,long>ee;
typedef pair<long,ee>openAns;
vector<openAns>allopenANs;
long bigEntry,bigExit,smallEntry,smallExit;
long dfs(long node,long curLen){
    if(inq[node]==0){
        inq[node]=1;
        dfs(bff[node],curLen+1);
    }
    else if(node==source)
    {
        if(zeroendans<curLen)
            zeroendans=curLen;
    }
    else if(bff[bff[node]]==node){
        curLen-=2;
        openAns oA;
        oA.first=curLen;
        oA.second.first=bff[node];
        oA.second.first=node;
        allopenANs.push_back(oA);
    }
  //  queue<long>
  return 0;
}
long dp[10010][5];
long wordLen;
string s1,s2,s3;
long perMutation[20];
string cvert(long val,long len){
    string s="";
    for(long i=0;i<len;i++)
        s=s+"?";
    for(long i=len-1;i>-1;i--)
    {
        s[i]='0'+val%10;
        val/=10;
    }
    return s;
}
bool matches(long val,string s){
    string s1=cvert(val,s.size());
    for(long i=0;i<s.size();i++){
        if(s[i]!='?'&&s[i]!=s1[i])
            return false;
    }
    return true;
}
ll wordCombVal1,wordCombVal2;
ll fwpos[1010],swpos[1010];
    long num;
ll getCombVal(ll comb){
    long pos=0,cnt=0;
    ll val1=0,val2=0;
    while(comb>0){
        if(comb%2==1){
            val1=val1|(1<<fwpos[pos]);
            val2=(1<<swpos[pos])|val2;
            cnt++;
        }
        comb/=2;
        pos++;
    }
    if(val1==wordCombVal1&&val2==wordCombVal2)
        return num-cnt;
    return 0;
}

map<string,long>wordId1;
map<string,long>wordId2;
int main(void){
    freopen ("E:/inputSmall.txt","r",stdin);
    freopen ("E:/outputSmall.txt","w",stdout);
    ll test_cases=1,l,seed=1,maxVal;
	//memset(dp,0,sizeof(dp));
	cin>>test_cases;
	ll lCount[28];
	ll digitCount[11];
    cout << setprecision(15) << fixed;
    memset(dp,-1,sizeof(dp));
    for(long T=0;T<test_cases;T++){

        cin>>num;
        wordId1.clear();
        wordId2.clear();
        ll ans=0;
        long wordCount1=0,wordCount2=0;
        for(long i=0;i<num;i++){
            cin>>s1>>s2;
            if(wordId1[s1]==0){
                wordCount1++;
                wordId1[s1]=wordCount1;

            }
            if(wordId2[s2]==0){
                wordCount2++;
                wordId2[s2]=wordCount2;
            }
            fwpos[i]=wordId1[s1];
            swpos[i]=wordId2[s2];
        }
        wordCombVal1=1<<wordCount1;
        wordCombVal1--;
        wordCombVal1=2*wordCombVal1;
        wordCombVal2=1<<wordCount2;
        wordCombVal2--;
        wordCombVal2=2*wordCombVal2;
        ll limitt=1<<num;
        for(long i=1;i<limitt;i++){
            ll cv=getCombVal(i);
            if(cv>ans)
                ans=cv;
        }
        memset(lCount,0,sizeof(lCount));
        memset(digitCount,0,sizeof(digitCount));

        cout<<"Case #"<<T+1<<": ";
        cout<<ans<<endl;
        //cout<<ans<<endl;


        //cout<<max(ans2,zeroendans);
        //cout<<endl;
    }
    return 0;
}
/*ll cumDist1[100005];
ll cumDist2[100005];
vector<ll>distFrom1;
vector<ll>distFrom2;
void initFact(){
    fact[0]=1;
    factInv[0]=1;
    for(ll i=1;i<0;i++){
        factInv[i]=(factInv[i-1]*getmoduloInv(i))%mdlo;
        fact[i]=(fact[i-1]*i)%mdlo;
    }
}
bool isLeapyear(long year){
    if(year%4==0&&(year%100!=0||year%400==0))
        return true;
    return false;
}
ll ds,ms,ys,de,me,ye,dc,mc,yc,day;
void next13th(){
    if(ds<13){
        ds=13;
        return;
    }
    ms++;
    ds=13;
    if(ms>12)
    {
        ms=1;
        ys++;
    }
}
    long months[]={31,28,31,30,31,30,31,31,30,31,30,31};
    long dayBeforeMonth[12];
bool validDate(){
    if(ys>ye)
        return false;
    if(ys<ye)
        return true;
    if(ms>me)
        return false;
    if(ms<me)
        return true;
    if(ds>de)
        return false;
    return true;
}
long getDay(long d,long m,long y){
    long day=((y-1900)*365+(y-1900)/4-(y-1900)/100+(y-1600)/400+dayBeforeMonth[m-1]+d+2)%7;
    if(y%4==0&&m<3){
        if(y%400==0||y%100!=0)
            day=(day+6)%7;
    }
    return day;
}
bool iscurDayFriday(){
    if(getDay(ds,ms,ys)==0)
        return true;
    return false;
}
void dijkstra(long startPoint){
    long m;
    if(startPoint==1)
        m=0;
    else
        m=1;
    distMatrix[m][startPoint]=0;
    priority_queue<edge, vector<edge>,greater <edge>>pq;
    pq.push(edge(0,startPoint));
    while(!pq.empty()){
        edge top=pq.top();
        pq.pop();
        ll d= top.first,u=top.second;
        if(distMatrix[m][u]==d){
            for(long i=0;i<graph[u].size();i++){
                ll v=graph[u][i].second;
                ll ec=graph[u][i].first;
                if(distMatrix[m][v]>distMatrix[m][u]+ec){
                    distMatrix[m][v]=distMatrix[m][u]+ec;
                    pq.push(edge(distMatrix[m][v],v));
                }
            }
        }
    }
}
ll vals[1];
ll dp[1];
ll totalSum[1];
long long mInv[1];
long long fact[1];
long long factInv[1];

//long long pow10[18];
long long getmoduloInv(long long n){
    if(n==1)
        return 1;
    if(mInv[n]>0)
        return mInv[n];
    long long m=(-1*mdlo)/n;
    m+=mdlo;
    m*=getmoduloInv(mdlo%n);
    mInv[n]=(m%mdlo);
    return mInv[n];
}
long long onNthbit(long pos,long val){
    return val|pwr2[pos];
}
bool isNthbitOn(long long pos,long long val){
    return (val&pwr2[pos])>0;
}

seg segTree[5];
long N;
void buildSumSegmentTree(long long b,long long e,long long node){
    if(b==e)
    {
         segTree[node].first=vals[b];
         return;
    }
    long long mid=(b+e)/2;
    buildSumSegmentTree(b,mid,node*2);
    buildSumSegmentTree(mid+1,e,1+(node*2));
    segTree[node].first=segTree[2*node].first+segTree[1+(node*2)].first;
}
long long getSum(long long qStart,long long qEnd,long long sStart,long long sEnd,long long node,prop p){

    long k=sEnd-sStart,n;
    for(long i=0;i<p.size();i++){
        segTree[node].second.push_back(p[i]);
        n=p[i];
        segTree[node].first+=(((n+k)*(n+k+1)*(2*n+2*k+1)-(n*(n-1)*(2*n-1)))/6+((n+k)*(n+k+1)-n*(n-1)))/2;
        }
    if(qEnd<sStart||qStart>sEnd)
    {
        return 0;
    }
    if(sStart>=qStart&&sEnd<=qEnd)
    {
         return segTree[node].first;
    }
    long long sMid=(sStart+sEnd)/2;
    prop l;
    for(long i=0;segTree[node].second.size();i++)
        l.push_back(segTree[node].second[i]+sMid+1-sStart);
    return getSum(qStart,qEnd,sStart,sMid,2*node,segTree[node].second)+getSum(qStart,qEnd,sMid+1,sEnd,1+(2*node),l);
}
long long update(ll node, long long sStart,ll sEnd,long upStart,long upEnd){
    if(upEnd<sStart||upStart>sEnd)
        return 0;
    long k=sEnd-sStart,n=sStart+1-upStart;
    if(upStart<=sStart&&upEnd>=sEnd){
        segTree[node].second.push_back(n);
        segTree[node].first+=(((n+k)*(n+k+1)*(2*n+2*k+1))/6);
        segTree[node].first-=(((n*(n-1)*(2*n-1)))/6);
        segTree[node].first+=(((n+k)*(n+k+1)-n*(n-1)))/2;
        return 0;
    }
    ll sMid=(sStart+sEnd)/2;
    update(node*2,sStart,sMid,upStart,upEnd);
    update(1+(node*2),sMid+1,sEnd,upStart,upEnd);
    segTree[node].first=segTree[2*node].first+segTree[1+(node*2)].first;

    for(long i=0;i<segTree[node].second.size();i++){
        n=segTree[node].second[i];
        segTree[node].first+=(((n+k)*(n+k+1)*(2*n+2*k+1)-(n*(n-1)*(2*n-1)))/6+((n+k)*(n+k+1)-n*(n-1)))/2;
    }
    return segTree[node].first;
}
void update(long x,long y){
    long len=y-x+1,add=0;
    for(long i=0;i<len;i++){
        add+=(i+1)*2;
        update(1,0,N-1,x+i,add+vals[x+i]);
    }
}
long getlen(long long num){
    long len=0;
    while(num>0){
        num/=10;
        len++;
    }
    return len;
}
encryptedLine lineConverter(string s){
    encryptedLine el;
    ll val=0,len=s.size();
    for(long i=0;i<len;i++){
        if(s[i]==' '){
            el.push_back(val);
            val=0;
        }
        else{
            val*=26;
            val+=(s[i]-'a');
        }
    }
    el.push_back(val);
    return el;
}
long getPalinDrome(long num){
    long a=num%10;
    long b=(num/10)%10;
    long c=(num/100)%10;
    return num*1000+a*100+b*10+c;
}

vector<unsigned long> get_primes(unsigned long max){
    vector<unsigned long> primes;
    char *sieve;
    sieve = new char[max/8+1];
    // Fill sieve with 1
    long m=(max/8)+1;
    for(long long i=0;i<m;i++)
        sieve[i]=255;
    for(unsigned long x = 2; x <= max; x++)
        if(sieve[x/8] & (0x01 << (x % 8))){
            primes.push_back(x);
            // Is prime. Mark multiplicates.
            for(unsigned long j = 2*x; j <= max; j += x)
                sieve[j/8] &= ~(0x01 << (j % 8));
        }
    delete[] sieve;
    return primes;
}string add(string a,string b){
    int l1=a.size();
    int l2=b.size();
    while(l1<l2){
        a="0"+a;
        l1++;
    }
    while(l2<l1){
        b="0"+b;
        l2++;
    }
    string s;
    int carry=0;
    for(long i=l2-1;i>-1;i--){
        int d=a[i]+b[i]+carry-2*'0';
        carry=d/10;
        a[i]='0'+(d%10);
    }
    if(carry)
        a="1"+a;
    return a;
}
long long mInv[1010];
long long fact[1000];
long long factInv[1000];
long long getmoduloInv(long long n){
    if(n==1)
        return 1;
    if(mInv[n]>0)
        return mInv[n];
    long long m=(-1*mdlo)/n;
    m+=mdlo;
    m*=getmoduloInv(mdlo%n);
    mInv[n]=(m%mdlo);
    return mInv[n];

}

long dp[200010];
vector<weightedPos>points;
vector<weightedPos>modifiedPositions;
vector<long long>heights;
long long segTree[530010];
long N,X,W;
void buildSegTree(long node,long b,long e){
    if(b==e)
        segTree[node]=b;
    else{
        long mid=(b+e)/2;
        buildSegTree(node*2,b,mid);
        buildSegTree(1+node*2,mid+1,e);
        if(heights[segTree[node*2]]<=heights[segTree[1+node*2]])
            segTree[node]=segTree[node*2];
        else
            segTree[node]=segTree[1+node*2];
    }
}
long long getMin(long node,long segBeg,long segEnd,long qBeg,long qEnd){
    if(segEnd<qBeg||segBeg>qEnd)
        return N;
    if(segBeg>=qBeg&&segEnd<=qEnd)
        return segTree[node];
    long mid=(segBeg+segEnd)/2;
    long fh=getMin(node*2,segBeg,mid,qBeg,qEnd);
    long sh=getMin(1+node*2,mid+1,segEnd,qBeg,qEnd);
    if(heights[sh]<heights[fh])
        return sh;
    return fh;
}
long long getMinPos(long node,long segBeg,long segEnd,long qBeg,long qEnd){
    if(segEnd<qBeg||segBeg<qEnd)
        return 0;
    if(segBeg>=qBeg&&segEnd<=qEnd)
        return segTree[node];
    long mid=(segBeg+segEnd)/2;
    long fh=getMin(node*2,segBeg,mid,qBeg,qEnd);
    long sh=getMin(node*2,mid+1,segEnd,qBeg,qEnd);
    return min(fh,sh);
}
long getPos(long val){
    long low=0,high=modifiedPositions.size()-1;
    long mid=(low+high)/2;
    while(low<high){
        if(modifiedPositions[mid].first<val)
            low=mid+1;
        else
            high=mid-1;
        mid=(low+high)/2;
    }
    if(mid>0)
        mid--;
    while(mid<modifiedPositions.size()&&modifiedPositions[mid].first<val)
        mid++;
    return mid;
}
long getMaxGroup(long index){
    if(dp[index]>-1)
        return dp[index];
    long pos=getPos(points[index].first+points[index].second);
    if(pos>=N)
        return 1;
    long nextPoint=getMin(1,0,N-1,pos,N-1);
    dp[index]=1+getMaxGroup(nextPoint);
    return dp[index];
}
*/
