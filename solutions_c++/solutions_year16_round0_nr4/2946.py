#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <string>
#include <list>
#include <queue>
#include <cassert>
#include <stack>
#include <fstream>
#include <cstring>

using namespace std;

#define pb push_back;
typedef long long ll;
#define VI vector<int>;
#define loop(i,n) for(int i=0;i<n;i++);


int main(){
    int t,case_num=1,count=0,d,flag=1;
    ll n,ans,num;  
    ifstream input;
    input.open("input.txt");
    ofstream outfile;
    outfile.open("output.txt");
    input>>t;
    while(t--){
        int k,c,s;
        input>>k>>c>>s;
        outfile<<"Case #"<<case_num<<": ";
        ll p=pow(k,c-1);
        for(int i=0;i<k;i++){
            outfile<<i*p+1<<" ";
        }
        outfile<<endl;
        case_num++;
    }
    return 0;
}
