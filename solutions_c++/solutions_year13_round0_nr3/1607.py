/// @file
/// @brief	문제: 
///	해결법 : 
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include<stack>
#include<map>
#include<queue>
#include<algorithm>
#include<cassert>
#include<cctype>
using namespace std;

#define rep(i,n)	for(int (i)=0;(i)<(n);(i)++)
#define repd(i,n)	for(int (i)=(n)-1;(i)>=0;(i)--)
#define REP(i,n) for (int (i)=0,_n=(n); (i) < _n; (i)++)
#define FOR(i,a,b) for (int _b=(b), (i)=(a); (i) <= _b; (i)++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset((x),0,sizeof(x));
#define CLEARA(x) memset(&(x),0,sizeof(x));
#define FILL(x,v) memset((x),(v),sizeof(x));
#define FILLA(x,v) memset(&(x),(v),sizeof(x));

//c++ 0x
#define FOREACH(it,c) for(auto it=(c).begin();it!=(c).end();++it)
#define rFOREACH(it,c) for(auto it=(c).rbegin();it!=(c).rend();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
//const double pi = acos(-1.0);
#define EPS 1e-9

#define PII pair<int,int> 
#define VI vector<int>
#define LL long long
#define ULL unsigned long long
template<typename T> inline T		gcd(T a, T b){if(a>b)swap(a,b);while(a!=0){b%=a;swap(a,b);}return b;}
template<typename T> inline T		lcm(T a, T b){return a/gcd(a,b)*b;}
//int pow(int a,int b){int c=1;while(b--)c*=a;return c;}


//#define PROB   "d:\\C-small-attempt0"
#define PROB   "d:\\C-large-1"

#define MAX_NUM_ITEM 1000000000

struct BigNum
{
	int count;
	ULL num[12];

	void GetFromString(const char* str)
	{
		char temp[1024];
		strcpy(temp,str);
		int len=strlen(temp);
		this->count=0;
		char *ptr;
		while(len>0)
		{
			if((len-=9)<0)len=0;
			ptr=temp+len;
			sscanf(ptr,"%llu",&num[this->count++]);
			*ptr=NULL;
		}
		while(this->count>1 && num[this->count-1]==0)
			this->count--;
	}
	bool operator <(const BigNum &s1) const{
		if(this->count < s1.count)return true;
		else if(this->count > s1.count)return false;
		else{
			FORD(i,this->count-1,0){
				if(this->num[i]<s1.num[i])return true;
				else if(this->num[i]>s1.num[i])return false;
			}
		}
		return false;
	}
	void ToSquare()
	{
		ULL temp=0;
		ULL prevNum[12];
		memcpy(prevNum,this->num,count*sizeof(ULL));
		FOR(n,0,2*(count-1)){
			FOR(i,max(n-count+1,0),min(n,count-1))
				temp+=prevNum[i]*prevNum[n-i];
			this->num[n]=temp%MAX_NUM_ITEM;
			temp/=MAX_NUM_ITEM;
		}
		count=2*(count-1)+1;
		if(temp>0)num[count++]=temp;
	}
	bool IsPan()
	{
		char strNum[128];
		sprintf(strNum,"%llu",num[count-1]);
		int len=strlen(strNum);
		repd(j,count-1){
			sprintf(strNum+len,"%09llu",num[j]);
			len+=strlen(strNum+len);
		}
		for(int i=0,j=len-1;i<j;)
			if(strNum[i++]!=strNum[j--])return false;
		fprintf(stderr,"%s, ",strNum);
		return true;
	}
};

int main(){
	freopen(PROB ".in","r",stdin);
	freopen(PROB ".out","w",stdout);

	char strA[1024],strB[1024];
	BigNum A,B;
	vector<BigNum> arr;
	//pre calc
	{
		int abJari,pos;
		FOR(n,1,10)
		{
			fprintf(stderr,"\npreCalc %d : ",n);
			memset(strA,'0',n*sizeof(char));
			strA[0]=strA[n-1]='1';
			strA[n]=NULL;
			pos=abJari=(n-1)/2;
			while(1)
			{
				A.GetFromString(strA);
				A.ToSquare();
				if(A.IsPan())
					arr.push_back(A);
				
				pos=abJari;
				while(pos>=0)
				{
					strA[n-(pos+1)]=++strA[pos];
					if(strA[pos]<='9')break;
					strA[n-(pos+1)]=strA[pos]='0';
					pos--;
				}
				if(pos<0)break;
			}
		}
	}
	fprintf(stderr,"ArraySize %d\n",arr.size());
	int T;scanf("%d",&T);
	FOR(t,1,T){
		scanf("%s %s",strA,strB);
		A.GetFromString(strA);
		B.GetFromString(strB);
		int i=lower_bound(ALL(arr),A)-arr.begin();
		int j=upper_bound(ALL(arr),B)-arr.begin();
Print:
		fprintf(stderr,"Case #%d: %d\n",t,j-i);
		printf("Case #%d: %d\n",t,j-i);
	}
	fclose(stdout);
	
	return 0;
}