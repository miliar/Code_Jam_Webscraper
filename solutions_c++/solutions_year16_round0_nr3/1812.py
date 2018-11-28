#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<vector>
#include<string>
#include<set>

using namespace std;


unsigned int convert2base(unsigned n,int b,int len){
    if (b==2) return n;
    unsigned r=0;
    for(int i=len;i>0;i--){
        r*=b;
        if (n&(1<<(i-1))){
            r+=1;
        }
    }
    return r;
}
int bigMod(int b,int p,int mod){
    if (p==0) return 1;
    int r=bigMod(b,p/2,mod);
    r=(r*r)%mod;
    if (p%2==1)
        r=(r*b)%mod;
    return r;
}
bool isDivisible(unsigned int n,int len,int b,int prime){

    int r=0;
    for(int i=len-1;i>=0;i--){
        if (n&(1<<i))
            r=(r+bigMod(b,i,prime))%prime;
    }
    return r==0;
}

int getDivisor4base(unsigned int n,int len,int b){
    int primes[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
    for(int i=0;i<25;i++){
        int prime=primes[i];
        if (isDivisible(n,len,b,prime))
            return prime;
    }
    return -1;
}
vector<int> getDivisorList(unsigned int n,int len){
    vector<int> divList,empty;
    for(int b=2;b<11;b++){
        int d=getDivisor4base(n,len,b);
        if (d==-1) return empty;
        divList.push_back(d);
    }
    return divList;
}
unsigned int getNdigitsJamCoin(int N){
    unsigned int maxV=1<<(N-2);

    unsigned int r=((rand()%maxV)<<1)|1;
    unsigned one=1;
    r|=(one<<(N-1));

    return r;
}

void show(vector<int> v){
    for(int i=0;i<v.size();i++)
        cout<<" "<<v[i];
    cout<<endl;
}
string getBinString(int n,int len){
    string s="";
    for(int i=len-1;i>=0;i--){
        if(n&(1<<i))
            s+="1";
        else s+="0";
    }
    return s;
}
void fun(int N,int J){

    //for(int i=2;i<11;i++)
     //   cout<<convert2base(39,i,6)<<endl;
    cout<<"Case #1:"<<endl;
    set<unsigned int> coinJamSet;
    srand (time(NULL));
    unsigned int cj;
    while(J>0){
        cj=getNdigitsJamCoin(N);
        if (coinJamSet.find(cj)!=coinJamSet.end())
            continue;
        coinJamSet.insert(cj);
       vector<int> divList=getDivisorList(cj,N);
       if (divList.size()>0){
            J--;
            //cout<<cj<<endl;
            cout<<getBinString(cj,N);
            show(divList);
       }
    }

}
int main(){
    //freopen("in.txt","r",stdin);
    freopen("out32.txt","w",stdout);

    fun(32,500);

    int N,T,J;
    return 0;
    cin>>T;
    for(int i=1;i<=T;i++){
        cin>>N>>J;

    }
    return 0;
}