#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int count(long long x, vector<int> &v){
    if(x==0){
        if(!v[0]){
            v[0]=1;
            return 1;
        }
        else return 0;
    }
    else{
        int nr=0;
        while(x!=0){
            int dig=x%10;
            x/=10;
            if(!v[dig]){
                v[dig]=1; 
                ++nr;
            }
        }
        return nr;
    }
}


int main(){
    int t; fin>>t;
    for(int tc=1;tc<=t;++tc){
        int n; fin>>n;
        
        vector<int> v(10,0);
        int seen=0;
     
        long long it;

        for(it=1; it<=10000 && seen<10; ++it){
            seen += count(it*n,v);
        }
 
        --it;
        if(seen==10)
           fout<<"Case #"<<tc<<": "<< it*n <<'\n';
        else
           fout<<"Case #"<<tc<<": INSOMNIA\n";

    }
}
/*
    int mx=0;
    vector<int> wh;        
    
    for(long long n=0;n<=100000000;++n){         
        vector<int> v(10,0);
        int seen=0;
     
        long long it;

        for(it=1; it<=10000 && seen<10; ++it){
            seen += count(it*n,v);
        }

        
        --it;
        if(seen==10)
           // cout<<setw(6)<<n<<":  after it: "<<setw(4)<<it<<"    number: "<<it*n<<'\n';
           {
            if(it>mx){mx=it; wh.clear(); wh.push_back(n);}
            else if(it==mx) wh.push_back(n);
        } 
        else
            cout<<n<<": not seen it yet...\n";
    }

    cout<<"max it: "<<mx<<" for: ";
    for(int i : wh) cout<<i<<" ";
    cout<<'\n';
}*/
