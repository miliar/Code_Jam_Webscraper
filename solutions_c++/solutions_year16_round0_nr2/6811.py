#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

static int times=0;

void myReverse(string& cake) {
    int len = cake.length();
    int first=0;
    int last=len-1;
    while (cake[first]=='+')
        first++;
    if (first-1 == last)
        return;
    while (cake[last]=='+')
        last--;
    
    if (first != 0)
        times++;
    
    for(int i=first; i<=last; i++) {
        if (cake[i] == '+')
            cake[i] = '-';
        else
            cake[i] = '+';
    }
    
    for(int i=0; i<(last/2+1); i++)
        swap(cake[i], cake[last-i]);
        
    times++;
    
    last = len;
    while(cake[last-1]=='+')
        last--;
    string part = cake.substr(0,last);
    myReverse(part);
    for(int i=0; i<last; i++)
        cake[i]=part[i];
    
}


int main() {
    string cake;
    ifstream fin("B-large.in.txt");
    ofstream fout("testout2.txt");
    int n;
    fin >> n;
    for (int i=1; i<=n; i++) {
        fin >> cake;
        myReverse(cake);
        fout << "Case #" << i << ": " << times << endl;
        times = 0;
    }

}