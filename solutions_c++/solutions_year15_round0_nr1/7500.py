#include <iostream>
#include <fstream>

using namespace std;

void build(int table[],string suite){
    for(int i=0;i<suite.size();i++){
        table[i]=(int)suite[i]-48;
    }
    return;
}
int main()
{
    int text_cases(0);
    int shy_max(0);
    string suite("");
    ifstream enter("A-large.in");
    ofstream end("A-large.out",ios::app);
    enter>>text_cases;
    for(int i(0);i<text_cases;i++){
        enter>>shy_max;
        enter>>suite;
        int friends(0);
        int table[shy_max+1];
        build(table,suite);
        for(int j(1);j<=shy_max;j++){
            int compt(0),person_before(0);
            person_before+=friends;
            while(compt<j){
                person_before+=table[compt];
                compt++;
            }
            if(person_before<j){
                friends+=j-person_before;
            }
        }
        end << "case #"<<i+1<<": "<<friends<<endl;
    }
    return 0;
}
