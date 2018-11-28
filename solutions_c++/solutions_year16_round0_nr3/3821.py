#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

bool is_prime(uint64_t num){
    if(num <= 3){
        return num > 1;
    }
    else if(num % 2 == 0 || num % 3 == 0){
        return false;
    }
    else{
        for (uint64_t i = 5; i * i <= num; i += 6) {
            if (num % i == 0 || num % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}

uint64_t find_divisor(uint64_t num){
    if(num <= 3){
        cout << "SHOULDNT GO HERE M8" << endl;
        return 0;
    }
    else if(num % 2 == 0){
        return 2;
    }
    else if(num % 3 == 0){
        return 3;
    }
    else{
        for (uint64_t i = 5; i * i <= num; i += 6) {
            if (num % i == 0){
                return i;
            }
            else if(num % (i + 2) == 0) {
                return i+2;
            }
        }
        cout << "SHOULDNT GO HERE M7" << endl;
        cout << num << endl;
        while(1);
        return -1;
    }
}

uint64_t mypow(uint64_t num, int top){
    uint64_t res = 1;
    for(int i=0; i<top; i++){
        res *= num;
    }
    return res;
}

uint64_t number_creator(string st, uint64_t base){
    uint64_t num = mypow(base, st.size()+1) + 1;
    for(int i=st.size()-1; i>=0; i--){
        num += (st[i]-'0') * mypow(base, st.size()-i);
    }
    return num;
}

uint64_t number_creator_normal(string st){
    uint64_t num = 0;
    //cout << st << endl;
    for(int i=st.size()-1; i>=0; i--){
        // cout << num << endl;
        num += (st[i]-'0') * mypow(10, st.size()-i-1);
    }
    return num;
}


int main(){

    set<uint64_t> primes;
    ifstream myfile("nums.txt");
    string line;
    vector<string> lines;

    //prime read
    ifstream primefile("primes.txt");

    
    while(getline(primefile, line)){
        lines.push_back(line);
    }

    for(int i=0; i<lines.size(); i++){
        primes.insert(number_creator_normal(lines[i]));
    }

    lines.clear();
    //number read
    while(getline(myfile, line)){
        lines.push_back(line);
    }

    
    int ctr = 0;
    vector<string> jamcoins;
    vector<vector<uint64_t> > divisors;
    for(int i=0; i<lines.size(); i++){
        int base;
        for(base=2; base<=10; base++){
            if(primes.find(number_creator(lines[i], base)) != primes.end()){
                break;
            }
        }
        
        if(base == 11){
            jamcoins.push_back(lines[i]);
            vector<uint64_t> divisors_cur;
            
            for(int base=2; base<=10; base++){
                divisors_cur.push_back(find_divisor(number_creator(lines[i], base)));
            }
            divisors.push_back(divisors_cur);
            ctr += 1;
        }
        if(ctr == 50){
            break;
        }
    }

    cout << "Case #1:" << endl;
    for(int i=0; i<ctr; i++){
        cout << "1" << jamcoins[i] << "1 ";
        for(int j=0; j<divisors[i].size(); j++){
            cout << divisors[i][j] << " ";
        }
        cout << endl;
    }

    // for(int i=0; i<nums.size(); i++){
    //     if(primes.find(nums[i]) != primes.end()){
    //         continue;
    //     }
    //     cout << find_divisor(nums[i]) << endl;
    // }

    //prime check
    // for(int i=0; i<nums.size(); i++){
    //     if(is_prime(nums[i])){
    //         primes.insert(nums[i]);
    //     }
    //     cout << i << endl;
    // }

    // ofstream ofile("primes.txt");

    // for(auto it=primes.begin(); it!=primes.end(); ++it){
    //     cout << *it << endl;
    // }


    return 0;

}


// lst = []
// def rf(arr):
//     if(len(arr))==14:
//         lst.append(arr)
//         return
//     rf(arr+[1])
//     rf(arr+[0])

// def main():
//     rf([])
//     print lst

//     f = open("nums.txt", "w")
//     for each in lst:
//         for l in each:
//             f.write(str(l))
//         f.write("\n")

// if __name__ == '__main__':
//     main()