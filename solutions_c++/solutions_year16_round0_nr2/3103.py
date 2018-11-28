#include <iostream>
#include <fstream>

using namespace std;

int revcake(string);

int main()
{
    int tests, counts=1;
    string cake;
    ifstream fin("B-large.in");
    ofstream fout("data.out",std::ofstream::trunc);

    fin >> tests;
    while(!fin.eof()&&tests){
        fin >> cake;
        tests--;
        int rev = revcake(cake);
        cout << "Case #"<< counts << ": " << rev;
        fout << "Case #"<< counts << ": " << rev;
        counts++;
        if(tests){
            cout << endl;
            fout << endl;
        }
    }
    fin.close();
    fout.close();
    return 0;;
}
int revcake(string cake){
    int rev=0;
    for(int i = 0; i<cake.length()-1; i++){
        if((cake.at(i)=='-')&&(cake.at(i+1)=='+')||(cake.at(i)=='+')&&(cake.at(i+1)=='-')) rev++;
    }
    if(cake[cake.length()-1]=='-')rev++;
    return rev;
}
