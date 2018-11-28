#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <ctime>

#include "lib/bigint/BigIntegerLibrary.hh"

#define ull unsigned long long

using namespace std;

vector<BigUnsigned> fas;

string curr = "";

//bool is_pal (BigUnsigned p){
//    stringstream ss;
//    ss<<p;
//    string k;
//    ss>>k;
//
//    return k == string(k.rbegin(),k.rend());
//
//}

bool is_pal (BigUnsigned p){
    BigUnsigned reverse = 0;
    BigUnsigned num = p;
    while( p != 0 )
    {
      reverse = reverse * 10;
      reverse = reverse + p%10;
      p = p/10;
    }

    return num==reverse;

}

void make_pal(int len){
    if(len==0){
        string final = curr;

        final+= string(curr.rbegin(),curr.rend()-1);

        BigUnsigned k = stringToBigUnsigned(final);
        k*=k;
        while(is_pal(k)){
            //if(find(fas.begin(),fas.end(),k)!=fas.end()||k==1) break;
            if(k==1) break;
            //cout<<k<<endl;
            fas.push_back(k);
            k*=k;
        }

        final = curr;
        final+= string(curr.rbegin(),curr.rend());


        k = stringToBigUnsigned(final);
        k*=k;
        while(is_pal(k)){
            //if(find(fas.begin(),fas.end(),k)!=fas.end()) break;
            //cout<<k<<endl;
            fas.push_back(k);
            k*=k;
        }

        return;
    }


    if(curr!=""){
        curr+="0";
        make_pal(len-1);
        curr = string(curr.begin(),curr.end()-1);
    }
    curr+="1";
    make_pal(len-1);
    curr = string(curr.begin(),curr.end()-1);
    curr+="2";
    make_pal(len-1);
    curr = string(curr.begin(),curr.end()-1);

}

int main ()
{
    freopen ("C.in","r",stdin);
    freopen ("C.out","w",stdout);

    //cout<<is_pal(1001)<<endl;
    fas.resize(0);
    fas.push_back(0); //remove?
    fas.push_back(1);
    fas.push_back(4);
    fas.push_back(9);


    for(int i =1;i<5;i++){
        make_pal(i);
    }

    sort(fas.begin(),fas.end());
    fas.erase( unique( fas.begin(), fas.end() ), fas.end() );

//    for(int i = 0;i<10;i++){
//        cout<<fas[i]<<endl;
//    }
    stringstream ss;
    ss<<fas[fas.size()-1];
    string garbage;
    ss>>garbage;

    //cout<<garbage.length()<<endl;

    int t; cin>>t;
    //cout<<fas.size()<<endl;
    for (int _t=0;_t<t;_t++){
        BigUnsigned f, s;
        string tmp;
        cin>>tmp;
        f = stringToBigUnsigned(tmp);
        cin>>tmp;
        s = stringToBigUnsigned(tmp);

        //cout<<f<<" "<<s<<" GEGE"<<endl;
        //cin>>f>>s;
        int ff,ss;
        for(int i = 0;i<fas.size();i++){
            if(f<=fas[i]){
                ff = i;
                break;
            }
        }
        for(int i = ff;i<fas.size();i++){
            if(s<fas[i]){
                ss = i;
                break;
            }
        }
        //cout<<ff<<" "<<ss<<endl;




        cout<<"Case #"<<_t+1<<": "<<ss-ff<<endl;



    }

    return 0;
}

