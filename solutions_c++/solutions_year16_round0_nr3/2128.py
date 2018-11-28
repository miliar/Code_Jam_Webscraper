#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<sstream>
#include<set>
#include<vector>
#include<map>
#include<cassert>
#include<queue>
using namespace std;

int main(){
    
    int tc;
    cin>>tc;
    long long n,J;
    cin>>n>>J;
    int cont=0;
    cout<<"Case #1:"<<endl;
    
    n=n/2;
    for(int i=0;i<(1<<(n-2));i++){
        long long val=(1LL<<(n-1))+i*2+1;
        vector<long long>x;
        for(int j=2;j<=10;j++){
            long long aux=val;
            long long sum=0;
            long long base=1;
            for(int k=0;k<n;k++){
                sum+=(aux%2)*base;
                base*=j;
                aux/=2;
            }
            x.push_back(sum);
        }
        
        //8 numeros
        set<long long>S;
        vector<long long>dev;
        
        for(int j=0;j<x.size();j++){
            for(long long k=2;k*k<=x[j];k++){
                if(x[j]%k==0){
                    if(S.find(k)==S.end()){
                        S.insert(k);
                        dev.push_back(k);
                        break;
                    }
                    
                    if(S.find(x[j]/k)==S.end()){
                        S.insert(x[j]/k);
                        dev.push_back(x[j]/k);
                        break;
                    }

                }
            }
        }
        
        if(dev.size()==x.size()){
            cont++;
            string s="";
            long long auxval=val;
            for(int j=0;j<n;j++){
                char ch='0'+(auxval%2);
                s=ch+s;
                auxval/=2;
            }
            s=s+s;
            cout<<s;
            for(int j=0;j<dev.size();j++)
                cout<<" "<<dev[j];
            cout<<endl;
        }
        
        if(cont==J)break;
    }

   // cout<<cont<<endl;

    return 0;
}



