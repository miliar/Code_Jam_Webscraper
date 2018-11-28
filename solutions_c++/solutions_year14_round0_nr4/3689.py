#include <iostream>
#include <fstream>
#include <stdbool.h>
#include <algorithm>
#include <vector>
#include <iterator>
using namespace std;

bool cmp (double i, double j) { return (i>j); }

int main()
{
    fstream fin, fout;
    fin.open("D-large.in");
    fout.open("c4.txt");
    vector <double> hKen; vector <double> dKen;
    vector <double> hNao; vector <double> dNao;
    int N, k, b, i, j, o = -1; double tmp, h; int hscore = 0, dscore = 0;
    fin >> N;
    for (k = 1; k <=N; k++)
    {
        hscore = 0; dscore = 0;
        fin >> b;
        for (i = 0; i < b; i++)
        {
            fin >> tmp; hNao.push_back(tmp); dNao.push_back(tmp);
        }

        for (i = 0; i < b; i++)
        {
            fin >> tmp; hKen.push_back(tmp); dKen.push_back(tmp);
        }
        sort(hKen.begin(), hKen.end(), cmp); sort(hNao.begin(), hNao.end(), cmp);
        sort(dKen.begin(), dKen.end(), cmp); sort(dNao.begin(), dNao.end(), cmp);
        for (i = 0; i < b; i++)
        {
            h = hKen.at(0); //cout << "!!!!!"<< h << endl;s
            o = -1;
            for (j = hKen.size()-1; j >=0; j--)
            {
                //cout << "Ken " << hKen.at(j) << " h:" << h << " j:"<<j<< endl;
                if(((hKen.at(j))>(hNao.back()))&&(hKen.at(j)<=h)) { h = hKen.at(j); o = j; }
            }

            if (o == -1) {hKen.pop_back(); hNao.pop_back(); hscore++;}
            else
            {
                hKen.erase(hKen.begin()+o); hNao.pop_back();
            }
            //if (hNao.at(b-i-1)-hKen.at(b-i-1) > 0) hscore++; cout << k;
        }
        for (i = 0; i < b; i++)
        {
            if(dNao.at(dNao.size()-1)<dKen.at(dKen.size()-1))
            {
                dNao.pop_back(); dKen.erase(dKen.begin());
            }
            else
            {
                dNao.pop_back(); dKen.pop_back(); dscore++;
            }
        }
        fout <<"Case #"<<k<<": "<<dscore<<" "<<hscore<<endl;
    }
    fin.close(); fout.close(); return 0;
}
