#include <bits/stdc++.h>
using namespace std;

//42

int main()
{

    ifstream in("input.txt");
    ofstream out("output.txt");
#define cin in
#define cout out



    int nbCas;
    cin>>nbCas;

    for(int c=1;c<=nbCas;c++) {
        int REPONSE = 42;
        cout<<"Case #"<<c<<": "<<endl;

        long long int N,J;
        cin>>N>>J;

        if(N <= 16) {


            vector<long long int> primes;

            vector<bool> isPrime(1e3,true);
            for(long long int c=2;c<isPrime.size();c++) {
                if(!isPrime[c]) continue;
                for(long long int c2=c;c2<isPrime.size();c2+=c) {
                    isPrime[c2]=false;
                }
                primes.push_back(c);
            }

            vector<long long > res;
            vector<vector<long long> > res2;

            for(long long int c=(1<<(N-1))+1;c<(1<<(N+1))&&res.size() < J;c+=2) {
                vector<long long> friendly;
                for(int c2=2;c2<=10;c2++){
                    vector<long long> remainders(primes.size(),0);
                    for(int c3=N;c3>=0;c3--){
                        long long act = (c & (1<<c3)) >> c3;
                        for(int c4=0;c4<remainders.size();c4++) {
                            remainders[c4]*=c2;
                            remainders[c4]+=act;
                            remainders[c4]%=primes[c4];
                        }
                    }
                    vector<long long>::iterator it = min_element(remainders.begin(),remainders.end());
                    if(*it > 0) {
                        goto nop;
                    }
                    friendly.push_back(primes[it-remainders.begin()]);
                }
                res.push_back(c);
                res2.push_back(friendly);
                nop:;
            }
            for(int c=0;c<res.size();c++){
                string s = "";
                long long tmp = res[c];
                while(tmp) {
                    s = s + (char)(tmp%2+'0');
                    tmp/=2;
                }
                reverse(s.begin(),s.end());
                cout<<s<<" ";
                for(int c2=0;c2<res2[c].size();c2++) cout<<res2[c][c2]<<" ";
                cout<<endl;
            }
        }

    }



}
