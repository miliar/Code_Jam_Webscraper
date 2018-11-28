#include <cstdio>
#include <iostream>
#include <string>
//#include <fstream>
using namespace std;


int main() {
    int t,i,maximum,current,j, friendsTotal, currentCase = 1, totalStanding;

    string groupString;
    do {
        cin >> t;
    } while (t>100 && t<1);
   // ofstream myfile;
   // myfile.open("output.out");
    for(i=0;i<t;i++)
    {
        friendsTotal = 0;
        totalStanding = 0;
        cin >> maximum;
        cin >> groupString;
        for(j=0; j < (int)groupString.size(); j++) {
            current = groupString[j] - 48;
            if(current != 0) {
                while(j > totalStanding) {
                  //  cout << "J: " << j << " still smaller than totalStanding: " << totalStanding << endl;
                    friendsTotal++;
                    totalStanding++;
                  //  cout << "Now j:" << j << " and totalStanding: " << totalStanding << endl;
                }
            }
            totalStanding += current;
        }
        cout << "Case #" << currentCase++ << ": " << friendsTotal << endl;
    }
   // myfile.close();
    return 0;
}
