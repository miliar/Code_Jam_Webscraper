#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <ctime>
#include <cctype>
#include <iomanip>
#include <algorithm>
#include <list>
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#define rerm(i,l,u,m) for(int (i)=(int)(l);(i)<=(int)(u);(i)+=(m))
typedef long long int lli;
typedef long long ll;
typedef unsigned long long int ulli;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
#define pb(x) push_back(x)
#define modu 1000000007

int arrayofno[90000];

int main() {
    int t,s=0;

    int n,i ,j,max_1,min_1,summation;

    //ifstream fin ("B-large.in");
    cin>>t ;
    s=t;
    while(t--)
	 {
        cin>>n;
        for(i=0;i<n;i++)
		{
            cin>>arrayofno[i] ;
            max_1 = max(max_1,arrayofno[i]) ;
        }

        min_1 = max_1 ;

        for(i=1;i<=max_1;i++)
		{
            summation=i ;
            for(j=0;j<n;j++)
	 {
                if( arrayofno[j] > i ) {
                    if( arrayofno[j]%i == 0 )
                        summation += (arrayofno[j]/i-1) ;
                    else
                        summation += (arrayofno[j]/i) ;
                }
            }
            min_1 = min(min_1,summation) ;
        }
        cout<<"Case #"<<(s-t)<<": "<<min_1<<endl;
    }
    return 0 ;
}
