#include <cstdlib>
#include <iostream>
#include <fstream>
#include <set>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream cin("B-small-attempt0.in");
    //ifstream cin("entrada.txt");
    ofstream cout("Redownload B-small-attempt0.txt");

    long long int case_=0,A,B,K,n,cont;
    cin>>case_;
    //cout<<(7&11)<<endl;
    for(int k=1;k<=case_;k++){

            cin>>A>>B>>K;
            cont=0;
            for (int i=0;i<A;i++){
                for(int j=0;j<B;j++){
                    n=i&j;
                    if(n<K){
                       //cout<<"---- "<<n<<" "<<i<<" & "<<j<<endl;
                        cont++;
                    }else{
                        //cout<<"++ "<<n<<" "<<i<<" & "<<j<<endl;
                    }
                }
            }
           cout<<"Case #"<<k<<": "<<cont<<endl;
          }


    return 0;
}
