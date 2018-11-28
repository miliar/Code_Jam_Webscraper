//
//  main.cpp
//  codejam_1
//
//  Created by Hasan Unlu on 11/04/15.
//  Copyright (c) 2015 Hasan Unlu. All rights reserved.
//
#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <algorithm>

#define rep(i,n) for(ll i = 0; i < (n); i++)

using namespace std;

typedef uint64_t ull;

typedef int64_t   ll;


//uint64_t or int64_t
//strtoll  or strtoull

uint64_t rev(uint64_t x){
    uint64_t tmp=0;
    while(x>0){
        tmp=tmp*10;
        tmp=tmp+x%10;
        x=x/10;
    }
    return tmp;
}

int main(int argc, const char * argv[]) {
    
    string line;
    
    ifstream infile ("/Users/hasanunlu/Desktop/codejam_1/codejam_1/input.txt");
    ofstream outfile ("/Users/hasanunlu/Desktop/codejam_1/codejam_1/output.txt");
    
    if (!infile.is_open())
        cout << "Unable to open file";
    
    uint64_t T;
    
    getline(infile, line);
    
    T=strtoull(line.c_str(), NULL, 10);
    
    cout <<"T="<< T << endl;
    cout<<"*********"<<endl;
    
    for(ull i=0; i<T; i++){
        
        ull C,D,V;
        
        getline (infile, line);
        char *input = const_cast<char*>(line.c_str());
        
        C=strtoull(input, &input, 10);
        D=strtoull(input, &input, 10);
        V=strtoull(input, NULL, 10);
        
        cout <<"C="<<C<<" D="<<D<<" V="<<V<<endl;
        
        ull *den=new ull[D];
        
        ull *exist=new ull[V+1];
        ull *exist_tmp=new ull[V+1];
        
        
        getline (infile, line);
        input = const_cast<char*>(line.c_str());

        
        for(ull j=0; j<D; j++)
            den[j]=strtoull(input, &input, 10);
        
        for(ull j=0; j<D; j++)
            cout<<den[j]<<" ";
        
        cout<<endl;
    
        for(ull j=0; j<(V+1); j++)
            exist[j]=0;
    
        int ii[5]={0};
        ull sum=0;
        
        
        if(D>=1){
            for(ii[0]=0; ii[0]<D; ii[0]++)
                if(den[ii[0]]<=V)
                    exist[den[ii[0]]]++;
        }
        
        if(D>=2){
            for(ii[0]=0; ii[0]<D; ii[0]++)
                for(ii[1]=ii[0]+1; ii[1]<D; ii[1]++){
                    sum=den[ii[0]]+den[ii[1]];
                    if(sum<=V)
                        exist[sum]++;
                }
        }
        
        if(D>=3){
            for(ii[0]=0; ii[0]<D; ii[0]++)
                for(ii[1]=ii[0]+1; ii[1]<D; ii[1]++)
                    for(ii[2]=ii[1]+1; ii[2]<D; ii[2]++){
                        sum=den[ii[0]]+den[ii[1]]+den[ii[2]];
                        if(sum<=V)
                            exist[sum]++;
                }
        }
        
        if(D>=4){
            for(ii[0]=0; ii[0]<D; ii[0]++)
                for(ii[1]=ii[0]+1; ii[1]<D; ii[1]++)
                    for(ii[2]=ii[1]+1; ii[2]<D; ii[2]++)
                        for(ii[3]=ii[2]+1; ii[3]<D; ii[3]++){

                            sum=den[ii[0]]+den[ii[1]]+den[ii[2]]+den[ii[3]];
                            if(sum<=V)
                                exist[sum]++;
                    }
        }

        if(D>=5){
            sum=0;
            for(ii[0]=0; ii[0]<D; ii[0]++)
                sum+=den[ii[0]];
            
            if(sum<=V)
                exist[sum]++;
        }

        for(ull j=0; j<V; j++)
            cout<<exist[j+1]<<" ";
        cout<<endl;
        
        ull result=0;
        
        for(ull j=1; j<=V; j++){
            if(exist[j]==0){
                result++;
                cout<<"Err "<<j<<endl;
                

                for(ull k=0; k<(V+1); k++)
                    exist_tmp[k]=0;
                
                for(ull k=1; k<=(V-j); k++)
                    
                    if(exist[k]>=1){
                        exist_tmp[k+j]=1;
                    }

                for(ull k=0; k<(V+1); k++)
                    if(exist_tmp[k]>=1){
                        exist[k]=exist_tmp[k];
                    }
                
                exist[j]=1;
                
            }
            
            for(ull k=1; k<=V; k++)
                cout<<exist[k]<<" ";
            cout<<endl;
            
        }
        
        for(ull j=0; j<V; j++)
            cout<<exist[j+1]<<" ";
        cout<<endl;
        
        cout<<"Case #"<<i+1<<": "<<result<<endl;
        outfile<<"Case #"<<i+1<<": "<<result<<endl;
        cout<<"\n*******************************************"<<endl;
        
        delete [] den;
        delete [] exist;
        
    }
    
    infile.close();
    outfile.close();
    
    return 0;
}
