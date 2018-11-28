#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream fin("A-large.in");
    ofstream fout("output-large.txt");
    int T, n, m1, m2, temp;
    int s[26];
    fin >> T;
    for(int i = 0; i < T; i++) {
        m1 = 0;
        m2 = 1;
        fin >> n;
        fin >> s[0];
        fin >> s[1];
        if(s[0] > s[1]){
            m1 = 0; m2 = 1;
        }
        else{
            m1 = 1; m2 = 0;
        }
        for(int j = 2; j < n; j++){
            fin >> s[j];
            //set max and second max
            if(s[j] > s[m2]){
                m2 = j;
                if(s[j] > s[m1]){
                    m2 = m1;
                    m1 = j;
                }
            }
        }

        fout << "Case #" << i+1 << ": ";

        temp = s[m1] - s[m2];
        if(temp){
            for(int k = 0; k < (temp/2); k++){
                fout << (char) (65 + m1) << (char) (65 + m1) << " ";
            }
            if(temp%2){
                fout << (char) (65 + m1) << " ";
            }
        }
        for(int l = 0; l < n; l++){
            temp = s[l];
            if((l!=m1)&&(l!=m2)){
                for(int k = 0; k < (temp/2); k++){
                    fout << (char) (65 + l) << (char) (65 + l) << " ";
                }
                if(temp%2){
                    fout << (char) (65 + l) << " ";
                }
            }
        }
        temp = s[m2];
        for(int m = 0; m < temp; m++){
            fout << (char) (65 + m1) << (char) (65 + m2);
            if(m < (temp - 1)) fout << " ";
        }
        fout << "\n";
    }
    return 0;
}
