#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <complex>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)
#define ALL(x) (x).begin(),(x).end()
#define LL long long

using namespace std;

vector<int> ll_to_vll(LL N){
    vector<int> numbers;
    while(N){
        numbers.push_back(N%10);
        N /= 10;
    }
    return numbers;
}

LL vll_to_ll(vector<int> numbers){
    LL res = 0;
    while(!numbers.empty()){
        res *= 10LL;
        res += numbers.back();
        numbers.pop_back();
    }
    return res;
}


struct Node{
    LL n, c, p;
    Node(){}
    Node(LL _n,LL _c, LL _p):n(_n),c(_c),p(_p){}
    bool operator<(const Node &n)const{
        return c > n.c;
    }
};
LL solve(LL N){
    priority_queue<Node> que;

    que.push(Node(0,0, -2));

    vector<LL> used(10000000, -1);

    LL res = 1LL<<50;
    while(!que.empty()){
        Node node = que.top();que.pop();
        if(used[node.n]!=-1)continue;
        used[node.n] = node.p;
        if(node.n==N){
            res = node.c;
            LL now = node.n;
            while(now!=-2){
                //if(abs(now-used[now])!=1)cout << now << " " << used[now] << endl;
                now = used[now];
            }
            break;
        }



        LL next = node.n + 1;
        if(used[next]==-1)que.push(Node(next,node.c+1, node.n));

        vector<int> numbers = ll_to_vll(node.n);
        vector<int> reversed_numbers = numbers;
        reverse(ALL(reversed_numbers));
        LL reversed = vll_to_ll(reversed_numbers);
        if(used[reversed]==-1)que.push(Node(reversed,node.c+1, node.n));
    }
    return res;
}

int main(){
    int T;
    cin >> T;
    REP(test_case,T){
        LL N;
        cin >> N;
        cout << "Case #" << test_case + 1 << ": " << solve(N) << endl;
    }
    return 0;
}
