#include <iostream>
#include <cstdio>
using namespace std;

int max_level = 0;
int aplaudiendo;
int genteAd;

void analize(int c);
void UpdateAplaudiendo(int v,string people, int Smax);

int main() {
    freopen("A-large.in","r",stdin);
    freopen("output.out","w+",stdout);

    int T; cin>>T;
    for (int c = 1;c <= T;c++){
        analize(c);
    }
}


void analize(int c){
    cout<<"Case #"<<c<<": ";

    int Smax; cin>>Smax;
    string people; cin>>people;

    aplaudiendo = -1;
    genteAd = 0;

    UpdateAplaudiendo(0, people , Smax); //agrego la gente del nivel 0
    while (1){
        if (aplaudiendo >= Smax){ //si todos aplauden
            break;
        }
        UpdateAplaudiendo(aplaudiendo+1, people , Smax);
        genteAd ++;
    }

    cout<<genteAd<<endl;

}
void UpdateAplaudiendo(int v,string people, int Smax){
    //cout<<"iniciando con v="<<v<<endl;

    if (v == aplaudiendo){ return; } //no logramos que todos aplaudan
    if (aplaudiendo >= Smax){ return; } //si ya todos aplauden

    int initial = aplaudiendo;

    aplaudiendo = v;

    int nuevos = 0;


    for (int x = initial+1;x <= aplaudiendo;x++) { //por toda la gente con nivel de verguenza del anterior al actual
        nuevos += (people[x] - '0');
    }

    UpdateAplaudiendo(aplaudiendo + nuevos , people, Smax);
}