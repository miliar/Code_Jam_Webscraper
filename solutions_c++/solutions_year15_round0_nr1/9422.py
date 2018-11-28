/*
 * =====================================================================================
 *
 *       Filename:  main.cc
 *
 *    Description:  google code jam Standing Ovation 
 *
 *        Version:  1.0
 *        Created:  11/04/2015 21:50:55
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Alexandre BUISSON-CHAVOT (albuic), admin@albuic.tk
 *   Organization:  Destiny Corporation©
 *
 * =====================================================================================
 */

#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string>


using namespace std;


int main(int argc, char** argv){
    

    ifstream input("input.txt", ios::in);
    string str;
    int numberOfLigne;
    int** shyness;


    if(input){
        getline(input, str);
        
        cout << "Getting File" << endl;
        
        numberOfLigne = atoi(str.c_str());
        
        /* malloc en fonction du nombre de ligne */
        shyness = (int**)malloc(sizeof(int*)*numberOfLigne);

        /* Copie des lignes */
        for(int i = 0 ; i < numberOfLigne ; i++){
            getline(input, str);

            /* recup de l'espace dans j */
            int j = 0;
            char espace = '0';
            while(espace != ' '){
                espace = str[j];
                j++;
            }

            
            /* recup premiere partie : Smax */
            char char_maxSh[4];
            int maxSh;
            int k = 0;
            for(k = 0 ; k < j ; k++){
                char_maxSh[k] = str[k];
            }
            char_maxSh[k-1] = '\0';
            maxSh = atoi(char_maxSh);
            
            shyness[i] = (int*)malloc(sizeof(int) * (maxSh+2));
            shyness[i][0] = maxSh;
            cout << shyness[i][0] << " ";
            
            
            /* recup 2eme partie */
            for(k = 0 ; k < maxSh+1 ; k++){
                char char_number[2];
                char_number[0] = str[j+k];
                char_number[1] = '\0';
                int number = atoi(char_number);
                shyness[i][k+1] = number;
                cout << shyness[i][k+1];
            }
            cout << endl;

            /* completer si \n */
        }
        
        cout << "Affichage tableau :" << endl;
        /* Affichage lignes */
        int j,k;
        cout << "numberOf ligne = " << numberOfLigne << endl;
        for(j = 0 ; j < numberOfLigne ; j++){
            cout << "shyness = " << shyness[j][0]+1+1 << endl;
            cout << shyness[j][0] << " ";
            for(k = 1 ; k < shyness[j][0]+1+1 ; k++){
                cout << shyness[j][k] << "/";
            }
            cout << endl;
        }

        input.close();

        /* RESOLUTION */
        int* reponse;
        reponse = (int*)malloc(sizeof(int) * numberOfLigne);

        for(int i = 0 ; i < numberOfLigne ; i++){
            int sum = 0;
            int amis = 0;
            for(k = 1 ; k < shyness[i][0]+2 ; k++){
                sum += shyness[i][k];
                while(sum < k){
                    sum++;
                    amis++;
                }
            }

            reponse[i] = amis;
        }

        /* Affichage reponses */
        ofstream sortie("sortie.txt", ios::out | ios::trunc);

        if(sortie){

        }else{
            cout << "FUCKING sortie" << endl;
            exit(-1);
        }

        cout << "REPONSES : " << endl;
        for(int i = 0 ; i < numberOfLigne ; i++){
            cout << "Case #" << i+1 << ": " << reponse[i] << endl;
            sortie << "Case #" << i+1 << ": " << reponse[i] << endl;
        }

        sortie.close();

    } else {
        cout << "Fucking ERROR d'ouverture !" << endl;
        exit(-1);
    }
}


