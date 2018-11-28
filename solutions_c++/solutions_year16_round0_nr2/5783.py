#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool checkcake(string s);
char flip(char s);

int main(){
    
    ifstream infile;
    ofstream outfile;
    
    infile.open("B-large.in");
    outfile.open("output.txt");
    
    int t;
    string s, s1;
    int step=0;
    int index, k;
    
    infile >> t;
    
    for(int i = 0; i<t; i++){
        infile >> s;
        step = 0;
        index = 0;
        
        while(!checkcake(s)){
            
            while(index+1 < s.length() && s[index] == s[index+1]){
                index++;
            }
            
            k = index;
            s1 = s;
            
            while(index>=0){
                s[k - index] = flip(s1[index]);
                index--;
            }
            
            step++;
            index = k;
        }
        
        outfile << "CASE #" << i+1 << ": " << step << endl;
        
    }
}

bool checkcake(string s){
    
    for(int i = 0; i < s.length(); i++){
        if(s[i] == '-'){
            return false;
        }
    }
    
    return true;
}

char flip(char s){
    if(s == '+')
        return '-';
    else
        return '+';
}
