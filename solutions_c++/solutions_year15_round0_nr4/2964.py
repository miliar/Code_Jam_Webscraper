// All includes 
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

#include <list>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>

#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <ctime>

#include <functional>
#include <numeric>
#include <iomanip>
#include <cstdio>

// All Macros
#define foreach(it,c) for(typeof((c).begin()) it=(c).begin(); it != (c).end() ; it++ )
#define F(i,mi,ma) for(int i=mi;i<ma;i++)

#define vi vector< int >
#define vs vector< string >
#define bn begin()
#define en end()
#define sz size()
#define pb push_back

#define mp make_pair
#define itr iterator

#define ld long double
#define ll long long

#define Fu(i,min,ma,inc) for(int i=min;i<ma;i+= inc)
#define Fd(i,ma,min,dec) for(int i=ma;i>=min;i-= dec)
#define vvi vector< vector< int > >
#define vvs vector < vs >
#define vd vector< double >
#define vvd vector< vd >
#define vb vector< bool >
#define vll vector< ll >

#define ERR 0.000000000001

using namespace std;

long long STL(string s){
     long long a=s[0]-'0';
     for(int i=1;i<s.size();i++)
             a=a*10+(s[i]-'0');
     return a;
} 
vector<int> SPint(string s,const string delim){
            vector<int> ans(0);
            string::size_type t=0,p=0;
            int N=0;
            while(true){
                   stringstream str;
                   p= s.find_first_of(delim,t);
                   if(p== string::npos  ){str<<s.substr(t);if(str.str()=="")break;str>>N;ans.pb(N);break;}
                   if(p!=t){str<< s.substr(t,p-t);str>>N;ans.pb(N);}
                   t=p+1;
            }
            return ans;
}
long long getn( vi pan )
{
     
                       int x,r,c;
                       x=pan[0];r=pan[1];c=pan[2];
                       if(x==1) return 0;
                       if(x==2){
                                if( r*c % 2 == 0 ) return 0;
                                return 1;
                       }
                       if(x==3){
                                if( r*c % 3 == 0 ){
                                    if(r*c >= 6) return 0;
                                    return 1;
                                }
                                return 1;
                       }
                       if(x==4){
                                if( r*c % 4 == 0){
                                    if( r*c >= 12 ) return 0;
                                    return 1;
                                }
                                return 1;
                       }
        return 2;               
}

int main()
{
   // ifstream in("a.in");
   // ofstream out("a.out");
    
    ifstream in("D-small-attempt1.in");
    ofstream out("D-small-attempt1.out");
    
    vs wr(3);
    //char[2][8] ch = { "GABRIEL", "RICHARD" };
    wr[0]= "GABRIEL";
    wr[1]= "RICHARD";
    wr[2] = "error";
    //while(in){
              string s;
              getline(in,s);
              int T = STL(s);
              F(i,0,T){
                       getline(in,s);
                       cout<<s<<endl;
                       vi pan = SPint(s," ");
                       
                       long long ans = getn(pan );
                       
                       cout<<" : "<<wr[ans]<<endl;
                       out<<"Case #"<<i+1<<": "<<wr[ans]<<endl;
              }
    //}
    out.close();
    in.close();
    getchar();
}
