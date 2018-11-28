//
//  main.cpp
//  Deceitful War
//
//  Created by Dylan Stenico on 12/04/14.
//  Copyright (c) 2014 Dylan Stenico. All rights reserved.
//


#include <iostream>
#include <fstream>

using namespace std;

void QuickSort(double list[], int dim);
void stampa(double * vet, int dim)
{
    for(int j = 0; j < dim; j++)
    {
        cout << vet[j] << " ";
    }
}
int main(int argc, const char * argv[])
{
    ifstream input("/Users/dylanstenico/Documents/School/InformationTechnology/2014/GoogleCodeJam/Deceitful War/D-large.in.txt");
    ofstream output("/Users/dylanstenico/Documents/School/InformationTechnology/2014/GoogleCodeJam/Deceitful War/D-large-attempt0.ou.txt");
    input.precision(5);
    
    int test;
    int blocks;
    
    int naomiPoint;
    int kenPoint;
    int naomiPoint2;
    int kenPoint2;
    
    double *naomi;
    double *ken;
    double *naomi2;
    double *ken2;
    
    input >> test;
    for(int i = 0; i < test; i++)
    {
        naomiPoint = 0;
        kenPoint = 0;
        naomiPoint2 = 0;
        kenPoint2 = 0;
        input >> blocks;
        int blocks2 = blocks;
        naomi = (double *) malloc(sizeof(double)* blocks);
        ken = (double *) malloc(sizeof(double)* blocks);
        
        naomi2 = (double *) malloc(sizeof(double)* blocks);
        ken2 = (double *) malloc(sizeof(double)* blocks);
        
        for(int j = 0; j < blocks; j++)
        {
            input >> naomi[j];
        }
        for(int j = 0; j < blocks; j++)
        {
            input >> ken[j];
        }
        
        QuickSort(naomi, blocks);
        QuickSort(ken, blocks);
        
        for(int j = 0; j < blocks; j++)
        {
            ken2[j] = ken[j];
            naomi2[j] = naomi[j];
        }
        
        while(blocks > 0)
        {
            /*cout << "partenza" << endl;
            stampa(naomi, blocks);
            cout << endl;
            stampa(ken, blocks);
            cout << endl;*/
            int trovato = -1;
            for(int k = 0; k < blocks; k++)
            {
                if(ken[k] > naomi[0])
                {
                    trovato = k;
                    break;
                }
            }
            for(int j = 0; j < blocks - 1; j++)
            {
                naomi[j] = naomi[j + 1];
            }
            
            if(trovato > -1)
            {
                for(int j = trovato; j < blocks -1; j++)
                {
                    ken[j] = ken[j + 1];
                }
                blocks --;
                kenPoint++;
            }
            else
            {
                for(int j = 0; j < blocks - 1; j++)
                {
                    ken[j] = ken[j + 1];
                }
                blocks --;
                naomiPoint++;
            }
            
            /*cout << "arrivo" << endl;
            stampa(naomi, blocks);
            cout << endl;
            stampa(ken, blocks);
            cout << endl;
            */
        }
        //cout << "punteggio1: " << naomiPoint << endl; //<< " " << kenPoint << endl;
        while(blocks2 > 0)
        {
            if(naomi2[blocks2 - 1] > ken2[blocks2 - 1])
            {
                blocks2 --;
                naomiPoint2++;
            }
            else
            {
                for(int k = 0; k < blocks2 - 1; k++)
                {
                    naomi2[k] = naomi2[k + 1];
                }
                blocks2 --;
                kenPoint2++;
            }
        }
        //cout << "punteggio2: " << naomiPoint2 << endl;
        output << "Case #" << i + 1 << ": " << naomiPoint2 << " " << naomiPoint << endl;
    }
}

void QuickSort(double list[], int dim)
{
    for(int i = 0; i < dim -1; i++)
    {
        for(int j = i + 1; j < dim; j++)
        {
            if(list[j] < list[i])
            {
                double tmp = list[j];
                list[j] = list[i];
                list[i] = tmp;
            }
        }
    }
}

void punteggioWar(double v1[], double v2[], int * punteggio)
{
    
}