#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef map<int, int> mii;
#define MAX 10000000

ll _sieve_size;
bitset<10000010> bs;
vi primes;
int T=1,N=32,J=500;
string jamcoin[501];
int total=0;
int arr[12];

void sieve(ll upperbound) {
  _sieve_size = upperbound + 1;
  bs.set();
  bs[0] = bs[1] = 0;
  for (ll i = 2; i <= _sieve_size; i++) if (bs[i]) {
    for (ll j = i * i; j <= _sieve_size; j += i) bs[j] = 0;
    primes.push_back((int)i);
  }
}

bool isPrime(ll N) {
  if (N <= _sieve_size) return bs[N];
  for (int i = 0; i < (int)primes.size(); i++)
    if (N % primes[i] == 0) return false;
  return true;
}


string convert(ll number ){
    string str="";

    while(number!=0){
        if(number%2 ==0 )str+='0';
        else str+='1';
        number/=2;
    }
    reverse(str.begin(), str.end() );
    return str;
}


int power(const int& base,const int& divisor,const int& po){
    int answer=1;
    for(int i=0;i<po;i++){
        answer*=( base);
        answer%=divisor;
    }
    return answer;
}


int div(string& str,const int& base){
    int var,fin=0;
    for(int i=0;i<168;i++){
        fin=0;
        for(int j=0;j<32;j++){
            if(str[32-1-j]=='1'){
                fin+=power(base,primes[i],j);
                fin%=primes[i];
            }
        }
        if( fin==0) return primes[i];
    }
    return -1;
}

void print(){

    cout<<jamcoin[total];
    for(int i=2;i<=10;i++)
        cout<<" "<<arr[i];
    cout<<endl;
}


int main(){
    sieve(MAX);

    freopen("outhput.out","w",stdout);
    string curr;

    cout<<"Case #1:"<<endl;
    for(unsigned int i=2147483648;i<4294967295;i++){
        if(total==J) break;
        int ans;
        bool know;

        curr=convert(i);
        if( curr[31]=='0' || curr[0]=='0') continue;
        jamcoin[total]=curr;
        for(int i=2;i<=10;i++){
            know=false;
            ans=div(curr,i);
            if(ans==-1){
                know=true;
                break;
            }
            arr[i]=ans;
        }
        if(know) continue;
        print();
        total++;
    }
    return 0;
}
