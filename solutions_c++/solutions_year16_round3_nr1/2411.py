#include<bits/stdc++.h>

using namespace std;

priority_queue <pair<int,int>> kol;

int wynik[1000001];

int main()
{
    ifstream in;
    ofstream out;
    in.open("in.txt");
    out.open("out.txt");

    int t;
    int n;
    in >> t;
    for(int i=1; i<=t; i++)
    {
        in >> n;
        int x;
        for(int a=0; a<n; a++)
        {
            in >> x;
            kol.push(make_pair(x,a));
        }
        out << "Case #" << i << ": ";
        if(n>2)
        {
            int ile=-1;
            while(!kol.empty())
            {
                pair <int,int> t=kol.top();
                kol.pop();
                ile++;
                wynik[ile]=t.second;
                if(t.first>1)
                {
                    kol.push(make_pair(t.first-1,t.second));
                }
            }
            ile--;
            for(int a=0; a<ile; a++)
            {
                out << char(wynik[a]+65) << " ";
            }
            out << char(wynik[ile]+65) << char(wynik[ile+1]+65) << endl;
        }
        else
        {
            while(!kol.empty())
            {
                kol.pop();
            }
            for(int a=0; a<x; a++)
            {
                out << "AB" << " ";
            }
            out << endl;
        }
    }

    in.close();
    out.close();
}
