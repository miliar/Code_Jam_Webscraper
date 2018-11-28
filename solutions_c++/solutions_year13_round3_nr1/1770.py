#include<iostream>
#include <fstream>

using namespace std;

bool vocal(char a) {
    if(a=='a'||a=='i'||a=='e'||a=='o'||a=='u') {
        return true;
    }
    return false;
}

long long getans(string linea, int n) {
    long long cont=0;
    int consonantes=0, mult, cons2;
    for(int i=0; i<linea.length(); i++) {
        //cout<<i<<" ";
        if(!vocal(linea.at(i))) {
            consonantes++;
            if(consonantes==n) {
                cons2=0;
                int j=i-1;
                while(j>=0&&cons2<n) {
                    if(!vocal(linea.at(j))) {
                        cons2++;
                    }
                    else {
                        cons2=0;
                    }
                    j--;
                }
                if(cons2==n) {
                    j++;
                }
                mult=i-j+1-n;
                cout<<i<<" "<<mult<<" "<<(linea.length()-i)<<endl;
                cont+=mult*(linea.length()-i);
                i-=(n-1);
                consonantes=0;
            }
        }
        else {
            consonantes=0;
        }
    }
    cout<<endl;
    return cont;
}

int main() {
    int T, caso=0; //Opciones es la cantiad de respuestas posibles.
    ofstream myfile;
    ifstream myReadFile;
    myReadFile.open("A-small-attempt0 (3).in");
    myfile.open ("Aoutput.txt");
    myReadFile>>T;
    while(T--) {
        caso++;
        string linea;
        int n;
        myReadFile>>linea>>n;
        myfile<<"Case #"<<caso<<": "<<getans(linea, n)<<endl;
    }
    myfile.close();
    return 0;
}
