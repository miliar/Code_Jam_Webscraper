#include <bits/stdc++.h>
using namespace std;
#define read            freopen("C:\\Users\\Dell\\Desktop\\in.txt", "r", stdin)
#define write           freopen("C:\\Users\\Dell\\Desktop\\out.txt", "w", stdout)
#define pii             pair<int , int >
#define in(a)           scanf("%d", &a)
#define ins(a)          scanf("%s", a)
#define in2(a, b)       scanf("%d%d", &a, &b)
#define in3(a, b, c)    scanf("%d%d%d", &a, &b, &c)
#define pn              printf("\n")
#define pr(a)           printf("%d\n", a)
#define prs(a)          printf("%d ", a)
#define pr2(a, b)       printf("%d %d\n", a, b)
#define pr3(a, b ,c)    printf("%d %d %d\n", a, b, c)
#define MP              make_pair
#define vi              vector<int >
#define _ceil(n, a)     ((n)%(a)==0?((n)/(a)):((n)/(a)+1))
#define cl              clear()
#define sz              size()
#define pb              push_back
#define MEM(a, b)       memset((a), (b), sizeof(a))
#define all(X)          (X).begin(), (X).end ()
#define iter(it, X)     for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define ext(a)          {printf("%s\n", a); return 0;}
#define oka(x, y)       ((x)>=0&&(x)<row&&(y)>=0&&(y)<col)

// Debugger.begin()

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); pn;}
vector<string> split(const string& s, char c) {
	vector<string> v;
	stringstream ss(s);
	string x;
	while (getline(ss, x, c))
		v.emplace_back(x);
	return move(v);
}

void err(vector<string>::iterator it) {}
template<typename T, typename... Args>
void err(vector<string>::iterator it, T a, Args... args) {
	cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << '\n';
	err(++it, args...);
}

// Debugger.end()

typedef long long LL;
static constexpr int inf = std::numeric_limits<int >::max();
//int  dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int  dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int  dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//bool check(int n, int pos) {return (n & (1<<pos))>>pos;} //typecast 1 in case of int
//int  on(int n, int pos) {return n | (1<<pos);} //typecast 1 in case of int
//int  off(int n, int pos) {return n & ~(1<<pos);} //typecast 1 in case of int
//bool operator < (const data &d) const{return cost<d.cost;} //reverse in priority queue

const int M=500010;
int main()
{
#ifndef ONLINE_JUDGE
    read;
    write;
#endif
    int t, cs=0, i, j, k;
    char A[10100], last;
    deque<int>q;

    in(t);
    while (t--)
    {
        ins(A);
        while (!q.empty()) q.pop_front();

        int n=strlen(A);
        for (i=0; i<n; i++)
        {
            if (q.empty()) q.push_front(A[i]);
            else if (A[i]>=q.front()) q.push_front(A[i]);
            else q.push_back(A[i]);
        }

        printf("Case #%d: ", ++cs);
        while (!q.empty())
        {
            printf("%c", q.front());
            q.pop_front();
        }
        pn;
    }


return 0;
}
