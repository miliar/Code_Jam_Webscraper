#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <cassert>
#include <complex>

using namespace std;

#define ST first
#define ND second
#define MP make_pair
#define PB push_back

typedef long long LL;
typedef long double LD;

typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
#define ZERO(x) memset(x,0,sizeof(x))

#define fabsl __builtin_fabsl
#define atan2l __builtin_atan2l
#define cosl __builtin_cosl
#define sinl __builtin_sinl
#define sqrtl __builtin_sqrtl

struct Event {
    int time;
    int zombie;
};

bool operator < (const Event& a, const Event& b) {
    return a.time < b.time;
}

struct Zombie {
    int x, y;
    int start;
    vector<int> my_events;
};

void alg2() {
    int n;
    cin >> n;
    vector<Zombie> zombies(n);
    vector<Event> events;
    events.reserve(1001 * n);
    for (int i = 0; i < n; ++i) {
        cin >> zombies[i].x >> zombies[i].y >> zombies[i].start;
        for (int j = zombies[i].start; j <= zombies[i].start + 1000; ++j) {
            Event event;
            event.time = j;
            event.zombie = i;
            events.PB(event);
        }
    }

    sort(ALL(events));

    for (int i = 0; i < (int) events.size(); ++i) {
        zombies[events[i].zombie].my_events.push_back(i);
    }

    vector<int> dp(events.size(), 0);
    for (int i = 0; i < (int) events.size(); ++i) {
        int needed = max(abs(zombies[events[i].zombie].x), abs(zombies[events[i].zombie].y)) * 100;
        if (needed <= events[i].time) {
            dp[i] = 1;
        }
    }
    int result = 0;
    for (int i = 0; i < (int) events.size(); ++i) {
        if (dp[i] == 0) {
            continue;
        }
        result = max(result, dp[i]);
        const Zombie& cur = zombies[events[i].zombie];
        FORE (it, zombies) {
            if (it - zombies.begin() != events[i].zombie) {
                int needed = max(abs(cur.x - it->x), abs(cur.y - it->y)) * 100;
                needed = events[i].time + max(needed, 750);
                if (needed <= it->start + 1000) {
                    int ev = it->my_events[max(0, needed - it->start)];
                    dp[ev] = max(dp[ev], dp[i] + 1);
                }
            }
        }
    }
    cout << result << endl;
}

#define NUMBER 4

char table[NUMBER][NUMBER];
char result[100];
const char * resultado[]={"X won","O won","Draw","Game has not completed"};
int win=-1;
bool notfinis=false;
map<char,int> myset;
	
bool winnerE(){
	if (myset.size()>2)
		return (false);
	if (myset.size()==1)
	{
		if(myset.count('X'))
			return (win=0);
		else 
			if(myset.count('O'))
			return (win=1);
		else 
			return false;
	}
	if (myset.size()==2){
		if(myset.count('X') && !(myset.count('O') ||myset.count('.')))
			return (win=0);
		else 
			if(myset.count('O') && !(myset.count('X') ||myset.count('.')))
					return (win=1);
	}	
	
	
	}

void horizontal(){
	
	REP(i,NUMBER){
		myset.clear();
		REP(j,NUMBER){
			
			myset[table[i][j]]+=1;
			if (table[i][j]=='.')
			{	//cout<<table[i][j]<<"DDD"<<i<<" "<<j<<endl;
				notfinis=true;
			
			}
		}
		winnerE();
		if (win>=0) return;
	}
}

void vertical(){

	REP(j,NUMBER){
		myset.clear();
		REP(i,NUMBER){
			
			myset[table[i][j]]+=1;
			
		}
		winnerE();
		if (win>=0) return;
	}
}

void diagonal(){


		myset.clear();
		REP(j,NUMBER){
			myset[table[j][j]]+=1;
		}
		winnerE();
		if (win>=0) return;

	
		myset.clear();
		REP(j,NUMBER){
			myset[table[j][NUMBER-1-j]]+=1;
			//cout<<table[j][NUMBER-1-j]<<endl;
		}
		winnerE();
		if (win>=0) return;
}




void alg() {
    int n;win=-1;notfinis=false;
	
	horizontal();
	vertical();
	diagonal();
	if (win<0){
		if (notfinis)
			cout << resultado[3] << endl;
		else//draw
			cout << resultado[2] << endl;
	}
	else //some winner
			cout << resultado[win] << endl;
}




void leer(){
	
	REP(i,4)
		REP(j,4){
			cin>>table[i][j];
		}
	
}

int main() {
    int n_cases;
    cin >> n_cases;
    for (int test_case = 1; test_case <= n_cases; ++test_case) {
        cout << "Case #" << test_case << ": ";
        leer();
        alg();
    }
}
