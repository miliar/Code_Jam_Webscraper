#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <list>
#include <fstream>
#include <algorithm>;
#include <iomanip>   

using namespace std;
typedef unsigned int uint;

void solve(istream& is, uint index)
{
    int arr[17];
    
    for (int i = 0; i < 17; i++)
        arr[i] = 0;
    
    int rij;
    is >> rij;
    
    for (int i = 1; i <= 4; i++) {
        int a,b,c,d;
        is >> a; is >> b; is >> c; is >> d;
        if (i == rij) {
            arr[a]++;arr[b]++;arr[c]++;arr[d]++;
        }
    }

    is >> rij;
    for (int i = 1; i <= 4; i++) {
        int a,b,c,d;
        is >> a; is >> b; is >> c; is >> d;
        if (i == rij) {
            arr[a]++;arr[b]++;arr[c]++;arr[d]++;
        }
    }
    
    int teller = 0;
    int nummer = 0;
    
    for (int i = 0; i < 17; i++) {
        
        if (arr[i] == 2) {
            teller++;
            nummer = i;
        }
    }
            
    
    if (teller == 0) {
        cout << "Case #" << index << ": " << "Volunteer cheated!" << endl;
    } else if (teller == 1) {
        cout << "Case #" << index << ": " << nummer << endl;
    } else {
        cout << "Case #" << index << ": " << "Bad magician!" << endl;
    }
}

void oef(istream& is)
{
    uint n;
    is >> n;
    for(uint i = 0;i < n; i++)
        solve(is, i+1);
}

#define EIGENTEST 1

int main()
{
    ifstream myfile ("/home/thomas/Downloads/A-small-attempt0.in");
    
    if (myfile.is_open())
    {
        oef(myfile);
        
        myfile.close();
    }
    
    return 0;
}

