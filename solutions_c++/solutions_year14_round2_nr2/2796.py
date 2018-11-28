//Abdul Rais
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define MAX 55
using namespace std;
long long int a,b,k,ans,i,j,t,x,p;
int main(){
    ifstream fin;
    ofstream fout;
    fout.open("NewLotteryGameOutputSmall.txt");
    fin.open("NewLotteryGameInputSmall.txt");
    fin>>t;
    x=1;
    while(t--){
    	ans=0;
    	fin>>a>>b>>k;
    	for(i=0;i<a;i++){
    		for(j=0;j<b;j++){
    			p=i&j;
    			if(p<k){
    				ans++;
    			}
    		}
    	}
    	fout<<"Case #"<<x<<": "<<ans<<endl;
    	x++;	
    }
    fout.close();
    return 0;
}
