/* Author: Sandeep */

/* 1. Did u interpret the qns correctly ?
   2. Is your i/o correct ?
   3. Int overflow, double precesion
   4. Array size correct ?
   5. Clearing/resetting vector, map etc.
   6. Stack ovrflow
   7. Global/local conflict
   8. Check for obvious typo(most imp)
   9. Think about edge cases
*/

#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <memory.h>
#include <cassert>

using namespace std;

#define ford(i, a, b, c)        for(int i=(a); i<(b); i+=(c))
#define fori(i, a, b)           ford(i,a,b,1)
#define rep(i, n)               fori(i,0,n)
#define ifor(i, a, b)           for(int i=(a); i>=(b); i--)
#define iter(i, a)              for(typeof((a).begin()) i=(a).begin(); i!=(a).end(); i++)
#define si(x)                   ((int)x.size())
#define SS                      ({int x;scanf("%d",&x);x;})
#define pb                      push_back
#define mp                      make_pair
#define all(a)                  a.begin(),a.end()
#define fill(a, v)              memset(a, v, sizeof(a))
#define inf                     (int)1e9
#define linf                    (long long)1e18
#define V                       vector
#define S                       string
#define XX                      first
#define YY                      second
#define P(v)                    rep(i, si(v)) cout<<v[i]<<" "; puts("")

typedef V<int> vi;
typedef V<S> vs;
typedef long long ll;
typedef pair<int,int> pii;

ll powModN(ll a, ll b, ll c) {
    ll res = 1;
    while (b){
        if (b%2) res= (res*(ll)a)%c;
        b/=2;
        a=(a*(ll)a)%c;
    }
    return res;
}

/* Program Body starts here */
bool isPalindrome (int *array, int size) {
	rep(i,size) {
		if(array[i] != array[size-1-i]) {
			return false;
		}
	}
	return true;
}

bool isPalindrome(ll number) {
	vector <int> num;
	while(number) {
		num.pb(number%10);
		number = number/10;
	}
	int size = num.size();
	int *array = new int [size];
	rep(i,size) {
		array[i] = num[size-1-i];
	}
	return isPalindrome(array,size);
}

bool AreAll9s( int *array, int size )
{
    int i;
    for( i = 0; i < size; ++i )
        if( array[i] != 9 )
            return false;
    return true;
}

void generateNextPalindromeUtil (int *num, int n )
{
    int mid = n/2;
 	bool leftsmaller = false;
    int i = mid - 1;
    int j = (n % 2)? mid + 1 : mid;
    while (i >= 0 && num[i] == num[j])
        i--,j++;
    if ( i < 0 || num[i] < num[j])
        leftsmaller = true;
    while (i >= 0)
    {
        num[j] = num[i];
        j++;
        i--;
    }
 
    if (leftsmaller == true)
    {
        int carry = 1;
        i = mid - 1;
        if (n%2 == 1)
        {
            num[mid] += carry;
            carry = num[mid] / 10;
            num[mid] %= 10;
            j = mid + 1;
        }
        else
            j = mid;
 
        while (i >= 0)
        {
            num[i] += carry;
            carry = num[i] / 10;
            num[i] %= 10;
            num[j++] = num[i--]; // copy mirror to right
        }
    }
}

ll nextGreaterPalindrome (int *array, int size) {
	ll returnValue = 0;
	if(AreAll9s(array,size)) {
		returnValue = 1;
		rep(i,size) {
			returnValue = returnValue * 10;
		}
		returnValue = returnValue+1;
	} else {
		generateNextPalindromeUtil(array,size);
		rep(i,size) {
			returnValue = returnValue*10 + array[i];
		}
	}
	return returnValue;
}

ll nextPalindrome (ll number) {
	vector <int> num;
	ll returnedValue = number;
	//cout<<"Number is "<<number<<endl;
	while(number) {
		num.pb(number%10);
		number = number/10;
	}
	int size = num.size();
	int *array = new int [size];
	rep(i,size) {
		array[i] = num[size-1-i];
	}
	//cout<<"Next Palidrome is ";
	if(isPalindrome(array, size)) {
		//cout<<returnedValue<<endl;
		return returnedValue;
	}
	returnedValue = nextGreaterPalindrome(array, size);
	//cout<<returnedValue<<endl;
	return returnedValue;
}


ll main2 () {
	ll a,b;
	cin>>a>>b;
	ll minNumber = ceil(sqrt(a));
	minNumber = nextPalindrome(minNumber);
	int count = 0;
	while((minNumber*minNumber) <= b) {
		if(isPalindrome(minNumber*minNumber)) {
			count++;
		}
		minNumber = nextPalindrome(minNumber+1);
	}
	return count;
}

int main () {
	int T;
	cin >> T;
	rep (i,T) {
		cout<<"Case #"<<i+1<<": "<<main2()<<endl;
	}
}
