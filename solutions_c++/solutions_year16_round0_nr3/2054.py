#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

vector<long> primes;

void fillPrimes(){
   primes.push_back(2);
   primes.push_back(3);
   primes.push_back(5);

   for (int i=7;i<100000;i+=2){
       bool prime=true;
       for (int j=0;j<primes.size();j++)
           if (i%primes[j]==0) {
               prime=false;
               break;
           }
       if (prime) primes.push_back(i);
   }
}
long getPrime(__int128_t t){
    for (int j=0;j<primes.size();j++)
        if (t%primes[j]==0&&t!=primes[j]) {
            return primes[j];
        }
    return 0;

}
__int128_t d[11];
int pr[11];
int main()
{
    fillPrimes();
    cout<<"Primes filled";
    ifstream f("input.txt");
    int t;
    f>>t;
    ofstream w("output.txt");

    for (int tests=1;tests<=t;tests++){
        w<<"Case #"<<tests<<":"<<endl;
        cout<<"tests";
        int n,jj;
        f>>n>>jj;
        long long st=1;
        for (int i=0;i<n-1;i++) st*=2;
        long long fs=st*2;
        for (long long i=st+1;i<fs;i+=2){
            long long cur=i;
            string s="";
            for (int k=0;k<=10;k++) d[k]=0;
            while (cur>0){
                s+='0'+(cur%2);
                for (int j=2;j<11;j++){
                    d[j]=d[j]*j+cur%2;
                }
                cur=cur/2;
            }
            bool st=1;
            for (int j=2;j<11;j++){
                pr[j]=getPrime(d[j]);
                if (pr[j]==0) {st=0; break;}
            }
            if (st){
                w<<s;
                for (int j=2;j<11;j++)w<<" "<<pr[j];
                w<<endl;
                jj--;
            }
            if (jj==0) break;


        }

    }
    w.close();
    return 0;
}

