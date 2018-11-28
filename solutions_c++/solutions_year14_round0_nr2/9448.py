#include<iostream>
#include<string>
#include<fstream>
#include<iomanip>

using namespace std;

ifstream fin("in");
ofstream fout("out");

double
speed(int times, double F){
    return 2.0 + times * F;
}

int
solve(){
    double C, F, X;
    fin>>C>>F>>X;
    int buy = 0;
    double current_time = X/2.0;

    while(true){
        buy++;
        //cout<<"buy = "<<buy<<endl;
        double tmp_time = 0.0;
        for(int i = 0; i < buy; i++){
            //cout<<C/speed(i, F)<<endl;
            tmp_time += C/speed(i, F);
        }
        tmp_time += X/speed(buy, F);
        //cout<<C/speed(buy, F)<<endl;

        //cout<<"Current: "<<current_time<<endl;
        //cout<<"New: "<<tmp_time<<endl;

        if(current_time - tmp_time > 0.0000001){
            current_time = tmp_time;
        } else {
            break;
        }
    }
    fout<<current_time<<endl;
    return 0;
}

int
main(){
    int case_num;
    fin >> case_num;
    fout<<setprecision (10);

    for(int i = 0; i < case_num; i++){
        fout<<"Case #"<<i+1<<": ";//<<solve()<<endl;
        solve();
    }

    return 0;
}
