#include <iostream>
#include<fstream>
#include <stdio.h>
#include<math.h>
#include<cmath>
using namespace std;

int main()
{

    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    int y,numberofseat=0;
    short int t=0, Smax=0;
    string str;

    cin>>t;
    for(int i=0;i<t;i++){
        cin>>Smax;
        cin >> str;
        y=0;
        numberofseat=0;
        for(int j=0 ; j <= Smax ; j++){
        if( j > numberofseat){
        y+=j-numberofseat;
        numberofseat += j-numberofseat;

        }

          numberofseat +=str[j]-(int)'0';



        }
cout<<"Case #"<<i+1<<": "<<y<<endl;

    }






    return 0;
}
