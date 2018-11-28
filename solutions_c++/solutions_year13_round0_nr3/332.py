#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <cstring>

using namespace std;

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)


typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;


typedef ull T;
#define LARGE1
#ifdef	LARGE1
const int		MAX_DIGITS=51;
#endif




vector<vi> target1List;
vector<vi> target2List;
map<int, int> dicIndex;

int isGreater(vi& a, vi& b)
{
	int asize=a.size();
	int bsize=b.size();
	if(asize>bsize)		return 1;
	if(asize<bsize)return -1;
	rep(i,asize){
		if(a[i]>b[i]) return 1;
		if(a[i]<b[i]) return -1;
	}
	return 0;
}
inline int getParindomeNum(vi viVal,bool isEqual)
{
	int length=viVal.size();
	if(length==1 &&viVal[0]==1&&isEqual==false)return 0;

	int dicSize=target2List.size();
	int i=dicIndex[length];
	
	for(;i<dicSize;i++){
		int graterFlag=isGreater(target2List[i],viVal);
		if(graterFlag==0){
			if(isEqual){
				return i+1;
			}else {
				return i;
			}
		}
		if(graterFlag>0 ){
			return i;
		}
	}

	return dicSize;
}
vi getVectorInt(string strval)
{
	const char* pchar=strval.c_str();
	int num=strval.size();
	vi val;
	rep(i,num){
		int n=int(pchar[i]- '0');
		val.push_back(n);
	}
	return val;
}
inline void alg(){

	string A,B;
	cin >>A;
	cin >>B;
	vi viA=getVectorInt(A);
	vi viB=getVectorInt(B);
	int sizeA=getParindomeNum(viA,false);
	int sizeB=getParindomeNum(viB,true);
	cout << sizeB-sizeA;

}


int num1_digit;
int num1_maxIdx;
int num2_digit;
int num2_maxIdx;
inline int calcNum2Digit(vi& cand1, int digit)
{
	int num2_digit=0;
	int maxIdx=std::min(num1_maxIdx,digit);
	int minIdx=digit-maxIdx;
	for(int i=minIdx;i<=maxIdx;++i){
		if(num2_digit>=10)return 10;
		num2_digit+=cand1[i]*cand1[digit-i];
	}
	return num2_digit;
}

void searchTarget(vi cand1,vi cand2,int currentDigit,int num1Val)
{
	vi::iterator itr1= cand1.begin()+(num1_digit-1)/2;
	vi::iterator itr2= cand2.begin()+(num2_maxIdx-2)/2;

	if(num1_digit%2==0){
		if(num1Val!=*itr1) return;	
	}

	cand1.insert(itr1,num1Val);
	itr2= cand2.insert(itr2,-1);
	cand2.insert(itr2,-1);
	int bgn=currentDigit/2 ;
	int end=num2_maxIdx/2 + 1;
	rep2(i,bgn,end){
		int num2val=calcNum2Digit(cand1,i);
		if(num2val >=10) return;
		cand2[i]				=num2val;
		cand2[num2_maxIdx-i]	=num2val;
	}
	target1List.push_back(cand1);
	target2List.push_back(cand2);
	return ;
	
}
void makeTargetNum(int d,int& bgnIdx){
	num1_digit	=d;
	num1_maxIdx	=num1_digit-1;
	num2_digit	=2*d-1;
	num2_maxIdx	=num2_digit-1;
	int endIdx=target1List.size();
		rep2(i,bgnIdx,endIdx){
		vi target1	= target1List[i];
		vi target2	= target2List[i];
		rep2(n,0,4){
			searchTarget(target1,target2,d,n);
		}
	}
	bgnIdx =endIdx;
}

void init(const int max_digit)
{
	{
		vi tmp1(1);
		vi tmp2(1);
		tmp1[0]=1;	tmp2[0]=1;
		target1List.push_back(tmp1);
		target2List.push_back(tmp2);
		tmp1[0]=2;	tmp2[0]=4;
		target1List.push_back(tmp1);
		target2List.push_back(tmp2);
		tmp1[0]=3;	tmp2[0]=9;
		target1List.push_back(tmp1);
		target2List.push_back(tmp2);
	}
	{
		vi tmp1(2);
		vi tmp2(3);
		tmp1[0]=1;tmp1[1]=1;	tmp2[0]=1;tmp2[1]=2;tmp2[2]=1;
		target1List.push_back(tmp1);
		target2List.push_back(tmp2);
		tmp1[0]=2;tmp1[1]=2;	tmp2[0]=4;tmp2[1]=8;tmp2[2]=4;
		target1List.push_back(tmp1);
		target2List.push_back(tmp2);
	}

	int bgnIdx=3;
	for(int d=3;d<=max_digit;++d){
		makeTargetNum(d,bgnIdx);
	}

	int size= target2List.size();
	int lastSize=-1;
	rep(i,size){
		vi target2		=target2List[i];
		int target2size	=target2.size();
		if(target2size>lastSize){
			for(int j=lastSize+1;j<=target2size;++j){
				dicIndex.insert(pair<int,int>(j,i));
			}
			lastSize=target2size;
		}
	}
}

int main(int argc, char** argv)
{	
	if(argc<2)return 0;

	string in_file=argv[1];
	freopen(in_file.c_str(),"r",stdin);
	freopen((in_file.substr(0,in_file.find_last_of("."))+".out").c_str(),"w",stdout);
	init(MAX_DIGITS);
	

	int n_cases;
	cin >> n_cases;cin.ignore();
	rep(i,n_cases){
		cout << "Case #" << i+1 << ": ";
		alg();
		cout << endl;
	}
	return 0;
}
