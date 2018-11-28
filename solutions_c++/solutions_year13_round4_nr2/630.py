#include <iostream>
#include <cmath>

using namespace std;

long long worstPossible(int rounds, long long prizes) {
    long long numTeams = (long long) pow(2, rounds);
    int wins = rounds - ((int) log2(prizes));
    return numTeams - pow(2, wins);
}

int main() {
    int ncases;
    cin>>ncases;
    for(int caseNum=0; caseNum < ncases; caseNum++) {
        int rounds;
        long long prizes;
        cin>>rounds>>prizes;
        long long numTeams = (long long) pow(2, rounds);
        if(numTeams > prizes)
            cout<<"Case #"<<caseNum+1<<": "<<numTeams - worstPossible(rounds, numTeams - prizes) - 2<<" "<<worstPossible(rounds, prizes)<<"\n";
        else
            cout<<"Case #"<<caseNum+1<<": "<<numTeams - 1<<" "<<numTeams - 1<<"\n";
    }
}
