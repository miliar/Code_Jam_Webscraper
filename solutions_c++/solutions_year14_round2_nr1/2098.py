#include <stdio.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
    ifstream fin("A-small-attempt0.in");
    int t;
    fin >> t;
    ofstream fout("output.txt");
    for(int s=1; s<=t; ++s)
    {
        int n;
        fin >> n;
        vector <string> words;
        for(int i=0; i<n; ++i)
        {
            string temp;
            fin >> temp;
            words.push_back(temp);
        }

        //cout << "Case #" << s << ": " << endl;

        /*for(int i=0; i<n; ++i)
            cout << words.at(i) << endl;*/

        vector <string> ridotte=words;
        vector <vector <int> > nlettere (ridotte.size());

        for(int i=0; i<ridotte.size(); ++i)
        {
            nlettere.at(i).push_back(1);
            if(ridotte.at(i).size()>1)
            for(int j=1; j<ridotte.at(i).size(); ++j)
            {
                if(ridotte.at(i).at(j)==ridotte.at(i).at(j-1))
                {
                    ridotte.at(i).erase(j,1);
                    ++nlettere.at(i).at(j-1);
                    --j;
                }
                else
                    nlettere.at(i).push_back(1);

            }


        }

        /*cout << endl;
        for(int i=0; i<n; ++i)
        {
            cout << ridotte.at(i) << " ";
            for(int j=0; j<ridotte.at(i).size(); ++j)
                cout << nlettere.at(i).at(j) << " ";
            cout << endl;
        }*/

        bool uguali=true;
        for(int i=1; i<ridotte.size(); ++i)
            if(ridotte.at(i)!=ridotte.at(i-1))
            {
                uguali=false;
                break;
            }

        //cout << endl << uguali << endl;

        fout << "Case #" << s << ": ";

        if(!uguali)
            fout << "Fegla Won" << endl;
        else
        {
            int mosse=0;
            for(int j=0; j<nlettere.at(0).size(); ++j)
            {
                int s=0;
                for(int i=0; i<nlettere.size(); ++i)
                    s+=nlettere.at(i).at(j);
                int media=int(round((float(s)/ridotte.size())));
                //cout << "media " << media << endl;

                for(int i=0; i<nlettere.size(); ++i)
                    mosse+=abs(media-nlettere.at(i).at(j));
            }
            //cout << "mosse " << mosse << endl;
            fout << mosse << endl;
        }
    }
}

