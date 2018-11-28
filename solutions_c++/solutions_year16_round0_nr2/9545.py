#include <algorithm>    // std::reverse
#include <vector>       // std::vector
#include<iostream>
#include<fstream>

using namespace std;

void flip(vector<char>& rv, int k){
     //rv è il vector in cui ci sono i pancake
    // i primi k pancake sono da "flippare"

    std::reverse(rv.begin(),rv.begin() + k);
    for (int i=0;i<k;++i){
        rv[i] = (rv[i] == '+') ? '+' : '-';
    }
}


int solve(vector<char>& v){
    int count = 0; // quante flippate ho fatto
    char side = v[0];
    for (int i = 1; i < v.size();++i ){
        // finché il lato è lo stesso vado avanti
        if (side != v[i]) {
            flip(v,i-1);
            side = v[i];
            ++count;
        }
    }

    if (side=='-'){
        flip(v,v.size());
        ++count;
    }
    return count;
}

int main()
{
    ifstream INP("in");
    ofstream OUT("out");
    if(!INP || !OUT)
      cout<<"ERRORE nei FILE"<<endl;
    else {
        int T;
        INP >> T;
        cout << T << endl;

        for (int i = 0; i < T ; i++){
            vector<char> v;
            char c = INP.get();

            while (c=='\n')
                c = INP.get();

            //leggo v
            while (c!='\n' && !INP.eof()){
                //  cout << c;
                  v.push_back(c);
                  c = INP.get();
            }

            cout << "....." <<endl;

            int sol = solve(v);

            if (i+1 < T)
                OUT <<"Case #"<<i+1<<": "<<sol<<endl;
            else
                OUT <<"Case #"<<i+1<<": "<<sol;
        }

       INP.close();
       OUT.close();
    }
}
