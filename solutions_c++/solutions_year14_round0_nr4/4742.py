#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>

#define MAX 100
#define test(a) cout << "TEST " << a << endl;
#define go(a,b) for(int a=0; a<b; a++)
#define case(a) fout << "Case #"<< a << ": " <<
using namespace std;

void display(vector<double> v){
    go(a,v.size()){
        cout << v[a] << " ";
    }
    cout << endl;
}

int war(vector<double> nam, vector<double> ken){
    //display(nam);
    //display(ken);
    if(nam.size()==0){
        return 0;
    }
    if(nam[0]>ken[ken.size()-1]){
        return ken.size();
    }
    if(ken[0]>nam[ken.size()-1]){
        return 0;
    }
    else{
        double lowest=nam[0];
        nam.erase(nam.begin()+0);
        int index;
        for(index=0; ken[index]<lowest; index++){}
        ken.erase(ken.begin()+index);
        return war(nam, ken);
    }

}

int dwar(vector<double> nam, vector<double> ken){
    //display(nam);
    //display(ken);
    if(nam.size()==0){
        return 0;
    }
    if(nam[0]>ken[ken.size()-1]){
        return 0;
    }
    if(ken[0]>nam[ken.size()-1]){
        return ken.size();
    }
    else{
        double lowest=nam[0];
        nam.erase(nam.begin()+0);
        int index;
        for(index=0; ken[index]<lowest; index++){}
        ken.erase(ken.begin()+index);
        return dwar(nam, ken)+1;
    }

}

int main()
{

    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    vector<double> nam;
    vector<double> ken;
    int n,x;
    fin >> n;
    go(a,n){
        fin >> x;
        double holder;
        go(b,x){
            fin >> holder;
            nam.push_back(holder);
        }
        go(b,x){
            fin >> holder;
            ken.push_back(holder);
        }
        sort(nam.begin(), nam.end());
        sort(ken.begin(), ken.end());
        case(a+1) dwar(ken,nam) << " "<<war(nam, ken) << endl;
        ken.resize(0);
        nam.resize(0);
    }

   }




