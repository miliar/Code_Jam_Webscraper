#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int solve(int n){
    int digitsCount = 0;
    int digits[10];
    fill_n(digits,10,-1);
    //int i = 1;
    int currN = 0;
    int lowerBit,resudial;
    while(digitsCount < 10){
        currN+=n;
        resudial = currN;
        while(resudial){
            lowerBit = resudial%10;
            if(digits[lowerBit] == -1){
                digitsCount ++;
                digits[lowerBit] = 1;
            }
            resudial = resudial/10;
        }

    }
    return currN;
}

int main()
{
    ifstream in("A-large.in");
    ofstream out("large_out.txt");
    if (! in.is_open()){
        cout << "Error opening file";
    }
    int t,n;
    in>>t;
    //vector<int> result;
    int lineCount = 1;
    while(t--){
        in>>n;
        //result.push_back(n);
        if(n==0)
            out<<"Case #"<<lineCount<<": INSOMNIA"<<endl;
        else
            out<<"Case #"<<lineCount<<": "<<solve(n)<<endl;
        lineCount ++;
    }
    //for(auto ele:result)
    //    out<<ele<<endl;
    in.close();
    out.close();
    return 0;
}
