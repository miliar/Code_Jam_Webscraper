#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int M;
char S[1001];

int solve(){
	int standup = 0;
	int friends = 0;
	int need;
	int si;

	for(int i=0; i<=M; i++){

		si = S[i] - 48; // ascii

		if(si>0 && standup < i){
			need = i - standup;
			friends += need;
			standup += need;
		}
		standup += si;
	}
    return friends;
}

int main(){

    int T;
    scanf("%d", &T);

    freopen("out/Sample.out","w",stdout);

    for(int t=1; t<=T; t++)
    {
        scanf("%d", &M);
        scanf("%s", &S);
		cout << "Case #" << t << ": " << solve() << endl;
    }
}
