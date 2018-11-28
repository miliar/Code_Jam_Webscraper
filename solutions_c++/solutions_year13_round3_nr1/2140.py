#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std;
int hitungCtr(string word, int w_length, int n);

int main()
{
    int t, n;
    string str;
    getline(cin, str);
    t = atoi(str.c_str());
    for(int s=0; s<t; s++)
    {
        getline(cin, str);
        int w_length = str.find(" ");
        string word = str.substr(0, w_length);
        string ntemp = str.substr(w_length+1);
        n = atoi(ntemp.c_str());
        //cout << word << n << "\n";

        int hasil = hitungCtr(word, w_length, n);

        cout << "Case #" << s+1 << ": " << hasil<< "\n";
    }
    return 0;
}

int hitungCtr(string word, int w_length, int n)
{
    int ctr = 0;
    int jum = 0;
    do
    {
        for (int i=n; i<=w_length; i++)
        {
            jum = 0;
            string sub_res = word.substr(0, i);
            for (int j=0; j<sub_res.length(); j++)
            {
                if(sub_res[j]!='a' && sub_res[j]!='e' && sub_res[j]!='i' && sub_res[j]!='o' && sub_res[j]!='u')
                {
                    jum++;
                }
                else
                {
                    jum = 0;
                }
                if(jum==n)
                {
                    ctr++;
                    //cout << "*";
                    break;
                }
            }

            //cout << sub_res << i << "\n";
        }
        for (int i=(w_length-n); i>0; i--)
        {
            jum = 0;
            string sub_res = word.substr(i);
            for (int j=0; j<sub_res.length(); j++)
            {
                if(sub_res[j]!='a' && sub_res[j]!='e' && sub_res[j]!='i' && sub_res[j]!='o' && sub_res[j]!='u')
                {
                    jum++;
                }
                else
                {
                    jum = 0;
                }
                if(jum==n)
                {
                    ctr++;
                    //cout << "*";
                    break;
                }
            }
            //cout << sub_res << i << "\n";
        }

        int end = word.length()-2;
        word = word.substr(1, end);
        w_length = word.length();

    } while(word.length()>=n);
        //cout << "word" << word;

    return ctr;
}
