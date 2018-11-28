// author : theycallhimavi
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <iterator>
#include <set>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>
#include <string>
#include <list>
#include <queue>
#include <stack>
#include <ctype.h>
#include <iomanip>
#include <ctime>
#include <cstdlib>
#include <utility>
using namespace std;
/*inline int read_int() {
char c;
while ((c=getchar_unlocked()) < 48 || c > 57);
int p = c-48;
while ((c=getchar_unlocked()) >= 48 && c <= 57) p=p*10+c-48;
return p;
}*/

#define MAX(x,y) ((x)<(y) ? (y) : (x))
#define MIN(x,y) ((x)<(y) ? (x) : (y))
#define SWAP(x,y) do { a+=number_of_requred; number_of_requred=a-number_of_requred; a=a-number_of_requred; } while( 0 )
#define mod1 1000000007ll
#define mod2 10000007ll
#define inf 99999999999999999ll
#define REP(i,n) for(i=0;i<n;i++)
#define REPI(i,j,n) for(i=j;i<n;i++)
#define PER(i,n) for(i=n-1;i>=0;i--)
typedef vector<int> vi;
typedef pair<int, int> ii;

template <class T>
T power(T x,T y,T m)
{
	T temp;
	if( y == 0)
		return 1;
	temp = power(x,y/2,m)%m;
	if (y%2 == 0)
		return ((temp % m)*(temp% m))%m;
	else
		return (((((x)*(temp))%m)*(temp))%m)%m;
}


int main(){
     long long int cases,just_a_random_variable;
	 long long land,getsitdone,aa;
	 just_a_random_variable = land = 0;
     long long int j,A,number_of_requred;
     long long int Arr[] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};
     cin>>cases;
     while(cases--){
		vector<int>V1,V2;
        vector<vector<int> >V4;
        land++;
        cin>>A>>number_of_requred;
        just_a_random_variable = 39;
        if(A > Arr[just_a_random_variable-1]){
			cout<<0<<endl;
            continue;
        }
        if(number_of_requred > Arr[just_a_random_variable-1])
			number_of_requred = Arr[just_a_random_variable-1];
            for(int i = 0;i < just_a_random_variable;i++){
				if(Arr[i] >= A){
					getsitdone = i;
                    break;
				}
            }
            for(int i = 0;i < just_a_random_variable;i++){
				if(Arr[i] <= number_of_requred)
					aa = i;
            }
            cout<<"Case #"<<land<<": "<<aa-getsitdone+1<<endl;
     }
     return 0;
}