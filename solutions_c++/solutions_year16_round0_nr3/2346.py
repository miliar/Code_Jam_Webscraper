#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>
#include <deque>
#include <math.h>

using namespace std;



long int div(long int number){
    long int d=0;
    if (number <= 2) return d;
    
    for(long int i=3; i<sqrt(number); i+=2)
    {
       if(number%i==0){
        d=i;
        break;
       }
          
    }  
    return d;
}
deque<long int> jam(long int p,long int M){
    deque<long int> q;
    q.push_back(1);
    for(long int i=0;i<M;i++){
        if(p%2==0)
            q.push_front(0);
        else
            q.push_front(1);
        p/=2;
    }
    q.push_front(1);
    return q;

}

long int divbase (deque<long int> q,long int b){
    long int n=q.size();
    long int num=0;
    for (long int i = 0; i < n; i++){
        num+=pow(b,n-1-i)*q.at(i);
        //cout<<q.at(i);
    }
    //cout<<" "<<num<<endl;
    long int d = div(num);
    return d;
}



 int main(){


long int T;
cin>>T;

for (long int i=0;i<T;i++){
    cout<<"Case #"<<i+1<<":"<<endl;
    long int N,J;
    cin>>N;
    cin>>J;
    long int nex=0;
    for(long int j=0;j<pow(2,N-2);j++){
        deque<long int> coin=jam(j,N-2);
        std::vector<long int> v;
        for (long int  m= 2; m <=10 ; m++)
        { 
            long int d=divbase(coin,m);
            if(d==0)
                break;
            else
                v.push_back(d);
        }
        if (v.size()==9){
            nex+=1;
            for (long int l=0;l<N;l++){
                cout<<coin.at(l);
            }
            cout<<" ";
            for (long int l=0;l<9;l++){
                cout<<v[l]<<" ";
            }
            cout<<endl;

        }
        if (nex==J)
            break;
    }

}

return 0;

}

