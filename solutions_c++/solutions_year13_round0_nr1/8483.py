#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

char funkcija(char jedan, char dva, char tri, char cetiri){
    char pomoc='A', nije='A';
    if(jedan!='T' && jedan!='.')
        pomoc=jedan;
    else if(dva!='T' && dva!='.')
        pomoc=dva;
    else if(tri!='T' && tri!='.')
        pomoc=tri;
    else if(cetiri!='T' && cetiri!='.')
        pomoc=cetiri;

    if((jedan==pomoc || jedan=='T') && (dva==pomoc || dva=='T') && (tri==pomoc || tri=='T') && (cetiri==pomoc || cetiri=='T')){
        return pomoc;
    }
    else return nije;
}


int main(){
    ofstream file;
    file.open ("example.txt");
    vector<vector<char> > polje;
    vector<char> vi(4);
    polje.insert(polje.begin(),4,vi);

    int n;
    cin>>n;
    for(int b=1;b<=n;++b){
    bool negotov=0,pobjednik=0;
    for(int i=0;i<4;++i){
        for(int j=0;j<4;++j){
            cin>>polje[i][j];
            if(polje[i][j]=='.')
                negotov=1;
        }
    }
    if(funkcija(polje[0][0],polje[0][1],polje[0][2],polje[0][3])!='A'){
        file<<"Case #"<<b<<": "<<funkcija(polje[0][0],polje[0][1],polje[0][2],polje[0][3])<<" won"<<endl;
        pobjednik=1;
    }
    else if(funkcija(polje[1][0],polje[1][1],polje[1][2],polje[1][3])!='A'){
        file<<"Case #"<<b<<": "<<funkcija(polje[1][0],polje[1][1],polje[1][2],polje[1][3])<<" won"<<endl;
        pobjednik=1;
    }
    else if(funkcija(polje[2][0],polje[2][1],polje[2][2],polje[2][3])!='A'){
        file<<"Case #"<<b<<": "<<funkcija(polje[2][0],polje[2][1],polje[2][2],polje[2][3])<<" won"<<endl;
        pobjednik=1;
    }
    else if(funkcija(polje[3][0],polje[3][1],polje[3][2],polje[3][3])!='A'){
        file<<"Case #"<<b<<": "<<funkcija(polje[3][0],polje[3][1],polje[3][2],polje[3][3])<<" won"<<endl;
        pobjednik=1;
    }
    else if(funkcija(polje[0][0],polje[1][0],polje[2][0],polje[3][0])!='A'){
        file<<"Case #"<<b<<": "<<funkcija(polje[0][0],polje[1][0],polje[2][0],polje[3][0])<<" won"<<endl;
        pobjednik=1;
    }
    else if(funkcija(polje[0][1],polje[1][1],polje[2][1],polje[3][1])!='A'){
        file<<"Case #"<<b<<": "<<funkcija(polje[0][1],polje[1][1],polje[2][1],polje[3][1])<<" won"<<endl;
        pobjednik=1;
    }
    else if(funkcija(polje[0][2],polje[1][2],polje[2][2],polje[3][2])!='A'){
        file<<"Case #"<<b<<": "<<funkcija(polje[0][2],polje[1][2],polje[2][2],polje[3][2])<<" won"<<endl;
        pobjednik=1;
    }
    else if(funkcija(polje[0][3],polje[1][3],polje[2][3],polje[3][3])!='A'){
        file<<"Case #"<<b<<": "<<funkcija(polje[0][3],polje[1][3],polje[2][3],polje[3][3])<<" won"<<endl;
        pobjednik=1;
    }
    else if(funkcija(polje[0][3],polje[1][2],polje[2][1],polje[3][0])!='A'){
        file<<"Case #"<<b<<": "<<funkcija(polje[0][3],polje[1][2],polje[2][1],polje[3][0])<<" won"<<endl;
        pobjednik=1;
    }
    else if(funkcija(polje[0][0],polje[1][1],polje[2][2],polje[3][3])!='A'){
        file<<"Case #"<<b<<": "<<funkcija(polje[0][0],polje[1][1],polje[2][2],polje[3][3])<<" won"<<endl;
        pobjednik=1;
    }
    else{
        if(negotov)
            file<<"Case #"<<b<<": Game has not completed"<<endl;
        else
            file<<"Case #"<<b<<": Draw"<<endl;
    }
    }


return 0;
    }
