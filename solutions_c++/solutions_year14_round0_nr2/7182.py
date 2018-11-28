#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{

    ifstream fin;
    fin.open("B-large.in");
    ofstream fout;
    fout.open("output.txt");
    int T;
    //cin >> T;
    fin >> T;
    int i;
    long double c,f,x,time,curr_f;
    for (i=1;i<=T;i++){
        //cin >> c >> f >> x ;
        fin >> c >> f >> x ;
        curr_f=2;
        time=0;
        while(1){
            if (((x-c)/curr_f)>(x/(curr_f+f))){
                time+=(c/curr_f);
                curr_f+=f;
                }
            else {time+=(x/curr_f); break; }
            }
        //cout << setprecision(7)<<fixed;
        //cout << "Case #"<<i<<": "<<time<<endl;
        fout << setprecision(7)<<fixed;
        fout << "Case #"<<i<<": "<<time<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
