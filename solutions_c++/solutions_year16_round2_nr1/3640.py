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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <cstring>
#include <climits>
#include <iostream>
#include <cassert>
#define mod 1000000007
#define eps 1e-4
#define arsize 1000000001
#define INF 0x3f3f3f3f
#define NINF INT_MIN
#define INFL 0x3f3f3f3f3f3f3f3fLL
#define P 3.14159265358979323846264338327950288419716939937510
#define size 1000000
using namespace std;
//ofstream fout ("/Users/priya/Desktop/A-large.out");
//ifstream fin ("/Users/priya/Desktop/A-large.in");
// int a, b;
// fin >> a >> b;
// fout << a+b << endl;
//  freopen("in", "r", stdin);
//  freopen("out", "w", stdout);
//long long int sum(long int x){
//    long long int ans=0;
//    for(long int i=1;i<sqrt(x);++i)if(x%i==0&&i%2!=0)ans+=i;
//    return ans;
//}
int main()
{
    ifstream fin ("/Users/priya/Desktop/A-small-attempt2.in");
    ofstream fout ("/Users/priya/Desktop/A-small-attempt2.out");
    int t; fin>>t;
    for(int b=0;b<t;b++){
        vector<int> ans;
        string m; fin>>m;
        int z=0,e=0,r=0,o=0,n=0,t=0,w=0,h=0,f=0,u=0,i=0,v=0,s=0,x=0,g=0;
        for(int k=0;k<m.length();k++)
        {
            switch(m[k]){
                case 'Z':z++; break;
                case 'E':e++; break;
                case 'R':r++; break;
                case 'O':o++; break;
                case 'N':n++; break;
                case 'T':t++; break;
                case 'W':w++; break;
                case 'H':h++; break;
                case 'F':f++; break;
                case 'U':u++; break;
                case 'I':i++; break;
                case 'V':v++; break;
                case 'S':s++; break;
                case 'X':x++; break;
                case 'G':g++; break;
            }
        }
        fout<<"Case #"<<b+1<<":"<<" ";
    start:
        if(z!=0){
            for(int k=0;k<z;k++) ans.push_back(0);;
            e-=z;
            r-=z;
            o-=z;
            z=0; goto start;
        }
        else if(w!=0){
            for(int k=0;k<w;k++)ans.push_back(2);
            t-=w;
            o-=w;
            w=0;goto start;
        }
        else if(x!=0){
            for(int k=0;k<x;k++)ans.push_back(6);
            s-=x;
            i-=x;
            x=0;
            if(s!=0){
                for(int k=0;k<s;k++)ans.push_back(7);
                e-=2*s;
                v-=s;
                n-=s;
                s=0; goto start;
            }
            else goto start;
        }
        else if((x==0)&&(s!=0)){
            for(int k=0;k<s;k++)ans.push_back(7);
            e-=2*s;
            v-=s;
            n-=s;
            s=0; goto start;
        }
        else if(g!=0){
            for(int k=0;k<g;k++)ans.push_back(8);
            e-=g;
            i-=g;
            h-=g;
            t-=g;
            g=0; goto start;
        }
        else if(v!=0){
            for(int k=0;k<v;k++)ans.push_back(5);
            f-=v;
            i-=v;
            e-=v;
            v=0;
            if(f!=0){
                for(int k=0;k<f;k++)ans.push_back(4);
                o-=f;
                u-=f;
                r-=f;
                f=0; goto start;
            }
            else goto start;
        }
        else if((v==0)&&(f!=0)){
            for(int k=0;k<f;k++)ans.push_back(4);
            o-=f;
            u-=f;
            r-=f;
            f=0; goto start;
        }
        else if(o!=0){
            for(int k=0;k<o;k++)ans.push_back(1);
            n-=o;
            e-=o;
            o=0; goto start;
        }
        else if(t!=0){
            for(int k=0;k<t;k++)ans.push_back(3);
            h-=t;
            r-=t;
            e-=2*t;
            t=0; goto start;
        }
        else if(i!=0){
            for(int k=0;k<i;k++)ans.push_back(9);
            n-=2*i;
            e-=i;
            i=0; goto start;
        }
        else
        {
            sort(ans.begin(),ans.end());
            vector<int>::iterator it=ans.begin();
            for(;it!=ans.end();it++) fout<<*it;
            fout<<endl;
        }
    }
    return 0;
}