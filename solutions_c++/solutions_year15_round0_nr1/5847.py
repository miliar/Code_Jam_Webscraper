#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <set>
#include <numeric> //accumulate(i poczatek,i koniec, wartosc_poczatkowa)
#include <utility> //swap
#include <map>
#include <cmath>
#include <functional> //for greater<>
using namespace std;

typedef vector<int> VI;
typedef long long LL;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
int main (int argc, char * const argv[]) {
#ifndef ONLINE_JUDGE
    if(!freopen("A-large.in", "r", stdin)) cout<<"Blad odczytu in.txt"<<endl;
    if(!freopen("out.txt", "w", stdout)) cout<<"Blad pliku wyjsciowego"<<endl;
#endif
	ios_base::sync_with_stdio(0);
	int numOfTestCases;
    cin>>numOfTestCases;
    FOR(numOfTestCase,1,numOfTestCases){
        int ile;
        string lancuch;
        cin>>ile>>lancuch;
        int tab[10000];
        int sumakontrolna[10000];
        memset(tab,0,sizeof(tab));
        memset(sumakontrolna,0,sizeof(sumakontrolna));
        REP(i,lancuch.length())
        tab[i]=lancuch[i]-'0';
        REP(i,SIZE(lancuch))
        {
            if(i==0)
                sumakontrolna[i]=0;
            else if(i==1)
                sumakontrolna[i]=tab[i-1];
            else sumakontrolna[i]=sumakontrolna[i-1]+tab[i-1];
        }
        int rozwiazanie=0;
        //REP(i,SIZE(lancuch))
        //cout<<numOfTestCase<<" " << i<< " "<<sumakontrolna[i]<<endl;
        for(;;rozwiazanie++){
            bool daSie=1;
            REP(poz,SIZE(lancuch)){
                if(sumakontrolna[poz]+rozwiazanie<poz){
                    //cout<<"numer testu "<<numOfTestCase<<" poz "<<poz<<" tab "<<tab[poz]<<" sumakont "<<sumakontrolna[poz]<<" rozw "<<rozwiazanie<<endl;
                    daSie=0;
                    break;
                }
            }
            if(daSie) break;
            
        }
        cout<<"Case #"<<numOfTestCase<<": "<<rozwiazanie<<endl;
    }
	
	
    return 0;
}