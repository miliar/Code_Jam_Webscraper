#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream in("war.in");
ofstream out("war.out");

int rezDeceitful(vector<double> naomi, vector<double> ken){
    int last = naomi.size()-1;
    if(last == -1){
        return 0 ;
    }
    if(naomi[last]>ken[last]){
        naomi.erase(naomi.begin()+last);
        ken.erase(ken.begin()+last);
        return 1+ rezDeceitful(naomi, ken);
    } else {
        naomi.erase(naomi.begin()+0);
        ken.erase(ken.begin()+last);
        return rezDeceitful(naomi, ken);
    }
}
int rezNormal(vector<double> naomi, vector<double> ken){
    int rez = 0;
    for(int i = 0 ; i < naomi.size(); i++){
        double kenChose = 0;
        for(int j=0; j<ken.size();j++){
            if(ken[j]>naomi[i]){
                kenChose = ken[j];
                ken.erase(ken.begin()+j);
                break;
            }
        }
        if(kenChose == 0){
            rez++;
        }
    }
    return rez;
}

void solve(int test){

    int nrPiese;
    in>>nrPiese;

    vector<double> naomi;
    vector<double> ken;

    for(int i=1;i<=nrPiese;i++){
        double x;
        in>>x;
        naomi.push_back(x);
    }
    for(int i=1;i<=nrPiese;i++){
        double x;
        in>>x;
        ken.push_back(x);
    }

    sort(naomi.begin(),naomi.end());
    sort(ken.begin(),ken.end());

    out<<"Case #"<<test<<": ";
    vector<double> naomiClone = naomi ;
    vector<double> kenClone = ken;

    out<<rezDeceitful(naomi,ken)<<" "<<rezNormal(naomi,ken);
    out<<"\n";

}

int main()
{
    int teste;
    in>>teste;
    for(int i=1;i<=teste;i++){
        solve(i);
    }
    return 0;
}
