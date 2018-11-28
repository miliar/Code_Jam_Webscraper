#include<iostream>
#include<algorithm>
#include <cstdio>
#include<string>
#include<vector>
#include<cmath>
#include<cstdio>
using namespace std;



long stringToBase(string str, int base){
    long result = 0;
    for (int i=str.length()-1,j=0 ; i>=0 ; i--,j++){
        result += ((str[i]-'0')*pow(base,j));
    }
    return result;
}


void generateBinary(int curLength, string curStr, int& J){
    if (J == 0)return;
    if (curLength > 1){
        generateBinary(curLength-1,curStr+"0",J);
        generateBinary(curLength-1,curStr+"1",J);
    }
    if (curLength == 1){
        curStr+="1";
        long results[9];
        long divisors[9];
        long sq;
        bool isNumber = true;
        for (int k=2 ; k<=10 ; k++){
            results[k-2]=stringToBase(curStr,k);
            //cout<<"base "<<k<<": "<<results[k-2]<<endl;
            //getchar();
            sq = sqrt(results[k-2])+1;
            bool isPrime = true;
            for (int d=2 ; d<sq ; d++){
                if (results[k-2] % d == 0){
                    divisors[k-2] = d;
                    isPrime = false;
                    break;
                }
            }
            if (isPrime){
                isNumber = false;
            }
        }
        if (isNumber){
            cout<< curStr;
            /*
            for (int d=0;d<9;d++)
                cout<<" "<<results[d];
            cout<<endl;
            */
            for (int d=0;d<9;d++)
                cout<<" "<<divisors[d];
            cout<<endl;
            J--;
        }

    }
}


int main(){
    freopen("output.txt","w",stdout);
    int testcases,N,J;
    cin>>testcases;
    for (int i=0 ; i<testcases ; i++){
        cin>>N>>J;
        if(i)cout<<endl;

        cout<<"Case #"<<(i+1)<<":\n";
        generateBinary(N-1,"1",J);
    }
    return 0;
}
