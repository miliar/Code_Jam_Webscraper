#include <iostream>
#include <cstdio>
#include <cassert>

using namespace std;

//after N rounds, there are 2^N possible records, so every possible record happens
//we just need to figure out who can be in the top p!


typedef unsigned long long ull;


//as long as you're not the highest, you can lose

ull ensured_win(int n,ull p){
    assert(p>=0);
    if(p>=((1ULL)<<n)){
        return ((1ULL)<<n)-1ULL;//everyone winds
    }
    else{
        if(p>((1ULL)<<(n-1))){
            //can win or lose
            return 2ULL*(ensured_win(n-1,p-((1ULL)<<(n-1)))+1ULL);
        }
        else{
            //must win
            return 0ULL;
        }
    }
}

//now note the lowest rank that can pass any particular round is 2^N-2, since that person could be at the optimal place, and then win.

//to achive rank r in the next round, we must be in rank

ull maybe_win(int n, ull p){
    assert(p>=0);
    if(p>=(1ULL<<n)){
        return (1ULL<<n)-1;//everyone wins
    }
    if(p>((1ULL)<<(n-1))){
        //we can lose this round
        ull fst = 2ULL*maybe_win(n-1,p-((1ULL)<<(n-1)))+1ULL;
        //or we can win of course
        ull snd = 2ULL*maybe_win(n-1,p);
        return max(fst,snd);
    }
    else{
        //we must win this round
        return 2ULL*maybe_win(n-1,p);
    }
}

int main(){
    int T;
    cin >> T;
    for(int c=0;c<T;c++){
        int N;
        ull P;
        cin >> N >> P;
        ull a = ensured_win(N,P);
        ull b = maybe_win(N,P);
        printf("Case #%d: %lld %lld\n",c+1,a,b);
    }
}
