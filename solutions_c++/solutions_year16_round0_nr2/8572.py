#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    int x,l;
    string s,n;


    int kasus;
        string baris;                   /// ini 17 - 22 membaca file inputan dr soal
        ifstream data;
        data.open ("B-large.in");
        getline(data, baris);
        (istringstream(baris) >> x);
        kasus=x;
    int j=0;
 while(!data.eof() && kasus>j-1)
    {

        if(j!=0){
        getline(data, baris);                               // baca file dr file
        s = baris;
        l = 0;

        if(s[0]=='-'){
                l+=1;
            }
        for(int i = 0; i<s.length(); i++){

            if(s[i]== '+' && s[i+1] == '-'){
                l+=2;
            }
        }

    ofstream data1;
        data1.open("B-large.out", ios::app);                   // ini membuat file outputan, buka file program nanti ada file baru
                data1<<"Case #"<<j<<": "<<l<<endl;

        }
    j++;
    }

    return 0;
}
