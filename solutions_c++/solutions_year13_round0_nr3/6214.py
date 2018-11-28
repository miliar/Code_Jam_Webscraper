/* 
 * File:   main.cpp
 * Author: Vekkiokonio
 *
 * Created on 14 aprile 2013, 0.25
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>

using namespace std;

bool fair(int x){
    string result;          // string which will contain the result
    ostringstream convert;   // stream used for the conversion
    convert << x;      // insert the textual representation of 'Number' in the characters in the stream
    result = convert.str(); // set 'Result' to the contents of the stream
    int l = result.length();
    int i = 0;
    bool flag = true;
    while (flag & i <= l/2){
        string a = result.substr(i, 1);
        string b = result.substr(l-1-i, 1);
        if (a.compare(b) != 0)
                flag = false;
        i++;
    }
    return flag;
}

bool square(int x){
    int root = sqrt(x);
    if (root*root == x)
        return fair(root);
    else
        return false;
}

int main(int argc, char** argv) {
    int n = 0;
    int test = 1;
    char num[20];
    int index = 0;
    ifstream myfile;
    ofstream output("ex3.txt");
    myfile.open("C-small-attempt0.in");
    myfile.getline(num, 5);
    while (int(num[index]) > 47 && int(num[index]) < 58){
        n = n*10 + int(num[index] - 48);
        index++;
    }
    n++;
    while (test < n){
        int a = 0;
        int b = 0;
        int count = 0;
        myfile.getline(num, 15);
        index = 0;
        while (int(num[index]) > 47 && int(num[index]) < 58){
                a = a*10 + int(num[index] - 48);
                index++;
        }
        index++;
        while (int(num[index]) > 47 && int(num[index]) < 58){
                b = b*10 + int(num[index] - 48);
                index++;
        }
        for (int i = a; i <= b; i++)
            if (fair(i) && square(i))
                count++;
        output << "Case #" << test << ": " << count << endl;
        test++;
    }
    myfile.close();
    output.close();
    return 0;   
}