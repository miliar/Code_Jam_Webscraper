#include <iostream>
#include <fstream>
#include <set>

#define LL long long int

using namespace std;

LL GetLastNum(LL num){
    LL i=1;
    set<int> rem_digits;
    rem_digits.insert(0);
    rem_digits.insert(2);
    rem_digits.insert(3);
    rem_digits.insert(4);
    rem_digits.insert(5);
    rem_digits.insert(6);
    rem_digits.insert(7);
    rem_digits.insert(8);
    rem_digits.insert(9);
    rem_digits.insert(1);
    set<LL> num_processed;
    while(1){
        LL current_num = i*num;
        if(current_num < 0){
        return -1;
        }
        else if(num_processed.find(current_num) != num_processed.end()){
        return -1;
        }
        num_processed.insert(current_num);
        LL temp = current_num;

        do{
            int digit  = (temp%10);
            if(rem_digits.find(digit)!= rem_digits.end()){
                rem_digits.erase(digit);
            }
            temp/=10;
        }while(temp);
        if(rem_digits.empty()){
            return current_num;
        }
        i++;
    }
    return -1;
}
int main(){
    ifstream inp;
    inp.open("A-large.in");
    ofstream out;
    out.open("codejam_out.txt");
    int num_tests = 0;
    inp >> num_tests;
    for(int t =1; t<= num_tests; t++){
        LL num = 0;
        inp >> num;

        LL last_num = GetLastNum(num);
        out << "Case #" << t << ": ";
        if(last_num<0){
            out << "INSOMNIA\n";
        }
        else{
            out <<last_num<<"\n";
        }
    }
    inp.close();
    out.close();
    return 0;
}
