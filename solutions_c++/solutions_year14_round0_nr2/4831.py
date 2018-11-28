#include  <vector>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <fstream>
using namespace std;
double cost, farm, need;
double res;

double solve(int n, double time, double tmp){
    tmp=min(tmp,time+need/(n*(farm)+2));
    if(time>=tmp) return tmp;


    return solve(n+1,time+cost/(n*(farm)+2),tmp);

}

int main(){

    ofstream myfile;
    myfile.open("output.txt");
    cout.precision(7);
    int t;
    ios::sync_with_stdio(0);

        cin>>t;

        	for (int i = 1; i <= t; ++i)
        	{
        		cin>>cost;
        		cin>>farm;
        		cin>>need;

        		res=solve(0, 0,need/2);
        		myfile<<"Case #"<<i<<": "<<fixed<<res<<'\n';
        	}



    myfile.close();
    return 0;
}

