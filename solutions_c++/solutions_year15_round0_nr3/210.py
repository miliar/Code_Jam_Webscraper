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
#include<map>
#include<queue>
using namespace std;
#define mdlo 1000000007
typedef vector<long>pancakes;
long N;
long multiPlicationTable[4][4];
long signTable[4][4];

long long pwr[20];
long long gcd(long long a,long long b){
    long long c;
    if(a>b){
        c=a;
        a=b;
        b=c;
    }
    c=b%a;
    while(c>0){
        b=a;
        a=c;
        c=b%a;
    }
    return a;
}
bool isPositive(char a,char b){
    if(a=='1'||b=='1')
        return true;
    if(a==b)
        return false;
    if(a=='i'){
        if(b=='j')
            return true;
        return false;
    }
    if(a=='j'){
        if(b=='k')
            return true;
        return false;
    }
    if(b=='i')
        return true;
    return false;
}
char getResult(char a,char b){
    if(a=='1')
        return b;
    if(b=='1')
        return a;
    if(a==b)
        return '1';
    if(a=='i'){
        if(b=='j')
            return 'k';
        return 'j';
    }
    if(a=='j'){
        if(b=='k')
            return 'i';
        return 'k';
    }
    if(b=='i')
        return 'j';
    return 'i';
}
int main(void){
    multiPlicationTable[0]={0,1,2,3};
    multiPlicationTable[1]={1,0,3,2};
    multiPlicationTable[2]={2,3,0,1};
    multiPlicationTable[3]={3,2,1,0};
    signTable[0]={0,0,0,0};
    signTable[1]={0,1,0,1};
    signTable[2]={0,1,1,0};
    signTable[3]={0,0,1,1};

	freopen ("E:/inputSmall.txt","r",stdin);
	  freopen ("E:/outputSmall3.txt","w",stdout);
	long test_cases;
	cin>>test_cases;
	string s;
	long long L,X;
	char seqq[1000010];

	for(long T=0;T<test_cases;T++){
	//	double C,F,X,currentCookies=0,currentRate=2.0,time,curtime=0;
		cin>>L>>X;
		if(X>1024)
            X=(X%1024)+1024;
		cin>>seqq;
		long currentValue=0,currentSign=0,currentPos=0;
		char cuurentChar='1';
		bool positive=true;
		long long Total=L*X;
		bool posible=false;
		for(long long i=0;i<Total;i++){
            if(positive==isPositive(cuurentChar,seqq[i%L]))
                positive=true;
            else
                positive=false;
            cuurentChar=getResult(cuurentChar,seqq[i%L]);

            if(currentPos==0){
                if(positive&&cuurentChar=='i')
                    currentPos++;
            }
            else if(currentPos==1){
                if(positive&&cuurentChar=='k')
                    currentPos++;
            }
            else if(i+1==Total&&!positive&&cuurentChar=='1'){
                posible=true;
                break;
            }
		}
		if(posible)
            printf("Case #%ld: YES\n",T+1);
		else
            printf("Case #%ld: NO\n",T+1);
	}
	return 0;
}

/*
long long getSumation(long i,long j){
	if(sums[i][j]==0){
		if(i+1==N)
			sums[i][j]=numbers[i][j];
		else if(getSumation(i+1,j)>getSumation(i+1,j+1))
			sums[i][j]=numbers[i][j]+sums[i+1][j];
		else
			sums[i][j]=numbers[i][j]+sums[i+1][j+1];
	}
	return sums[i][j];
}
long long minVal(string s){
    long long val=0;
    if(s[0]=='?')
        val=1;
    else
        val=s[0]-'0';
    for(long long i=1;i<s.size();i++)
    {
        if(s[i]=='?')
            s[i]='0';
        val=(val*10)+(s[i]-'0');
    }
    return val;
}
long long addVal(string s,long long val){
    if(val<1)
        return 0;
    long d=log10((double)val);
    int l=s.size()-1;
    if(s[l-d]!='?'){
        for(long long j=1+l-d;j>-1;j--)
        {
            if(s[j]=='?'){
                return pwr[l-j];
            }
        }
        return -1;
    }
    else{//s[l-d]=='?'
        long long p=pwr[d];
        long long firstDigit=val/p;
        long long sub=firstDigit*p;
        long long rest=addVal(s,val-sub);
        if(firstDigit!=9||rest!=p)
            return sub+rest;
        for(long long j=1+l-d;j>-1;j--)
        {
            if(s[j]=='?'){
                return pwr[l-j];
            }
        }
        return -1;
    }
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
long chainLength[5000056];

long getChainLength(long long i){
	long l=0;
	while(i>5000000){
		if(i%2)
			i=3*i+1;
		else
			i/=2;
		l++;
	}
	if(chainLength[i]==0){
		if(i%2)
			chainLength[i]=2+getChainLength((1+3*i)/2);
		else
			chainLength[i]=1+getChainLength(i/2);
	}
	return chainLength[i]+l;
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
long maxlength[5000056];
void drawRevtangles(){
    long s=rectangles.size();
    sort(rectangles.begin(),rectangles.end());
    long long maxX,maxY,minX,minY;
    for(long long i=0;i<s;i++){
        point bottomRight,topleft;
        topleft=rectangles[i].leftTop;
        bottomRight=rectangles[i].rightBottom;
        long long j=i;
        while(j<s&&bottomRight.inside(rectangles[j].leftTop)){
            bottomRight.x=max(bottomRight.x,rectangles[j].rightBottom.x);
            bottomRight.y=max(bottomRight.y,rectangles[j].rightBottom.y);
            j++;
        }
        i=j-1;
        for(long long x=topleft.x;x<=bottomRight.x;x++)
            for(long long y=topleft.y;y<bottomRight)
    }
}*/
/*
typedef vector<char>word;
typedef pair<long,long>weightedPos;

long dp[200010];
vector<weightedPos>points;
vector<weightedPos>modifiedPositions;
vector<long long>weightPlusPos;
long long segTree[530010];
long N,X,W;
void buildSegTree(long node,long b,long e){
    if(b==e)
        segTree[node]=b;
    else{
        long mid=(b+e)/2;
        buildSegTree(node*2,b,mid);
        buildSegTree(1+node*2,mid+1,e);
        if(weightPlusPos[segTree[node*2]]<=weightPlusPos[segTree[1+node*2]])
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
    if(weightPlusPos[sh]<weightPlusPos[fh])
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
