#include<bits/stdc++.h>

using namespace std;

#define FOR(i,a,b)   	for(int (i)=(a);(i)<(b);(i)++)
#define PB           	push_back
#define INF          	(1 << 30)
#define DEBUG(___x)     cout<<#___x<<" = ["<<___x<<"]"<<endl
#define SORT(___a)      sort(___a.begin(),___a.end())
#define RSORT(___a)     sort(___a.rbegin(),___a.rend())
#define PI           	3.141592653589793238
#define MP           	make_pair
#define PII          	pair<int,int>
#define ALL(___v)       (___v).begin(), (___v).end()
#define VS           	vector<string>
#define VI           	vector<int>
#define S            	size()
#define B				begin()
#define E				end()
#define print(___v)     {cout<<"[";if(___v.S)cout<<___v[0];FOR(___i,1,___v.S)cout<<","<<___v[___i];cout<<"]\n";}
#define clr(___x, ___v)	memset(___x, ___v , sizeof ___x);
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)


int tu(int val) {return (1 << val);}
bool iset(int mask, int id) {if((mask & tu(id) ) != 0)return true;return false;}
void doset(int &mask, int id) {mask |= tu(id);}
void dounset(int &mask, int id) {mask = mask & (~tu(id));}

typedef long long 					bint;
template<typename T> string tos( T a ) 	{ stringstream ss; string ret; ss << a; ss >> ret; return ret;}

int arr[100000];

int main() {
	
	//freopen("in.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A_out_large.txt", "w", stdout);
	
	int T, N, va, vb, sp;
	cin >> T;
	
	FOR(t,0,T) {
        
        cin >> N;
        sp = va = vb = 0;
        FOR(i,0,N)cin >> arr[i];
        
        FOR(i,1,N) {
            if(arr[i] < arr[i-1]) {
                va += arr[i-1]-arr[i];
                sp = max(sp, arr[i-1]-arr[i]);
            }
        }
        
        vb = 0;
        FOR(i,0,N-1) {
            int taken = min(sp, arr[i]);
            vb += taken;
        }
        
        printf("Case #%d: %d %d\n", 1+t, va, vb);
	}
	
	return 0;
}
