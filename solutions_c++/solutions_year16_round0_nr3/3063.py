#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <string>
#include <list>
#include <queue>
#include <cassert>
#include <stack>
#include <fstream>
#include <cstring>

using namespace std;

#define pb push_back;
typedef long long ll;
typedef unsigned long long ull;
#define VI vector<int>;
#define loop(i,n) for(int i=0;i<n;i++);

unsigned long long get_num(std::vector<int> v,int base){
    int n=v.size();
    unsigned long long num=0;
    for(int i=0;i<n;i++){
        if(v[i]==1)
            num+=pow(base,n-1-i);
    }
    return num;
}

int prime_set[] ={
     2,     3,      5,     7,    11,     13,   17,    19,    23,    29, 
     31,     37,     41,     43,     47,     53,     59,     61,     67,     71, 
     73,     79,     83,     89,     97,    101,    103,    107,    109,    113, 
    127,    131,    137,    139,    149,    151,    157,    163,    167,    173, 
    179,    181,    191,    193,    197,    199,    211,    223,    227,    229, 
    233,    239,    241,    251,    257,    263,    269,    271,    277,    281, 
    283,    293,    307,    311,    313,    317,    331,    337,    347,    349, 
    353,    359,    367,    373,    379,    383,    389,    397,    401,    409, 
    419,    421,    431,    433,    439,    443,    449,    457,    461,    463, 
    467,    479,    487,    491,    499,    503,    509,    521,    523,    541, 
    547,    557,    563,    569,    571,    577,    587,    593,    599,    601, 
    607,    613,    617,    619,    631,    641,    643,    647,    653,    659, 
    661,    673,    677,    683,    691,    701,    709,    719,    727,    733, 
    739,    743,    751,    757,    761,    769,    773,    787,    797,    809, 
    811,    821,    823,    827,    829,    839,    853,    857,    859,    863, 
    877,    881,    883,    887,    907,    911,    919,    929,    937,    941, 
    947,    953,    967,    971,    977,    983,    991,    997,   1009   };

int is_prime(ull num){
    int sqt=sqrt(num);
    int n=sizeof(prime_set)/sizeof(int);
    for(int i=0;i<n && prime_set[i]<=sqt;i++){
        if(num%prime_set[i]==0)
            return prime_set[i];
    }
    for(int temp=1009;temp<=sqt;temp+=2){
        if(num%temp==0)
            return temp;
    }
    return -1;
}

int main(){
    int t,case_num=1,count=0,d,flag=1,r;  
    ifstream input;
    input.open("input.txt");
    ofstream outfile;
    outfile.open("output.txt");
    input>>t;
    while(t--){
        unsigned long long num,temp;
        std::vector<std::vector<int> > ans,sol;
        int n,j,counter=0;
        input>>n>>j;
        std::vector<int> bool_num(n,0);
        bool_num[0]=bool_num[n-1]=1;
        int k=pow(2,n-2);
        for(int i=0;i<k;i++){
            std::vector<int> v(9);
            for(int d = 0; d < n-2; d++){
                bool_num[n-2-d]=0;
                if(i & (1<<d))
                    bool_num[n-2-d]=1;
            }
            for(int d=0;d<n;d++)
                cout<<bool_num[d];
            cout<<endl;
            for(int base=2;base<=10;base++){
                num=get_num(bool_num,base);
                r=is_prime(num);
                cout<<"num="<<num<<" r="<<r<<endl;
                if(r==-1){
                    break;
                }
                v[base-2]=r;
            }
            if(r!=-1){
                for(int pre=0;pre<9;pre++){
                    cout<<v[pre]<<" ";
                }
                cout<<endl;
                ans.push_back(v);
                sol.push_back(bool_num);
                counter++;
                if(j==counter) break;
            }
        }
        outfile<<"Case #"<<case_num<<":"<<endl;
        for(int i=0;i<j;i++){
              for(int tring=0;tring<n;tring++)
                  outfile<<sol[i][tring];
              outfile<<" ";
              for(int tring=0;tring<9;tring++)
                  outfile<<ans[i][tring]<<" ";
              outfile<<endl;
        }     
    }
    return 0;
}
