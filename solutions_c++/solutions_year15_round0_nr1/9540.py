#include<iostream>
#include<fstream>
using namespace std;
int main(){
  ifstream INP("input1");
  ofstream OUT("output1");
  if(!INP || !OUT)
    cout<<"ERRORE nei FILE"<<endl;
  else
    {

            const int maxSmax = 1000;
            const int maxTest = 100;

            int T; //quanti test ci sono
            int smax[maxTest];
            int audiance[maxTest][maxSmax+1];

            int friends[maxTest]; //risultato da calcolare

            INP >> T;


            //popolo l'audiance e smax
            for (int i = 0; i<T; ++i){
                INP >> smax[i];
                INP.get();

                int c=INP.get() -'0';
                for (int j = 0; j<(smax[i]+1);j++){
                    audiance[i][j] = c;
                    c=INP.get() -'0';
                }
            }

            //calcolo num min di amici
            int people_clapping = 0;
            for (int i=0; i<T; i++){
                people_clapping = 0;
                friends[i]=0;
                for (int j=0;j<(smax[i]+1);j++){
                    if (j>people_clapping){
                        int nf = j - people_clapping;
                        friends[i] += nf;
                        people_clapping += nf;
                    }
                    people_clapping += audiance[i][j];
                }
            }

            for (int i=0;i<T;i++){
                OUT<<"Case #"<<i+1<<": "<<friends[i]<<endl;
            }

      INP.close();
      OUT.close();
    }
    return 0;
}
