#include <fstream>
#include <vector>
#include <cassert>
#include <iostream>
#include <algorithm>

#define EPS 1e-6

using namespace std;

ifstream fin("D-large.in");
ofstream fout("warout.txt");
ifstream testFin("warin.txt");

double abs(double a);
bool isGreater(double a, double b);
bool isEqual(double a, double b);
int war(vector<double>* naomi, vector<double>* ken);
void test(void);
int deciet(vector<double>* naomi, vector<double>* ken);

int main(int argc, char* argv[]){
    int t;
    fin >> t;
    test();
    //loops over all cases
    for(int i = 0; i < t; i++){
        vector<double> ken,naomi;
        int n;
        fin >> n;
        
        //reads in naomi's set
        for(int j = 0; j < n; j++){
            double temp;
            fin >> temp;
            naomi.push_back(temp);
        }
        
        //reads in ken's set
        for(int j = 0; j < n; j++){
            double temp;
            fin >> temp;
            ken.push_back(temp);
        }
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        fout << "Case #" << i+1 << ": " << deciet(&naomi,&ken) << ' ' << war(&naomi,&ken) << '\n';
    }
    testFin.close();
    fin.close();
    fout.close();
    return 0;
}

double abs(double a){
    //returns the absolute value
    if(isGreater(a,0)) return a;
    return 0 - a;
}

bool isGreater(double a, double b){
    return a > b + EPS;
}

bool isEqual(double a, double b){
    return abs(a - b) < EPS;
}

int war(vector<double>* naomi, vector<double>* ken){
    
    //Calculates the points naomi will get if she plays war optimally
    int kenFront = ken -> size() - 1, kenBack = 0;
    int score = 0;
    
    for(int naomiFront = naomi -> size() - 1; naomiFront >= 0 ; naomiFront--){
        if(isGreater(naomi -> at(naomiFront), ken -> at(kenFront))){
            score++;
            kenBack++;
        }else{
            kenFront--;
        }
    }
    return score;
}

int deciet(vector<double>* naomi, vector<double>* ken){
    
    //Calculates the points naomi will get if she plays decietful war optimally
     
    
    return naomi -> size() - war(ken,naomi);
}

void test(void){
    int t;
    testFin >> t;
    //loops over all cases
    for(int i = 0; i < t; i++){
        vector<double> ken,naomi;
        int n;
        testFin >> n;
        
        //reads in naomi's set
        for(int j = 0; j < n; j++){
            double temp;
            testFin >> temp;
            naomi.push_back(temp);
        }
        
        //reads in ken's set
        for(int j = 0; j < n; j++){
            double temp;
            testFin >> temp;
            ken.push_back(temp);
        }
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        switch(i){
            case 0:
                cout << "case 0" << endl;
                assert(war(&naomi,&ken) == 0);
                assert(deciet(&naomi,&ken) == 0);
                break;
            case 1:
                cout << "case 1" << endl;
                assert(war(&naomi,&ken) == 0);
                assert(deciet(&naomi,&ken) == 1);
                break;
            case 2:
                cout << "case 2" << endl;
                assert(war(&naomi,&ken) == 1);
                assert(deciet(&naomi,&ken) == 2);
                break;
            default:
                cout << "case 3" << endl;
                assert(war(&naomi,&ken) == 4);
                assert(deciet(&naomi,&ken) == 8);
        }
    }
    cout << "All tests passed. You are awesome!" << endl;
    return;
}
