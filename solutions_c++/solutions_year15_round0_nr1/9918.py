#include <bits/stdc++.h>
using namespace std ;

int main()
{
    ifstream fin ("A-small-attempt0.in") ;
    ofstream fout ("A-small-attempt0.out") ;
    int t ;
    fin >> t ;
    for(int h=1;h<=t;h++)
    {
        int s,somme=0,res=0,a ;
        fin >> s ;
        string ch ;
        fin >> ch ;
        //cout << (int)ch[0];
        for (int i=0;i<s+1;i++)
        {
            a= (int)ch[i]-48;
            if (a!=0&&i>somme){
                res+= i-somme ;
                somme+=res ;
            }
            somme+=a;

        }
        fout << "Case #"<<h<<": "<<res<< endl;
    }

    return 0;
}
