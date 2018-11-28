/* 
 * File:   main.cpp
 * Author: Timo
 *
 * Created on 9. huhtikuutata 2016, 21:21
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

    char uniqs[] = "ZWUXG";
    string uniq_digs[] = {"ZERO", "TWO", "FOUR", "SIX", "EIGHT"};
    int uniq_digis[] = {0, 2, 4, 6, 8};
    
    string _digs[] = {"ONE", "THREE", "FIVE", "SEVEN", "NINE"};
    int _digis[] = {1, 3, 5, 7, 9};
    
    std::vector<int> found_digits(10,0);
    
    bool search( std::vector<int> histo, std::vector<int> foo) {
        bool zero = true;
        for(int i=0; i<histo.size(); ++i) {
            if(histo[i] < 0) return false;
            if(histo[i]> 0) zero = false;
        }
        if(zero) {
            found_digits = foo;
            return true;
        }
        
        for(int i=0; i<5; ++i) {
            std::vector<int> histo_ = histo;
            std::vector<int>    foo_ = foo;
            foo_[_digis[i]]++;
            for(int j=0; j<_digs[i].size(); ++j) {
                histo_[(unsigned char) (_digs[i][j]-'A')]--;
                if(histo_[(unsigned char) (_digs[i][j]-'A')] < 0) continue;
            }
                if(search(histo_, foo_)) return true;
        }
    }
    
/*
 * 
 */
int main(int argc, char** argv) {
    //ifstream ifs("input.txt");
    ifstream ifs("A-large.in");
    //ifstream ifs("D-small-attempt3.in");
    //ifstream ifs("D-large.in");
    ofstream ofs("output.txt");
    
    int T;
    ifs >> T;
    ifs >> ws;
    
    
    for(int test=1; test<=T; test++) {
        ofs << "Case #" << test << ": ";
        cout << "Case #" << test << ": ";
        
        
        string line;
        getline(ifs,line);
        std::vector<int> histo(30,0);
        std::vector<int> digits(10,0);
       
        
        //cout << line << endl;
        for(int i=0; i<line.size(); ++i) {
            //cout << (int)(unsigned char)(line[i]-'A') << endl; cout.flush();
            histo[(unsigned char)(line[i]-'A')]++;
        }
            //cout << "!!" << endl; cout.flush();
        
        for(int i=0; i<5; ++i) {
            //cout << uniqs[i] << endl; cout.flush();
            int foo = histo[(unsigned char)(uniqs[i]-'A')];
            //cout << foo << endl; cout.flush();
            digits[uniq_digis[i]] += foo;
            
            for(int j=0; j<uniq_digs[i].size(); ++j) {
                histo[(unsigned char)(uniq_digs[i][j]-'A')] -= foo;
            }
        }
        
        /*for(int i=0; i<10; ++i) {
            for(int j=0; j<digits[i]; j++) {
                cout << i;
            }
        }
        cout << endl;
        cout << search(histo, digits) << endl;*/
        search(histo, digits);
        //found_digits = digits;
        for(int i=0; i<10; ++i) {
            for(int j=0; j<found_digits[i]; j++) {
                cout << i;
                ofs << i;
            }
            //cout << digits[i]<< " " << endl;
        }
        cout << endl;
        ofs << endl;
        
        continue;
        
        int K,C,S;
        ifs >> K >> C >> S;
        
        if(K > C*S) {
            ofs << " IMPOSSIBLE" << endl;
            cout << " IMPOSSIBLE" << endl;
            continue;
        }
        
        int foo = C;
        //while((foo-1)*C >= K)
        //    foo--;
        int j=0;
        long long i=0;
        while(true) {
            long long val = 0;
            for(int j=0; j<foo; ++j) {
                val *= K;
                val += i;
                i++;
                if(i>=K) break;
            }
            ofs << " " << (val+1);
            cout << " " << (val+1);
            j++;
            if(j>S) {cout << endl; cout << C << " " << i << " " << S << endl; cout.flush();throw;};
            if(i>=K) break;
        }
        ofs << endl;
        cout << endl;
    }
    
    return 0;
}

