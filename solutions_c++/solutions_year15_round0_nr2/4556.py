#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>
#include <fstream>
#include <iomanip>
using namespace std;
typedef long long ll; 
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<int, bool> pib;
#define MOD %1000003
//ofstream sout("code1.out");

void printvec(vector<int> v){
    //sout<<"printing vector"<<endl;
    for(int i=0;i<v.size();i++){
        //sout<<v[i]<<" ";
    }   
    //sout<<endl;
}
int timefn(vector<int> v){
    int t1,t2,max=0,index=0;
    //printvec(v);
    if(v.size()==0) {
        //sout<<"all pancakes eaten"<<endl;
        return 0;
    }
    vector <int> v1,v2;
    v1.clear();v2.clear();
    for(int i=0;i<v.size();i++){
        v2.push_back(v[i]);
        if(v[i]>1)
            v1.push_back(v[i]-1);
        if(v[i]>max){
            max=v[i];
            index=i;
        }
    }
    if(v[index]%9==0){
        v2.push_back(v2[index]-(v2[index])/3);
        v2[index]=(v2[index])/3;
    }
    else{
        v2.push_back(v2[index]-(v2[index]+1)/2);
        v2[index]=(v2[index]+1)/2;
    }
    
    if(max<=3){
        //sout<<"all plates have 1 more pancake left to be eaten in 1 second"<<endl;
        return max;
    }
    //sout<<"first vector"<<endl;
    t1=timefn(v1)+1;
    //sout<<"second vector"<<endl;
    t2=timefn(v2)+1;
    v1.clear();
    v2.clear();
    return min(t1,t2);
}

int main(){
    ios_base::sync_with_stdio(false);cin.tie(0);
    ifstream fin("B-small-attempt3.in");
    ofstream fout("output.out");
    int t,n,temp,ans;
    std::vector<int> v;
    fin>>t;
    for(int nCases=1;nCases<=t;nCases++){
        v.clear();
        fin>>n;
        for(int i=0;i<n;i++){
            fin>>temp;
            v.push_back(temp);
        }
        ans=timefn(v);
        //sout<<"Case #"<<nCases<<": "<<ans<<endl<<endl<<endl;
        fout<<"Case #"<<nCases<<": "<<ans<<endl;
    }
    //system ("pause");
    return 0;
}  
