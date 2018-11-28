#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <list>
#include <climits>
#include <fstream>

using namespace std;

const char nums[] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };


// This function multiplies x with the number represented by res[].
// res_size is size of res[] or number of digits in the number represented
// by res[]. This function uses simple school mathematics for multiplication.
// This function may value of res_size and returns the new value of res_size
int multiply(int x, int res[], int res_size)
{
    int carry = 0;  // Initialize carry

    // One by one multiply n with individual digits of res[]
    for (int i=0; i<res_size; i++)
    {
        int prod = res[i] * x + carry;
        res[i] = prod % 10;  // Store last digit of 'prod' in res[]
        carry  = prod/10;    // Put rest in carry
    }

    // Put carry in res and increase result size
    while (carry)
    {
        res[res_size] = carry%10;
        carry = carry/10;
        res_size++;
    }
    return res_size;
}

int allNumbersFound(string s, vector<char> &v){

    std::vector<char>::iterator it;

    for(int i = 0; i < s.size(); i++){

        char c = s[i];

        it = find (v.begin(), v.end(), tolower(c));
        if (it != v.end()){

            v.erase(it);
        }
    }

    return v.empty()? 1: 0;
}

// This function finds the number of sheeps
void countSheeps(int T, unsigned int n, unsigned int i, vector<char> &numv)
{
    if(!n){

        cout << "Case #" << T << ": INSOMNIA" << endl;
        return;
    }


    unsigned int num = n*i;
    string str = to_string(num);
    while(!allNumbersFound(str,numv)){

        countSheeps(T,n,i+1,numv);
        return;
    }

    cout << "Case #" << T << ": " << num << endl;
}

void getInput(vector<int> &nv){

    string line;
    int T = 0;
    int counter = 0;

    while ( std::getline(std::cin, line) && !line.empty() ){

        if(!T){ // read the T

            T = std::stoi(line);

        }else{

            if(counter < T){

                int N = std::stoi(line);
                nv.push_back(N);

                counter++;
            }
        }
    }
}

int main(){

    vector<int> tc;

    getInput(tc);

    std::ofstream out("A-small-attempt3.out");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

    for(int i = 0; i < tc.size(); i++){

        int num_size = 10;
        vector<char> l;
        for(int k = 0; k < num_size; k++)
            l.push_back(nums[k]);

        countSheeps(i+1,tc[i],1,l);
    }

    return 0;
}
