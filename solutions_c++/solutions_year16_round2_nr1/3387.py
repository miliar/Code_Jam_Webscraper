#include <algorithm>    // std::reverse
#include <vector>       // std::vector
#include<iostream>
#include<fstream>

using namespace std;
using namespace std;

void rimuovi(vector<char>& v, const char* parola, int dim){
    for (int i =0; i<dim; ++i){
        vector<char>::iterator it = find(v.begin(),v.end(),parola[i]);
        v.erase(it);
    }
}

void solve1(vector<char>& v, int* sol,int num,char lt, const char* parola, int dim){
    while (std::find(v.begin(),v.end(),lt) != v.end()){
        //remove parola da v
        rimuovi(v,parola,dim);
        //incremento di 1 sol[num]
        sol[num] = sol[num] + 1;
    }
}

void solve(vector<char>& v, int* sol){
// 0Z 2W 6X 8G
    if (!v.empty())
        solve1(v,sol,0,'Z',"ZERO",4);
    if (!v.empty())
        solve1(v,sol,2,'W',"TWO",3);
    if (!v.empty())
        solve1(v,sol,6,'X',"SIX",3);
    if (!v.empty())
        solve1(v,sol,8,'G',"EIGHT",5);

// 3H 4R
    if (!v.empty())
        solve1(v,sol,3,'H',"THREE",5);
    if (!v.empty())
        solve1(v,sol,4,'R',"FOUR",4);

// 1O 5F
    if (!v.empty())
        solve1(v,sol,1,'O',"ONE",3);
    if (!v.empty())
        solve1(v,sol,5,'F',"FIVE",4);

// 7S 9N
    if (!v.empty())
        solve1(v,sol,7,'S',"SEVEN",5);
    if (!v.empty())
        solve1(v,sol,9,'N',"NINE",4);
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

        for (int i = 0; i < T ; i++){
            vector<char> v;
            char c = INP.get();

            while (c=='\n')
                c = INP.get();

            //leggo v
            while (c!='\n' && !INP.eof()){
                  v.push_back(c);
                  c = INP.get();
            }

            int sol[10] = {0};

            solve(v,sol);

            if (i+1 < T){
                OUT <<"Case #"<<i+1<<": ";
                for (int i=0;i<10;++i){
                    while (sol[i] > 0){
                        OUT << i;
                        sol[i] = sol[i] - 1;
                    }
                }
                OUT<<endl;
            }else{
                OUT <<"Case #"<<i+1<<": ";
                for (int i=0;i<10;++i){
                    while (sol[i] > 0){
                        OUT << i;
                        sol[i] = sol[i] - 1;
                    }
                }
            }
        }

       INP.close();
       OUT.close();
    }
}
