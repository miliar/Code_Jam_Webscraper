#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
int getint()
{
	char ch;
	do
	{
		ch=getchar();
	}while (ch!='-'&&(ch<'0'||ch>'9'));
	int ans=0,f=0;
	if (ch=='-') f=1; else ans=ch-'0';
	while (isdigit(ch=getchar())) ans=ans*10+ch-'0';
	if (f) ans*=-1;
	return ans;
}
#define N 5
int F[N][N],S[N][N],a,b;
bool row[N];
int A[N],B[N];
int Solve(){
    int count=0,ans;
    for(int i=1 ; i<N ; i++){
            for(int j=1 ; j<N ; j++){
                if(A[i]==B[j]){
                    count++;
                    ans=i;
                }
            }
    }
    if(count==1)
        return ans;
    if(count==0)
        return 6;
    return 5;
}
int main()
{
	int testCases,n;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	testCases=getint();
	for(int k=1 ; k<=testCases ; k++){
        a=getint();
        for(int i=1 ; i<N ; i++){
            for(int j=1 ; j<N ; j++){
                F[i][j]=getint();
                if(i==a)
                    A[j]=F[i][j];
            }
        }
        b=getint();
        for(int i=1 ; i<N ; i++){
            for(int j=1 ; j<N ; j++){
                S[i][j]=getint();
                if(i==b)
                    B[j]=S[i][j];
            }
        }
        int solve=Solve();

        if(solve<=4)
            cout<<"Case #"<<k<<":"<<" "<<A[solve]<<endl;
        else if(solve==5)
            cout<<"Case #"<<k<<":"<<" "<<"Bad magician!"<<endl;
        else if(solve==6)
             cout<<"Case #"<<k<<":"<<" "<<"Volunteer cheated!"<<endl;
	}
	return 0;
}

