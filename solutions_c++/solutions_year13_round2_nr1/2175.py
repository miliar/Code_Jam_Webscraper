#ifndef OBJET_H
#define OBJET_H

#define taille 100

#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <map>


using namespace std;

class Objet
{
public:
    Objet(int N);
    int A;
    int solve();
    void tri();
    vector<int> motes;
    bool possible();
    int nbajouter(int t, int s);
};


#endif // OBJET_H
