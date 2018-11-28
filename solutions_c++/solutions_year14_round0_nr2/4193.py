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
int t,p;
double c,f,x,ans,r,a,b,ans1;
int main(){
    ifstream fin;
    ofstream fout;
    fout.open("CookieClickerAlphaoutputLarge.txt");
    fin.open("inp.txt");
    fin>>t;
    p=1;
    while(t--){
    	r=2.0;
    	ans=0;
    	ans1=0;
    	fin>>c>>f>>x;
    	if(c>=x){
    		ans1=x/r;
    		fout<<"Case #"<<p<<": "<<setprecision(12)<<1.0*ans1<<endl;
    	}
    	else{
    		while(1){
    			b=x/r;
    			a=c/r+(x/(r+f));
    			ans1=ans;
    			ans+=c/r;
    			r+=f;
    			if(b<=a){
    				ans1+=b;
    				break;
    			}
    		}
    		fout<<"Case #"<<p<<": "<<setprecision(12)<<1.0*ans1<<endl;
    	}
      p++;
    }
    fout.close();
    return 0;
}
