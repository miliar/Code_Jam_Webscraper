#ifndef OBJET_H
#define OBJET_H

#define taille 100

#include <string>
#include <fstream>
#include <iostream>

using namespace std;

class Objet
{
public:
    Objet(int N_, int M_);
    bool gagnant(char p);
    bool gameNotEnded();
    int tab[taille][taille];
    string solve();
    int elimination();
    bool eliminerligne(int l, int val);
    bool eliminercolonne(int c, int val);
    void display();
    int N,M;
};

#endif // OBJET_H
