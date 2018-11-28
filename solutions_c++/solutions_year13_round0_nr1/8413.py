//
//  main.cpp
//  tic-tac-toe-totem
//
//  Created by Thiebaud Vannier on 13/04/13.
//  Copyright (c) 2013 Thiebaud Vannier. All rights reserved.
//
#include <iostream>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

/*
 le joueur 1 est celui qui joue les X et le joueur 2 est celui qui joue les O
 la diagonal1 est cel qui vas du haut gauche au bas droite 
 la diagonal2 est cel qui vas du haut droite au bas gauche
*/

//typedef enum CaseGrille{ rien=0, joueur1=1, joueur2=2, totem=3} CaseGrille;
typedef enum Victoir{nonDef=-1, aucune=0, joueur1=1, joueur2=2}Victoir;

#define TAILLE_GRILLE 4

//on analyse la grille et ou di qui a gagner ou perue sans la charger, en la lisant directement pour estre sur d'avoir du resultat plus rapide
void analyzeGrille();

int main(int argc, const char * argv[])
{
    //declaration de variable
    int nbGrille = 0;
    
    //on fout tout sur l'entrée standard
    cout << "combien de grille v'at-on devoire analizé" << endl;
    scanf("%d", &nbGrille);
    cout << "faite un copier coller de tout les grille ici" << endl;
    
    //on initialise la grille
    for (int i=0; i<nbGrille; i++) {
        cout << "Case #" << i+1 << ": ";
        analyzeGrille();
    }
    return 0;
}

void analyzeGrille()
{
    //declaration de variable
    string ligne;
    Victoir vicLigne=nonDef, vicColone[TAILLE_GRILLE], diagonal1=nonDef, diagonal2=nonDef;
    Victoir caseGrille=nonDef;
    Victoir grille = nonDef;//variable qui retien quel joueur a gagner la grille si il y en a un
    bool caseVide = false;//permet de savoir si il reste des case vide ou non
    
    //on initialise le tableau des colone
    for (int i=0; i<TAILLE_GRILLE; i++) {
        vicColone[i]=nonDef;
    }
    
    //on li les info de l'utilisateur
    for (int i=0; i<TAILLE_GRILLE; i++) {
        cin >> ligne;
        vicLigne = nonDef;//on remet vicLigne a nonDef
        
        if (ligne.length() == TAILLE_GRILLE)//si l'utilisateur a rentré sufisement de caractere
        for (int j=0; j<TAILLE_GRILLE; j++) {
            //en fonction du symbole on di a quel joueur est la case
            if (ligne[j]=='X') caseGrille = joueur1;
            else if (ligne[j] == 'O') caseGrille = joueur2;
            else if (ligne[j] == 'T') caseGrille = nonDef;
            else
            {
                caseGrille = aucune;
                caseVide = true;
            }
            //maintenent on dit si quelqu'un a gagner ou non en fonction de la case
            //diagonale1
            if (i==j && diagonal1==nonDef)
                diagonal1 = caseGrille;
            else if (i==j && diagonal1 != caseGrille && caseGrille != nonDef)
                diagonal1 = aucune;
            //diagonal2
            if (i+j==TAILLE_GRILLE-1 && diagonal2==nonDef)
                diagonal2 = caseGrille;
            else if (i+j==TAILLE_GRILLE-1 && diagonal2 != caseGrille && caseGrille != nonDef)
                diagonal2 = aucune;
            //ligne
            if (vicLigne==nonDef)
                vicLigne = caseGrille;
            else if (vicLigne != caseGrille && caseGrille != nonDef)
                vicLigne = aucune;
            //colone
            if (vicColone[j]==nonDef)
                vicColone[j] = caseGrille;
            else if (vicColone[j] != caseGrille && caseGrille != nonDef)
                vicColone[j] = aucune;
        }
        if (vicLigne == joueur1 || vicLigne == joueur2)
        {
            if (grille==nonDef)
                grille = vicLigne;
            else if (vicLigne!=grille)
                grille = aucune;
        }
        
    }
    
    //on regarde quel joueur a gagner
    if (diagonal1 == joueur1 || diagonal1 == joueur2)
    {
        if (grille==nonDef)
            grille = diagonal1;
        else if (diagonal1!=grille)
            grille = aucune;
    }
    if (diagonal2 == joueur1 || diagonal2 == joueur2)
    {
        if (grille==nonDef)
            grille = diagonal2;
        else if (diagonal2!=grille)
            grille = aucune;
    }
    for (int i=0; i<TAILLE_GRILLE; i++) {
        if (vicColone[i] == joueur1 || vicColone[i] == joueur2)
        {
            if (grille==nonDef)
                grille = vicColone[i];
            else if (vicColone[i]!=grille)
                grille = aucune;
        }
    }
    if (grille == nonDef && !caseVide)
        grille = aucune;
    
    //on ecrit le score
    switch (grille) {
        case joueur1:
            cout << "X won" << endl;
            break;
        case joueur2:
            cout << "O won" << endl;
            break;
        case aucune:
            cout << "Draw" << endl;
            break;
        case nonDef:
            cout << "Game has not completed" << endl;
            break;
        default:
            break;
    }
    
    
}


































