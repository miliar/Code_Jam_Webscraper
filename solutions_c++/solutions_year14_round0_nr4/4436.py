#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <utility>
#include <stdlib.h>
#include <algorithm>
#include <iomanip>
#include <math.h>

using namespace std;

bool in_array(const int &needle, const vector<int> &haystack)
{
    int max=haystack.size();

    if (max==0) return false;

    for(int i=0; i<max; i++)
        if (haystack[i]==needle)
            return true;
    return false;
}

vector<double> explode(string inputstring, string delimiter)
{
    vector<double> explodes;
    inputstring.append(delimiter);
    while(inputstring.find(delimiter)!=string::npos){
        explodes.push_back(atof((inputstring.substr(0, inputstring.find(delimiter))).c_str()));
        inputstring.erase(inputstring.begin(), inputstring.begin()+inputstring.find(delimiter)+delimiter.size());
    }
    return explodes;
}

int ken_playing(vector<double> w_naomi_lies, vector<double> w_ken, vector<double> w_naomi, int best_score)
{
    bool bug = true;

    int nb_blocks = w_naomi.size();
    int a = 0, b = 0;

    int anti_score = 0;

    sort(w_ken.begin(), w_ken.end());
    sort(w_naomi.begin(), w_naomi.end());

    bool next = false;

    vector<int> j_played; // Ken's
    vector<int> k_played; // Naomi's

    for(int i = 0; i < nb_blocks; i++)
    {
        if(anti_score >= nb_blocks - best_score)
            return -1;

        next = false;
        for(int j = 0; j < nb_blocks; j++)
        {
            if(!in_array(j, j_played) && !next)
            {
                if(w_ken[j] > w_naomi_lies[i])
                {
                    next = true;

                    // Ken joue le premier block qui est plus grand que celui de Naomi
                    j_played.push_back(j);

                    // Naomi joue en réalité un autre block (son plus petit)

                    a = 0;
                    while(in_array(a, k_played))
                        a++;

                    if(w_naomi[a] >= w_ken[j] && bug)
                        return -1; //Naomi s'est trompée

                    k_played.push_back(a);

                    anti_score++;
                }
            }
        }

        if(!next)
        {
            // Naomi a joué un block plus lourd que tout ceux de Ken restants, Ken joue son moins lourd

            a = 0;
            while(in_array(a, j_played))
                a++;

            j_played.push_back(a);

            // Naomi joue en réalité le moins lourd battant celui de Ken

            b = 0;
            while(in_array(b, k_played) || w_naomi[b] < w_ken[a])
                b++;

            if(b >= nb_blocks  && bug)
                return -1;

            k_played.push_back(b);
        }

    }

    return nb_blocks - anti_score;
}


vector<double> naomi_thinking(vector<double> w_ken, vector<double> w_naomi, int nb_1_first, int nb_faibles)
{
    int score_est = 0;
    int nb_blocks = w_ken.size();

    vector<int> j_played;
    vector<int> k_played;

    vector<double> w_naomi_lies;

    int b = 0, c = 0;

    for(int i = 0; i < nb_1_first; i++)
    {
        // Naomi joue 1

        w_naomi_lies.push_back(1);

        b = 0;
        while(in_array(b, j_played))
            b++;
        j_played.push_back(b);

        c = 0;
        while(in_array(c, k_played) || w_naomi[c] < w_ken[b])
            c++;
        k_played.push_back(c);

        score_est++;
    }

    // Compter le nombre de blocks de Ken qui sont strictement au dessus tous les blocks restants de Naomi

    /*int nb_faibles = 0;
    bool next = true;
    for(int i = 0; i < nb_blocks; i++)
    {
        next = true;
        if(!in_array(i, j_played))
        {
            for(int j = 0; j < nb_blocks; j++)
            {
                if(!in_array(j, k_played) && next)
                {
                    if(w_naomi[j] > w_ken[i])
                        next = false;
                }
            }
            if(next)
                nb_faibles++;
        }
    }
    */

    for(int i = 0; i < nb_faibles; i++)
    {
        b = nb_blocks - 1;
        while(in_array(b, j_played))
            b--;
        j_played.push_back(b);

        w_naomi_lies.push_back((w_ken[b]+w_ken[b-1])/2);

        b = 0;
        while(in_array(b, k_played))
            b++;
        k_played.push_back(b);


    }

    for(int i = 0; i < nb_blocks; i++)
    {
        if(!in_array(i, k_played))
        {
            score_est++;
            w_naomi_lies.push_back(1);
        }
    }

    return w_naomi_lies;

}


int main()
{
    ifstream file("file.txt");



    ofstream fichier("result.txt", ios::out | ios::trunc);

    int nb_blocks = 0;

    if(file)
    {
        string row;
        getline(file, row);

        int score = 0;
        int score_d = 0;

        int nb_case = atoi(row.c_str());

        for(int a = 0; a < nb_case; a++)
        {
            score = 0;
            score_d = 0;

            getline(file, row);
            nb_blocks = atoi(row.c_str());

            vector<double> w_ken(nb_blocks);
            vector<double> w_naomi(nb_blocks);
            vector<double> w_naomi_lies;

            getline(file, row);
            w_naomi = explode(row, " ");

            getline(file, row);
            w_ken = explode(row, " ");

            sort(w_naomi.begin(), w_naomi.end());
            sort(w_ken.begin(), w_ken.end());

            score = ken_playing(w_naomi, w_ken, w_naomi, 0);

            int var_score = 0;

            for(int i1 = 0; i1 < nb_blocks; i1++)
            {
                for(int i2 = 0; i2 < nb_blocks - i1; i2++)
                {
                    if(score_d < nb_blocks)
                    {
                        w_naomi_lies = naomi_thinking(w_ken, w_naomi, i1, i2);
                        var_score = ken_playing(w_naomi_lies, w_ken, w_naomi, 0);
                        if(var_score > score_d)
                            score_d = var_score;
                    }
                }
            }


            cout << "Case #" << a+1 << ": " << score_d << " "<< score << endl;
            fichier << "Case #" << a+1 << ": " << score_d << " "<< score << endl;
        }


    }
    else
    {
        cout << "Not found." << endl;
    }

    return 0;
}
