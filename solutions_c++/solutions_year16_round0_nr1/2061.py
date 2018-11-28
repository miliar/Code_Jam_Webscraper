#include <iostream>
#include <fstream>
using namespace std;

void cijfers(int n,bool resultaat[10]){
    while(n>0){
        resultaat[n%10]=true;
        n/=10;
    }
}


int main (){
    ifstream in("Al.in");
    ofstream out("aloutput.txt");
    int testcases;
    in >> testcases;
    int testcasses = testcases;
    while (testcasses -->0){
        long long int n;
        in>>n;
        if(n==0){
            out<<"Case #"<<testcases-testcasses<<": INSOMNIA"<<endl;
            continue;
        }
        long long int totaal=0;
        bool resultaat[10]={0};
        bool klaar=false;
        while(klaar==false){
            totaal+=n;
            cijfers(totaal,resultaat);
            klaar=true;
            for(int i=0;i<10;i++){
                if(resultaat[i]==false){
                    klaar=false;
                }
            }
        }
        out<<"Case #"<<testcases-testcasses<<": "<<totaal<<endl;
    }
    return 0;
}
