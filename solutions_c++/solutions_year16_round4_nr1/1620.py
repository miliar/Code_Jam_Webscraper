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
typedef vector<long>elements;
typedef pair<long,long>edge;
vector<edge>criticalEdges;
adjList Graph[29];
ll heights[5];
ll segTree[3];
long nums[5005];
long g[5005];

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
long dp[10][5];
ll betPlaced[40];
ll cumBet[40];
ll B;
long wordLen;
string s1,s2,s3;
long perMutation[20];
elements moveTo(elements e, long frompos,long topos){
    long dm;
    if(frompos>topos)
        dm=-1;
    else
        dm=1;
    long val=e[frompos];
    for(long i=frompos;i!=topos;i+=dm){
        e[i]=e[i+dm];
    }
    e[topos]=e[frompos];
    return e;
}
double getMaxBenifit(long nextPos){
  ll budgetRequired;
  budgetRequired=nextPos*(betPlaced[nextPos-1])-cumBet[nextPos-1];
  if(nextPos==0||budgetRequired>B||betPlaced[nextPos]==betPlaced[nextPos-1])
    return 0;
  ll budget=0;

  ll betVal=min(betPlaced[nextPos]-(ll)1,betPlaced[nextPos-1]+(B-budgetRequired)/nextPos);
  double expectedProfit=0,divis=nextPos;
  for(long i=0;i<nextPos;i++){
    double moneyPushed=(betVal-betPlaced[i])*36;
    budget+=(betVal-betPlaced[i]);
    expectedProfit+=moneyPushed;
  }
  expectedProfit=expectedProfit/divis;
  expectedProfit=expectedProfit-budget;
    return expectedProfit;
}
int main(void){
    freopen ("E:/inputSmall.txt","r",stdin);
    freopen ("E:/outputSmall2.txt","w",stdout);
    ll test_cases=1,l,seed=1,m,R,P,S;
  //memset(dp,0,sizeof(dp));
  cin>>test_cases;
  ll totalPlayer;
  cout << setprecision(15) << fixed;
    for(long T=0;T<test_cases;T++){
        cin>>N>>R>>P>>S;
        cout<<"Case #"<<T+1<<": ";
        totalPlayer=R+P+S;
        if(R+R>totalPlayer||P+P>totalPlayer||S+S>totalPlayer){
            cout<<"IMPOSSIBLE\n";
        }
        else{
            if(N==1){
                             if(P)
                    cout<<"P";

                if(R)
                    cout<<"R";
                if(S)
                    cout<<"S";
                cout<<endl;
            }
            else if(N==2){
                if(R==0||S==0||P==0)
                    cout<<"IMPOSSIBLE\n";
                else{
                    if(R==2)
                        cout<<"PRRS";
                    else if(S==2)
                        cout<<"PSRS";
                    else
                        cout<<"PRPS";
                    cout<<endl;
                }
            }
            else{
                char seqans[9];
                if(R<2||P<2||S<2||R==4||S==4||P==4)
                    cout<<"IMPOSSIBLE\n";
                else{
                    if(R==2){
                        cout<<"PRPSPSRS\n";
                    }
                    else if(S==2)
                        cout<<"PRPSPRRS\n";
                    else
                        cout<<"PRRSPSRS\n";//PRSR
                }
            }
        }
     //   cout<<maxProfit<<endl;
    }
    return 0;
}
