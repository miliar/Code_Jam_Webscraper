#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<sstream>
#define REP(i,n) for(int i=0;i<n;++i)
#define FOR(i,j,k) for(int i=j;i<k;++i)
#define REPD(i,n) for(int i=n;i>-1;--i)
#define ALL(v) v.begin(),v.end()
#define ll long long
#define PB push_back
using namespace std;

bool Row(int wsk,vector<vector<int> > d){
       vector<int> tmp = d[wsk];
       int last = -1 ;
       REP(i,tmp.size())
       {
         if(tmp[i]!=-1){
                            if(last == -1) last = tmp[i];
                            else if(tmp[i]!=last) return false;
                        }
       }
       return true;
     }
     
bool Column(int wsk,vector<vector<int> > d){
       vector<int> tmp;
       REP(j,d.size()) tmp.PB(d[j][wsk]);
       int last = -1 ;
       REP(i,tmp.size())
       {
         if(tmp[i]!=-1){
                            if(last == -1) last = tmp[i];
                            else if(tmp[i]!=last) return false;
                        }
       }
       return true;
     }

int main()
{
    int ts;cin>>ts;
    REP(tn,ts)
    {
        string ret = "NO";
        int n,m; cin>>n>>m;
        vector<vector<int> > d(n);
        REP(i,n){
                 d[i].resize(m);
                 REP(j,m) cin>>d[i][j];
                 }
                 
                //  cout<<"----"<<endl;
                //     REP(i,d.size()) {REP(j,d[i].size()) cout<<d[i][j]<<" ";cout<<endl;}
                //     cout<<"----"<<endl;
                     
        bool hasSolution = true;
        while(true){
                    int mv = 101;
                    REP(i,d.size()) REP(j,d[i].size()) if(d[i][j]>0&&d[i][j]<mv) mv = d[i][j];
                    bool hasChange = false;
                    
                    REP(i,d.size())
                     REP(j,d[i].size())
                     {
                        if(d[i][j]==mv)
                        {
                            if(Row(i,d))
                            {
                               hasChange = true;
                               REP(k,d[i].size()) d[i][k]=-1;
                            //   i = j = 110;
                            }
                            else  if( Column(j,d))
                               {
                                   hasChange = true;
                                   REP(k,d.size()) d[k][j] = -1; 
                                //   i = j = 110;
                               }
                        }
                     }
                     
                  //   cout<<"----"<<endl;
                  //  REP(i,d.size()) {REP(j,d[i].size()) cout<<d[i][j]<<" ";cout<<endl;}
                  //   cout<<"----"<<endl;
                      
                     if(mv==101) break;
                    
                      if(!hasChange){
                                       hasSolution = false;
                                       break;
                                     }
                    }
                    
        if(hasSolution) ret = "YES";
        cout<<"Case #"<<(tn+1)<<": "<<ret<<endl;
    }
}
