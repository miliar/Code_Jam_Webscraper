#include <iostream>
#include <cstdio>
#include <cstring>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <ctime>
#include <cstring>
#include <sstream>
#include <fstream>
using namespace std;
bool compare(double x, double y){
    return (x>y);
}
int war(double naomi[], double ken[], int n)
{
    int n_wins=0, k_max=0;
    for(int i=0; i<n; ++i){
        if(naomi[i]>ken[k_max]){
            n_wins++;
        }
        else{
            k_max++;
        }
    }
    return n_wins;
}
int De_war(double naomi[], double ken[], int n)
{
    int n_max=0, n_wins=0;
    for(int i=0; i<n; ++i){
        if(naomi[n_max]>ken[i]){
            n_wins++;
            n_max++;
        }
    }
    return n_wins;
}
int main( )
{   
    /*clock_t start;
    start=clock();
    /***********************************************/
    freopen("D-large.in", "rt", stdin);
    freopen("D-large.out", "wt", stdout);
    int t;
    cin>>t;
    for(int i=1; i<t+1; ++i) {
        cout<<"Case #"<<i<<": ";
        int n;
        cin>>n;
        double naomi[n], ken[n];
        for(int j=0; j<n; ++j){
            cin>>naomi[j];
        }
        for(int j=0; j<n; ++j){
            cin>>ken[j];
        }
        sort(naomi, naomi+n, compare);
        sort(ken, ken+n, compare);
        cout<<De_war(naomi, ken, n)<<" ";
        cout<<war(naomi, ken, n)<<endl;
    }
    /************************************************
    start=clock()-start;
    printf("Time = %f\n", (float)start/CLOCKS_PER_SEC);*/
    return 0 ;
}