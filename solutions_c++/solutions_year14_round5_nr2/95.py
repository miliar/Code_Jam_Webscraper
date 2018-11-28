#include<iostream>
#include<fstream>
#include<string>
#include<bitset>
#include<algorithm>
#include<set>
#include<map>
using namespace std;

int H[100],G[100];
int Dhit[100], Thit[100];
int N,P,Q;

//int DP[num_monsters][num_turns]
map<int,int> DP;
int search(int, int,int);
int next_state(int i, int health, int turns){
    if (i>=N) return 0;
    if (health + Q >= H[i]){
        return search(i+1,0,turns + 1);
    }
    else{
        return search(i, health + Q, turns + 1);
    }
}

int search(int i, int health, int turns){
    if (turns < 0) return -1000000;
    if (i >= N) return 0;
    if (DP.find(i + health * 101 + turns * 101 * 201)!= DP.end()){
        return DP[i + health * 101 + turns * 101 * 201];
    }
    int s1 = next_state(i,health,turns);
    int s2;
    if (health + P >= H[i]){
        s2 = G[i] + search(i+1,0,turns - 1);
    }
    else{
        s2 = search(i, health + P, turns - 1);
    }
    DP[i + health * 101 + turns * 101 * 201] = max(s1, s2);
    return max(s1, s2);
}


int main(){
    ifstream in("B.in"); ofstream out("B.out");
    int T;
    in>>T;

    for (int t=0;t<T;t++){
        out<<"Case #"<<t+1<<": ";
        in>>P>>Q>>N;
        for (int i=0;i<N;i++) in>>H[i]>>G[i];
        DP.clear();
        out<<search(0,0,1)<<"\n";
    }
}
