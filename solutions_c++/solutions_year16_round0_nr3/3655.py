#include <iostream>
#include <fstream>
#include <vector>
using namespace std;


vector<int> htprimes(100000); // the 1st 100000 primes

void initprimes(vector<int> &v){
    ifstream prfin("htprimes.txt");
    for(int i=0;i<100000;++i) prfin>>v[i];
}


bool good(long long values[], int divisors[]){
    for(int j=2;j<=10;++j){
        divisors[j]=0;
        for(int i=0;!divisors[j] && i<100;++i)
            if(values[j]%htprimes[i]==0)
                divisors[j]=htprimes[i];
        if(!divisors[j]) return false;
    }
    return true;
}


void binout(int x,int i){
    if(i<16){
        binout(x>>1,i+1);
        cout<< (x&1);
    }
} 


int main(){
    initprimes(htprimes);
    
    int T,n,j; //cin>>T>>n>>j;
    n=16; j=50;    

    if(n==16){
        cout<<"Case #1:\n";

        int found=0;

        long long startnr = (1<<15) + 1;
        
        while(found<j){
            long long values[11];
            long long factors[11];            

            for(int i=2; i<=10; ++i){ values[i]=0; factors[i]=1; }
           
            
 
            int stcopy=startnr;
            for(int i=0;i<16;++i){
                if(stcopy&1)
                    for(int j=2;j<=10;++j) values[j]+=factors[j];
                
                for(long long j=2;j<=10;++j) factors[j]*=j;
                stcopy>>=1;
            }
                    
            //for(int i=2; i<=10; ++i){ cout<<values[i]<<'\n';}
            
            int divisors[11];  
            if( good(values,divisors) ){
                binout(startnr,0);
                for(int j=2;j<=10;++j) cout<<' '<<divisors[j];
                cout<<'\n';
                ++found;
            }
            startnr+=2;
        }        


    }    
    else cout<<"don't know...\n";
}
