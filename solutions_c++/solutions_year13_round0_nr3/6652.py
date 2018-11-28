#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool isPalindrome(int P);
bool isSquarePal(int S);

int main(){
    int T, min, max, i=0, j=0, count=0;
    ifstream fi;
    ofstream fo;
    
    fi.open("C-small-attempt0.in");
    fo.open("output.out");
    
    fi>>T;

    for(i=0;i<T;i++){
        count =0;
        fi>>min; fi>>max;
        for(j=min;j<=max;j++)
            if(isPalindrome(j) && isSquarePal(j)) count++;
        
        fo<<"Case #"<<i+1<<": "<<count<<endl;
        }
}

bool isPalindrome(int P){
        int x=P, sum=0;
        while(x){
            sum=sum*10+x%10;
            x/=10;
            }
        if(sum==P) return 1;
        else return 0;
        }
        
bool isSquarePal(int S){
     int i=0;
        for(i=1;i<=sqrt(S);i++){
            if((i*i==S) && isPalindrome(i)) return 1;
            }
        return 0;
        }
