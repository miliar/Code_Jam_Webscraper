#include <cstdio>
#include <cstdlib>
#include <cassert>
#include<cmath>
#include <iostream>
#include <vector>
#include<string>
using namespace std;
int main(){
    FILE *fin = freopen("B-large.in", "r", stdin);
    assert(fin!=NULL);
    FILE *fout = freopen("B-large.out", "w", stdout);
    int cases;
    cin>>cases;
    vector <string> lists;
    string s;
    for(int i=0;i<cases;i++) {

            cin>>s;
            lists.push_back(s);
    }
    for(int i=0;i<cases;i++){
            int moves=0;
            int prev=0;
            int siz=lists[i].length();
            for(int j=0;j<siz;j++){
                if((lists[i][siz-j-1]=='-') && (prev==0)){
                    moves+=1;
                    prev=1;
                }
                else if((lists[i][siz-j-1]=='+') && (prev==1)){
                    moves+=1;
                    prev=0;
                }
            }
            cout<<"Case #"<<i+1<<": "<<moves<<endl;
    }
}
