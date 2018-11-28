#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <sstream>

using namespace std;

int jml[10];

int main()
{
    long long int N,K,L=0,tampil,x;
    jml[0]=jml[1]=jml[2]=jml[3]=jml[4]=jml[5]=jml[6]=jml[7]=jml[8]=jml[9]=0;

    int kasus;
        string baris;
        ifstream data;
        data.open ("B-large.in");
        getline(data, baris);
        (istringstream(baris) >> x);
        kasus=x;
    int j=0;
    while(!data.eof() && kasus>j-1)
    {
        if(j!=0){
        getline(data, baris);
        string kata;
        kata=baris;
        int a=0;
        for(int j=0 ; j<kata.length();j++){
            if(kata[j]=='-' && j==0)
                a++;
            if(kata[j]=='+' && kata[j+1]=='-')
                a+=2;
        }
        ofstream data1;
        data1.open("A-small-attempt6.out", ios::app);
                data1<<"Case #"<<j<<": "<<a<<endl;
        }
        j++;
    }


    return 0;
}
