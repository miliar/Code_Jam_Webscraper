#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <string>
#include <unordered_map>
#include <queue>
#include <fstream>
using namespace std;
//#define INT_MAX 10000;

void SleepSheep(int N, int casenumber, string filename){
    if(N == 0) {
        ofstream out_file(filename,fstream::app);
        out_file << "Case #" << casenumber << ": INSOMNIA";
        out_file << endl;
        out_file.close();
        return;
    }
    bool my_array[10] {0};
    int temp = N;
    int sum=0;
    vector<int> curr_digits;
    //find digits of N
    while(temp != 0){
        int curr_digit = temp % 10;
        if(my_array[curr_digit] == 0) {
            my_array[curr_digit] = 1;
            sum+=1;
        }
        if(sum == 10) {for(int i=curr_digits.size()-1; i>=0; i--) cout << curr_digits.at(i);}
        curr_digits.push_back(temp % 10);
        temp = (temp - (temp % 10)) / 10;
    }
    //start multiplying
    vector<int> new_digits = curr_digits;
    int j=2;
    while(1){
        int length = curr_digits.size();
        int newlength = new_digits.size();
        int carry = 0;
        for(int i=0; i<length; i++){
            int add = curr_digits.at(i) + new_digits.at(i) + carry;
            new_digits.at(i) = (add) % 10;
            carry = add / 10;
            if(my_array[new_digits.at(i)] == 0){
                my_array[new_digits.at(i)] = 1;
                sum+=1;
            }
        }
        for(int i=length; i<newlength; i++){
            int add = carry + new_digits.at(i);
            new_digits.at(i) = add % 10;
            carry = add / 10;
            if(my_array[new_digits.at(i)] == 0){
                my_array[new_digits.at(i)] = 1;
                sum+=1;
            }
        }
        if(carry > 0) {new_digits.push_back(carry);
        if(my_array[carry] == 0){
            my_array[carry] = 1;
            sum+=1;
        }
        }
        if(sum == 10) {
           ofstream out_file(filename,fstream::app);
            out_file << "Case #" << casenumber << ": ";
            for(int i=new_digits.size()-1; i>=0; i--) out_file <<  new_digits.at(i);
            out_file << endl;
            out_file.close();
            return;
        }
        //cout << j << endl;
        j++;
    }
}

int NumberFlips(string curr_string){
    int size = curr_string.length();
    char first = curr_string.at(0);
    int nbflips {0};
    for(int i=1; i<size; i++){
        if(curr_string.at(i) != curr_string.at(i-1))
            nbflips++;
    }
    if(first == '+'){
        if(nbflips %2 == 0) return nbflips;
        else return nbflips+1;
    }
    else{
        if(nbflips %2 ==0) return nbflips+1;
        else return nbflips;
    }
}


int main(){
    ifstream infile;
    infile.open("test.in");
    if(infile.is_open()) cout << "Success!" << endl;
    string currline;
    string outfile = "out.txt";
    infile >> currline;
    int nbtests = stoi(currline);
    int curr_test;
    ofstream out_file(outfile);
    for(int i=1; i<=nbtests; i++){
        infile >> currline;
       //cout << currline << endl;
        //cout << curr_test << endl;
        int res = NumberFlips(currline);
        out_file << "Case #" << i << ": " << res << endl;
    }
    infile.close();
    out_file.close();
}

