#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <sstream>

using namespace std;

int jml[10];

int main()
{

    int kasus,x;
        string baris;                   /// ini 17 - 22 membaca file inputan dr soal, ada berapa case
        ifstream data;
        data.open ("A-large.in");
        getline(data, baris);
        (istringstream(baris) >> x);
    kasus=x;
    int j=1;
    while(!data.eof() && kasus>j-1)
    {
        if(j!=0){               //ini baca file juga,
        getline(data, baris);
        string kata,temp="";
        kata=baris;
        temp+=kata[0];
        for(int i=1 ; i<kata.length(); i++){
            if(kata[i]<temp[0])
                temp+=kata[i];
            else{
                string a=temp;
                temp=kata[i]+a;
            }
        }
        ofstream data1;
        data1.open("A-small-attempt6.out", ios::app);                   // ini membuat file outputan, buka file program nanti ada file baru
        data1<<"Case #"<<j<<": "<<temp<<endl;
        }
        j++;

    }


    return 0;
}
