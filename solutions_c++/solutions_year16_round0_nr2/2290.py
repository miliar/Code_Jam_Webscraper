//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


int extra() {
    string pancakes;
    cin >> pancakes;
    pancakes += "+";
    int number = 0;
    For(i, pancakes.size()-1) number += (pancakes[i] != pancakes[i+1]);
    printf("%d\n", number);
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
