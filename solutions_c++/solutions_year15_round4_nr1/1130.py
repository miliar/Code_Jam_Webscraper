/*
 * This is my code,
 * my code is amazing...
 */
//Template v2.0
//iostream is too mainstream
#include<iostream>
#include<string>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<unordered_map>
#include<unordered_set>
#include<vector>
#include<iomanip>
//clibraries
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<ctime>
//defines
#define ll long long
#define lld long double
#define pll pair<ll,ll>
#define pld pair<lld,lld>
#define vll vector<ll>
#define vvll vector<vll>
#define INF 1000000000000000047
const char en='\n';
#define debug(x){cerr<<x<<en;}
#define prime 47
#define lprime 1000000000000000009
#define lldmin LDBL_MIN
#define MP make_pair
#define PB push_back
using namespace std;



int main(){
	ios::sync_with_stdio(false);


            vector<pll> M(1000);
            M['^']=MP(-1,0);
            M['v']=MP(1,0);
            M['<']=MP(0,-1);
            M['>']=MP(0,1);

            int T;
            cin>>T;
            for(int t=1; t<=T; t++){
                
                int r,c;
                cin>>r>>c;
                vvll V(r+47,vll(c+47,'.'));
                vll R(r+47,0),C(c+47,0);

                for(int i=1; i<=r; i++)
                    for(int j=1; j<=c; j++){
                        char cc;
                        cin>>cc;
                        V[i][j]=cc;
                        R[i]+=(V[i][j]!='.');
                        C[j]+=(V[i][j]!='.');
                    }

                

                int pocet=0;
                int err=0;
                for(int i=1; i<=r; i++)
                    for(int j=1; j<=c; j++){
                        if(V[i][j]!='.'){
                        if(R[i]==1 && C[j]==1)err=1;
                            pll smer = M[V[i][j]];
                            int x=i,y=j;
                            x+=smer.first;
                            y+=smer.second;
                            //cout<<x<<" "<<y<<" "<<smer.first<<" "<<smer.second<<en;
                            while(true){
                                if(x>r || y>c || x<1 || y<1){/*cout<<"pripocitavam"<<endl;*/pocet++; break;}
                                if(V[x][y]!='.')break;
                                x+=smer.first;
                                y+=smer.second;
                            }
                        }
                    }


                cout<<"Case #"<<t<<": ";
                if(err)
                    cout<<"IMPOSSIBLE"<<en;
                else cout<<pocet<<en;





            }





}
