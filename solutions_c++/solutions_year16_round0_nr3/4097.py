#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>  
#include <vector>
#include <math.h>
#include <bitset>

using namespace std;

int main(){
    int N; //length of jamicoin
    int numberSearching; //number of jamicoins I must find
    int numberFound=0;

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> N ;
        cin >> numberSearching;
    }


    // the magical coin
    int coin[N];
    coin[0]=1;
    coin[N-1]=1;

    for(int m=1; m<N-1; m++){
        coin[m]=0;
    }

    cout<<"Case #"<<numberFound+1<<":"<<endl;


    int limit= (int) pow(2, N-2);
    int counter=0;

    while(numberFound<numberSearching && counter<limit){
        //cout<<"Well I got here"<<endl;
    
        int j=2;
        int divisors[9]={0,0,0,0,0,0,0,0,0};
        int summing[9]={0,0,0,0,0,0,0,0,0};
        bool jamicoin=true;
        
        
    while(jamicoin && j<=10){
            unsigned long long totalSum=1;
            for(int i=2; i<=N; i++){
                unsigned long long temp = (unsigned long long) coin[N-i]*pow((double) j, (double) i-1);
                totalSum=totalSum+temp;
            }
            unsigned long long square=(unsigned long long)sqrt(totalSum);
           // cout<<"J is: "<<j<<" sqrare root of: "<<totalSum<< " is: "<<square;
            unsigned long long k=2;
            unsigned long long sum=(unsigned long long) totalSum;
            bool searching=true;
	
                while(searching && k<=square){
                    if(sum%k==0){
                        divisors[j-2]=k;
                       // cout<<" The divisor is: "<<k;
                         summing[j-2]=sum;
                        searching=false;
                    }
                    k++;
                }
    
            if(searching){
                for (int r=0; r<9; r++) {
                    divisors[j]=0;
                    summing[j]=0;
                }
                jamicoin=false;
            }

           // cout<<endl;
        j++;
        }
        

        
        if (jamicoin) {
            //for(int a=0;a<9; a++){
              //  cout<<summing[a]<<", ";
            //}
            //cout<<endl;
    
            for(int i=0;i<N;i++){
                cout<<coin[i];
            }
            cout<<" ";
            for(int i=0; i<9; i++){
                cout<<divisors[i]<<" ";
            }
            cout<<""<<endl;
            numberFound++;
        }


        //increment coin
       if(coin[N-2]==0){
            coin[N-2]=1;
        }
       else{
            int counterP=1;
            bool untilFound=true;
            while(untilFound && counterP<=N-2){
                if(coin[N-2-counterP]==0){
                    coin[N-2-counterP]=1;
                    for(int p=counterP-1; p>0; p--){
                        coin[N-2-p]=0;
                    }
                    untilFound=false;
                }
                counterP++;
            }
        }


      //  cout<<counter<<endl;
    counter++;
       // cout<<numberFound<<endl;
    }
}
