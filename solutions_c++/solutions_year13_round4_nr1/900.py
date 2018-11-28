#include<iostream>
#include<algorithm>

using namespace std;
int n, m, pas[10500], o, e, p, T;
int cost(int distance){
    return distance * n - distance * (distance - 1) / 2;
}

int solve(){
    fill(pas, pas + 10500, 0);
    cin >> n >> m;
    int res = 0;
    for(int i = 0;i < m;i++){
	cin >> o >> e >> p;
	res += p * cost(abs(e - o));
	if(e < o){
	    for(int i = e;i < o;i++){
		pas[i] += p;
	    }
	}
	else{
	    for(int i = o;i < e;i++){
		pas[i] -= p;
	    }
	}
    }
    while(true){
	int now = 0;
	bool b = true;
	for(int i = 1;i <= n;i++){
	    if(pas[i] > 0){
		pas[i]--;
		now++;
		b = false;
	    }
	    else{
		res -= cost(now);
		now = 0;
	    }
	}
	if(b)break;
    }
    while(true){
	int now = 0;
	bool b = true;
	for(int i = 1;i <= n;i++){
	    if(pas[i] < 0){
		pas[i]++;
		now++;
		b = false;
	    }
	    else{
		res -= cost(now);
		now = 0;
	    }
	}
	if(b)break;
    }
    return res;
}

int main(){
    cin >> T;
    for(int t = 1;t <= T;t++){
	cout << "Case #" << t << ": " << solve() << endl;
    }
    return 0;
}
