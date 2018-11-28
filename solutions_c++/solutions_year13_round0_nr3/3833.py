#include<iostream>
#include<stdio.h>
#include<sstream>
#include<string.h>
#include<cstdlib>
using namespace std;
bool testpalin(string snum);

int main(){
    int T;
    cin>>T;
    
    int itr;
    for( itr=0;itr<T;itr++){
        bool flag1 = true;
        long long int s1;
        long long int s2;
        long long count = 0;
        cin>>s1;
        cin>>s2;

        long long int num =1;
        while(num*num < s1){
            num++;
        }
        while(num*num <= s2){
            stringstream ss1;
            ss1 << num;
            string snum1 = ss1.str();
            bool ret1 = testpalin(snum1);
            if( ret1 == true){                         
                stringstream ss;
                ss << num*num;
                string snum = ss.str();
                bool ret = testpalin(snum);
                if(ret == true){
                    count++;
                }
             } 
             num++;        
        }
        cout<<"Case #"<<itr+1<<": "<<count<<endl;
    }    
    return 0;
    
}

bool testpalin(string snum){
        bool flag1 = true;
        int size = snum.size();
        for(int i=0;i<snum.size()/2;i++){
            if(snum[i] != snum[size-i-1]){
                flag1 = false;
            }
        }
    return flag1;
}    
