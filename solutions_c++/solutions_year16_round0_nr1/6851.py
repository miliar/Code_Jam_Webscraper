#include <fstream>
#include <vector>

using namespace std;

ifstream f("p1.in");
ofstream g("p1.out");

int t, i, j, sawAll, aux, found = 1;
long long n;
vector<int> seen;


void watchNumber(int n){
    while(n != 0){
        seen[n % 10] = 1;
        n = n / 10;
    }

    sawAll = 1;
    for(int i=0; i<10; i++){
        if(!seen[i]){
            sawAll  = 0;
        }
    }


}

int main(){
    f>>t;

    for(i=0; i<t;i++){
        f>>n;
        seen = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        sawAll = false;

        j = 0;
        found = 1;
        while(! sawAll){
            j++;
            aux = j * n;
            watchNumber(aux);
            if(j > 100){
                found = 0;
                break;
            }
        }
        if(found){
            g<<"Case #"<<i+1<<": "<<aux<<"\n";
        }
        else{
            g<<"Case #"<<i+1<<": INSOMNIA\n";
        }

    }
}
