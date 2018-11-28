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

int main(){
    ios_base::sync_with_stdio(false);cin.tie(0);
    ifstream fin("A-large.in");
    ofstream fout("A-large.txt");
    int t,count;
    int n;
    vector<int> a;
    string s;
    fin>>t;
    for(int cases=1;cases<=t;cases++){
		//cout<<endl<<endl<<"new test case!"<<endl;
        count=0;
        a.clear();
        fin>>n;
        fin>>s;
        a.push_back((int)(s[0]-'0'));
        if(a[0]==0){
            a[0]=1;
            count++;
        }
        for(int i=1;i<s.length()-1;i++){
            a.push_back((int)(s[i]-'0'));
            //cout<<"initial a["<<i<<"]:"<<a[i]<<endl;
            a[i]+=a[i-1];
            //cout<<"cumulative a["<<i<<"]:"<<a[i]<<endl;
            if(a[i]<i+1){
                //cout<<i<<" "<<a[i]<<endl;
                count+=1+i-a[i];
                a[i]=i+1;
            }
            //cout<<"final cumulative a["<<i<<"]:"<<a[i]<<endl<<endl;
        }
        fout<<"Case #"<<cases<<": "<<count<<endl;

    }

    //system ("pause");
    return 0;
}  
