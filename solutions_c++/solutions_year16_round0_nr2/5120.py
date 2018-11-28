#include<bits/stdc++.h>

using namespace std;

#define FOR(i,a,b)   	for(int (i)=(a);(i)<(b);(i)++)
#define PB           	push_back
#define INF          	(1 << 26)
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

int flip(int mask, int len) {
	string st = "";
	FOR(i,0,len) {
		if(iset(mask, i))st += "1"; 
		else st += "0";
	}

	int ind = 0;
	for(int i = len-1; i >= 0; i--) {
		if(st[i] == '1')dounset(mask, ind);
		else doset(mask, ind);
		ind++;
	}
	return mask;
}

const int LM = 65543;
int dep[LM], vis[LM];
int solve(int mask, int len) {

	queue<int> qu;
	clr(vis, 0);

	vis[mask] = 1;
	dep[mask] = 0;
	qu.push(mask);

	while(qu.size() > 0) {
		int umask = qu.front(); qu.pop();
		FOR(i,1,len+1) {
			int vmask = flip(umask, i);
			if(vis[vmask] == 0) {
				vis[vmask] = 1;
				dep[vmask] = dep[umask]+1;
				qu.push(vmask);
			}
		}
	}

	return dep[0];
}

int main() {
    
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B_out_small.txt", "w", stdout);
    
    int T;
    scanf("%d", &T);

    FOR(t,0,T) {
    	string st;
    	cin >> st;

    	int mask=0;
    	FOR(i,0,st.S)if(st[i] == '-')doset(mask, i);
		printf("Case #%d: %d\n", t+1, solve(mask, st.S));
    }
    
    return 0;
}

/*                       _        _                       _           _ 
         ___  ___  _   _| |    __| | ___ _ __   __ _ _ __| |_ ___  __| |
        / __|/ _ \| | | | |   / _` |/ _ \ '_ \ / _` | '__| __/ _ \/ _` |
        \__ \ (_) | |_| | |  | (_| |  __/ |_) | (_| | |  | ||  __/ (_| |
        |___/\___/ \__,_|_|___\__,_|\___| .__/ \__,_|_|   \__\___|\__,_|
        Mukit Hasan, Jahangirnagar University.*/
