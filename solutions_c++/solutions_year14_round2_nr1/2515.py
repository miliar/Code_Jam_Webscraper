#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");

    int t, i;

    fin >> t;

    for(int j = 1; j <= t; j++)
    {

        int n; int countx = 0, flag = 0,y;
        fin >> n;
        string s1, s2;
        fin >> s1 >> s2;
        i = 0;
        if(s2.length() > s1.length()) {string tt = s1; s1 = s2; s2 = tt;}
        if(s1 == s2){countx = 0;}
        else{

            int q = 0;
                while(i < s1.length())
                {
                    char temp = s1[i]; int mycount1 =0, mycount2 =0,mycount11 =0, mycount21 =0;
                    for( y = i; s1[y] == temp; y++){mycount1++;}

                    for(y = q; s2[y] == temp; y++){mycount2++;}
                    if(mycount2 == 0) {flag = 1; break;}
                    else {if(mycount1 >= mycount2) countx += mycount1-mycount2;
                            else countx += mycount2-mycount1;}
                    i += mycount1;
                    q += mycount2;
                }
                if(s1.length() == s2.length()){
                y = s2.length()-1; int dum = 0;
                for(i = 0; i <s1.length(); i++) if(s2[y] == s1[i]) dum++;
                if(dum == 0) flag = 1;}
        }
        fout << "Case #" << j <<": " ;
        if(flag == 0) fout << countx;
        else fout << "Fegla Won";
        fout << "\n";


    }
    fin.close();
fout.close();
    return 0;
}
