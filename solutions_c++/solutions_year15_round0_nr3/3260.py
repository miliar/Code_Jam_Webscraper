#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int indiceMotif(string motif);

string produit(string motif1, string motif2);

string dico[8][8] = {{"1",  "i",    "j",    "k",    "-1",   "-i",   "-j",   "-k"},
                     {"i",  "-1",   "k",    "-j",   "-i",   "1",    "-k",   "j"},
                     {"j",  "-k",   "-1",   "i",    "-j",   "k",    "1",    "-i"},
                     {"k",  "j",    "-i",   "-1",   "-k",   "-j",   "i",    "1"},
                     {"-1", "-i",   "-j",   "-k",   "1",    "i",    "j",    "k"},
                     {"-i", "1",    "-k",   "j",    "i",    "-1",   "k",    "-j"},
                     {"-j", "k",    "1",    "-i",   "j",    "-k",   "-1",   "i"},
                     {"-k", "-j",   "i",    "1",    "k",    "j",    "-i",   "-1"}};

string recherche(string chaine, string valeur, long long indDeb, long long *X, long long L, long long *indice);

string dernierProduit(string chaine, long long indDeb, long long X, long long L);

int main()
{
    ifstream input("input.in");
    ofstream output("output.out");
    if(input == NULL)
        return -1;

    int T;
    long long L, X;
    string chaine, mpy;
    input >> T;
    long long indi, indj, indk;
    for(int i(0); i<T; i++){
        cout << "**********case " << i+1 << "**************" << endl;
        output << "Case #" << i+1 << ": ";
        input >> L;
        input >> X;
        input >> chaine;
        string vali = recherche(chaine, "i", 0, &X, L, &indi);
        if(vali == ""){
            output << "NO";
            if(i < T-1)
                output << endl;
            continue;
        }
        string valj = recherche(chaine, "j", indi, &X, L, &indj);
        if(valj == ""){
            output << "NO";
            if(i < T-1)
                output << endl;
            continue;
        }
        string valk = recherche(chaine, "k", indj, &X, L, &indk);
        if(valk == ""){
            output << "NO";
            if(i < T-1)
                output << endl;
            continue;
        }
        string fin = dernierProduit(chaine, indk, X, L);
        mpy = produit("1", vali);
        mpy = produit(mpy, valj);
        mpy = produit(mpy, valk);
        mpy = produit(mpy, fin);
        if(mpy != "-1"){
            output << "NO";
            if(i < T-1)
                output << endl;
            continue;
        }
        output << "YES";
        if(i < T-1)
            output << endl;
        continue;
    }
    return 0;
}

string recherche(string chaine, string valeur, long long indDeb, long long *X, long long L, long long *indice){
    if(indDeb >= L)
        return "";
    long long j = indDeb;
    string mpy = "1", temp;
    while(j < L || *X > 1){
        temp = "";
        temp += chaine[j];
        mpy = produit(mpy, temp);
        j++;
        if(j == L && *X > 1){
            j=0;
            (*X)--;
        }
        if(mpy == valeur || produit(mpy, "-1") == valeur){
            *indice = j;
            return mpy;
        }
    }
    return "";
}

int indiceMotif(string motif){
    if(motif.size() == 1){
        switch(motif[0]){
        case '1':
            return 0;
            break;
        case 'i':
            return 1;
            break;
        case 'j':
            return 2;
            break;
        case 'k':
            return 3;
            break;
        }
    }else{
        switch(motif[1]){
        case '1':
            return 4;
            break;
        case 'i':
            return 5;
            break;
        case 'j':
            return 6;
            break;
        case 'k':
            return 7;
            break;
        }
    }
    return -1;
}

string produit(string motif1, string motif2){
    int ind1 = indiceMotif(motif1), ind2 = indiceMotif(motif2);
    return dico[ind1][ind2];
}

string dernierProduit(string chaine, long long indDeb, long long X, long long L){
    if(indDeb >= L)
        return "1";
    string mpy = "1", tmp;
    long long j = indDeb;
    while(j < L || X > 1){
        tmp = "";
        tmp += chaine[j];
        mpy = produit(mpy, tmp);
        j++;
        if(j == L && X > 1){
            j=0;
            X--;
        }
    }
    return mpy;
}






