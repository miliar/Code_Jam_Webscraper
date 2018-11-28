#include <cmath>
#include <climits>
#include <queue>
#include <vector>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iomanip>   
#include <iostream>  
#include <sstream>  // istringstream buffer(myString);
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <set>
#include <unordered_map>
#include <unordered_set>
using namespace std;
#define gcd                         __gcd
#define OR |
#define AND &
#define XOR ^
#define bit(x,i) (x&(1<<i))  //select the bit of position i of x
#define lowbit(x) ((x)&((x)^((x)-1))) //get the lowest bit of x
#define hBit(msb,n) asm("bsrl %1,%0" : "=r"(msb) : "r"(n)) //get the highest bit of x, maybe the fastest
#define max(a,b) (a<b?b:a)
#define IN(i,l,r) (l<i&&i<r) //the next for are for checking bound
#define LINR(i,l,r) (l<=i&&i<=r)
#define LIN(i,l,r) (l<=i&&i<r)
#define INR(i,l,r) (l<i&&i<=r)
#define F(i,L,R) for (int i = L; i < R; i++) //next four are for "for loops"
#define FE(i,L,R) for (int i = L; i <= R; i++)
#define FF(i,L,R) for (int i = L; i > R; i--)
#define FFE(i,L,R) for (int i = L; i >= R; i--)
#define getI(a) scanf("%d", &a) //next three are handy ways to get ints, it's also force you to use '&' sign
#define getII(a,b) scanf("%d%d", &a, &b)
#define getIII(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define wez(n) int (n); scanf("%d",&(n)) //handy if the input is right after the definition of a variable
#define wez2(n,m) int (n),(m); scanf("%d %d",&(n),&(m))
#define wez3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k))
#define TESTS wez(testow)while(testow--) //for multilple cases problems
#define whileZ int T; getI(T); while(T--) // the same as above
#define getS(x) scanf("%s", x) //get a char* string
#define clr(a,x) memset(a,x,sizeof(a)) //set elements of array to some value
#define char2Int(c) (c-'0')
#define lastEle(vec) vec[vec.size()-1] 
#define SZ(x) ((int)((x).size()))
#define REMAX(a,b) (a)=max((a),(b)) // set a to the maximum of a and b
#define REMIN(a,b) (a)=min((a),(b));
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++) // traverse an STL data structure
#define ALL(c) (c).begin(),(c).end() //handy for function like "sort()"
#define PRESENT(c,x) ((c).find(x) != (c).end()) 
#define CPRESENT(c,x) (find(ALL(c),x) != (c).end()) 
#define ll long long //data types used often, but you don't want to type them time by time
#define ull unsigned long long
#define ui unsigned int
#define us unsigned short
#define IOS ios_base::sync_with_stdio(0); //to synchronize the input of cin and scanf
#define INF 1001001001
#define PI 3.1415926535897932384626
//for map, pair
#define mp make_pair
#define fi first
#define se second
// for debug
inline void pisz(int n) { printf("%d\n",n); }
#define DBG(vari) cerr<<#vari<<" = "<<(vari)<<endl;
#define printA(a,L,R) FE(i,L,R) cout << a[i] << (i==R?'\n':' ')
#define printV(a) printA(a,0,a.size()-1)
#define MAXN 10000
//for vectors
#define pb push_back
typedef int elem_t;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 

int main()
{
    int t;
    getI(t);
    int a = 1;
    while(t--)
    {
    	string s;
    	cin >> s;
    	string ans;
    	vector<int> let(26, 0);
    	int dig = s.size();
    	for(int i = 0; i < dig; ++i)
    	{
    		let[s[i]-'A']++;
    	}
    	//find 0
    	while(true)
    	{
    		int x0 = 0;
    		x0 = min(let[25], min(let[4], min(let[17], let[14])));
    		let[25] -= x0;
    		let[4] -= x0;
    		let[17] -= x0;
    		let[14] -= x0;
    		for(int i = 0; i < x0; ++i)
    			ans += '0';
    		int x6 = 0;
    		x6 = min(let[23], min(let[8], let[18]));
    		let[23] -= x6;
    		let[8] -= x6;
    		let[18] -= x6;
    		for(int i = 0; i < x6; ++i)
    			ans += '6';
    		int x2 = 0;
    		x2 = min(let[19], min(let[22], let[14]));
    		let[19] -= x2;
    		let[22] -= x2;
    		let[14] -= x2;
    		for(int i = 0; i < x2; ++i)
    			ans += '2';
    		int x4 = 0;
    		x4 = min(let[5], min(let[14], min(let[20], let[17])));
    		let[5]-= x4;
    		let[14] -= x4;
    		let[20] -= x4;
    		let[17] -= x4;
    		for(int i = 0; i < x4; ++i)
    			ans += '4';
    		int x8 = 0;
    		x8 = min(let[4], min(let[8], min(let[6], min(let[7], let[19]))));
    		let[4]-= x8;
    		let[8] -= x8;
    		let[6] -= x8;
    		let[7] -= x8;
    		let[19] -= x8;
    		for(int i = 0; i < x8; ++i)
    			ans += '8';
    		int x5 = 0;
    		x5 = min(let[5], min(let[8], min(let[4],let[21])));
    		let[5]-= x5;
    		let[8] -= x5;
    		let[21] -= x5;
    		let[4] -= x5;
    		for(int i = 0; i < x5; ++i)
    			ans += '5';
    		int x3 = 0;
    		x3 = min(let[19], min((int)floor(let[4]/2), min(let[7], let[17])));
    		let[19]-= x3;
    		let[17] -= x3;
    		let[7] -= x3;
    		let[4] -= x3*2;
    		for(int i = 0; i < x3; ++i)
    			ans += '3';
    		int x7 = 0;
    		x7 = min(let[18], min((int)floor(let[4]/2), min(let[21], let[13])));
    		let[18]-= x7;
    		let[13] -= x7;
    		let[21] -= x7;
    		let[4] -= x7*2;
    		for(int i = 0; i < x7; ++i)
    			ans += '7';
    		int x9 = 0;
    		x9 = min(let[8], min((int)let[13]/2, let[4]));
    		let[8]-= x9;
    		let[13] -= x9*2;
    		let[4] -= x9;
    		for(int i = 0; i < x9; ++i)
    			ans += '9';
    		int x1 = 0;
    		x1 = min(let[14], min(let[13], let[4]));
    		for(int i = 0; i < x1; ++i)
    			ans += '1';
    		let[14]-= x1;
    		let[13] -= x1;
    		let[4] -= x1;
    		break;
    	}
    	sort(ans.begin(), ans.end());
    	cout << "Case #" << a << ": " << ans << endl;
    	a++;

    }
}
