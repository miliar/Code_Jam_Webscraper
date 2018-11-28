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
int t,i,j,a,b[4][4],x,ans,num;
vector<int >v;
vector<int >u;
int main(){
    ifstream fin;
    ofstream fout;
    fout.open("magictrickoutput.txt");
    fin.open("inp.txt");
    fin>>t;
    x=1;
    while(t--){
    	ans=0;
    	fin>>a;
    	for(i=0;i<4;i++){
    		for(j=0;j<4;j++){
    			fin>>b[i][j];
    		}
    	}
    	for(i=0;i<4;i++){
    		v.push_back(b[a-1][i]);
    	}
    	sort(v.begin(),v.end());
    	fin>>a;
    	for(i=0;i<4;i++){
    		for(j=0;j<4;j++){
    			fin>>b[i][j];
    		}
    	}
    	for(i=0;i<4;i++){
    		u.push_back(b[a-1][i]);
    	}
    	sort(v.begin(),v.end());
    	for(i=0;i<4;i++){
    		for(j=0;j<4;j++){
    			if(v[i]==u[j]){
    			   num=v[i];
			       ans++;
				   break;	
    		    }
    		}
    	}
    	if(ans==1){
    		fout<<"Case #"<<x<<": "<<num<<endl;
    	}
    	else if(ans>1){
    		fout<<"Case #"<<x<<": "<<"Bad magician!"<<endl;
    	}
    	else{
    		fout<<"Case #"<<x<<": "<<"Volunteer cheated!"<<endl;
    	}
      x++;
      v.clear();
      u.clear();
    }
    fout.close();
    return 0;
}
