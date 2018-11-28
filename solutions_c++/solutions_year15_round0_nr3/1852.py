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

#define H1 1
#define Hi 2
#define Hj 3
#define Hk 4

int pole[4][4]={{H1,Hi,Hj,Hk},{Hi,-H1,Hk,-Hj},{Hj,-Hk,-H1,Hi},{Hk,Hj,-Hi,-H1}};


int main(){
	ios::sync_with_stdio(false);
        

        map<int,int>M;
        M['1']=1;
        M['i']=2;
        M['j']=3;
        M['k']=4;

        int t;
        cin>>t;
        for(int tt=1; tt<=t; tt++){
            int p,k;
            cin>>p>>k;
            string ss,s;
            cin>>ss;
            for(int i=0; i<k; i++)
                s+=ss;

            //cout<<s<<endl;
            int zac=M[s[0]];
            int pos=1;
            int hi=0,hj=0,hk=0;

            while(zac!=Hi && pos<s.length()){
            //cout<<zac<<endl;
                int znam = zac/abs(zac);
                zac=pole[abs(zac)-1][M[s[pos]]-1]*znam;
                pos++;
            }
            if(zac==Hi)
                hi=1;

            if(pos<s.length()){
            //cout<<"hi "<<hi<<" pos "<<pos<<endl;
            pos+=1;
            zac=M[s[pos-1]];
            //cout<<zac<<en;
            while(zac!=Hj && pos<s.length()){
                int znam = zac/abs(zac);
                zac=pole[abs(zac)-1][M[s[pos]]-1]*znam;
                pos++;
            }
            if(zac==Hj)
                hj=1;
            }
            //cout<<"hj "<<hj<<" pos "<<pos<<endl;
            if(pos<s.length()){
            pos+=1;
            zac=M[s[pos-1]];
            while(pos<s.length()){
                int znam = zac/abs(zac);
                zac=pole[abs(zac)-1][M[s[pos]]-1]*znam;
                pos++;
            }
            if(zac==Hk)
                hk=1;
 
            }
            //cout<<"hk "<<hk<<" pos "<<pos<<endl;
            cout<<"Case #"<<tt<<": ";
            if(hi && hj && hk){
                cout<<"YES"<<en;
            }
            else cout<<"NO"<<en;

        }
        




}
