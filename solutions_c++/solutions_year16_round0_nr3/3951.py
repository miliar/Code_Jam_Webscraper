//coin jam

#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>

using namespace std;

long long notPrime(long long N){
    long long p  = sqrt(N);
    for(long long i=2;i<=p;i++){
        if(N%i == 0) return i;
    }
    return -1;
}

inline long long numberInBase(long long n,int base){
    long long ret = 0;
    int j =0;
    while(n){
        if(n%2==1){
           ret +=  pow(base,j);
        }
        n = n/2;
        j+=1;
    }

    return  ret;
}

inline string numberInBinary(long long n){

    string ret = "";
    while(n){
        if(n%2==0) ret  = '0'+ ret;
        else ret = '1'+ret;

        n = n/2;

    }
    return ret;
}

int main(){
    int T,N,J;

  //  freopen("C-small-attempt0.in","r",stdin);
   // freopen("a.out","w",stdout);

    cin>>T;

    cin>>N>>J;

    long long l,s,k,number,numC,c;


    s = pow(2,N-1)+1;

    l = pow(2,N-2)-1;
    cout<<"Case #"<<T<<": "<<endl;
    k = 0;
    for(int j=0;j<=l && k<J;j++)
    {
        long long numList[11];

        number = s + j*2;

        numC = notPrime(number);
        c = 3;
        if(numC==-1) continue;
        else{
          //  cout << number<<" "<<numC<<endl;
            numList[2] = numC;
            for(c = 3;c<=10;c++){

                numC = numberInBase(number,c);
            //    cout<<numC<<" ";
                numC = notPrime(numC);
             //   cout<<numC<<endl;
                if(numC == -1) break;
                else numList[c] = numC;

            }

            if(c==11) {
                    k++;
                    cout<<numberInBinary(number)<<" ";
                    for(int m = 2;m<=10;m++) cout<<numList[m]<<" ";
                    cout<<endl;
            }
        }
        }







    return 0;
}
