#include <iostream>
#include <fstream>


using namespace std;
/*
int main()
{
    ifstream fin("A-small-attempt1.in");
    int cases;
    fin >> cases;
    ofstream fout("solution.txt");

    for(int i=0; i<cases;i++){
        int res = -1;
        int f1, f2;
        int a1[16], a2[16];

        fin >> f1;
        for(int j=0; j<16; j++)
            fin >> a1[j];

        fin >> f2;
        for(int j=0; j<16;j++)
            fin >> a2[j];

        int num = -1;
        int cont = 0;

        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){

                if(a1[(f1-1)*4 + j] == a2[(f2-1)*4 + k]){
                    if(cont >= 1){
                        res = 3;
                    }else{
                        num = a1[(f1-1)*4 + j];
                        cont++;
                        res = 1;
                    }
                }
            }
        }

        if(num == -1) res = 2;

        fout << "Case #" << i+1 << ": ";

        switch(res){
            case 1: fout << num << endl;
                    break;
            case 2: fout << "Volunteer cheated!" << endl;
                    break;
            case 3: fout << "Bad magician!" << endl;
                    break;
            default: break;
        }

    }

    return 0;
}
*/

int main()
{
    //ifstream fin("B-small-attempt0.in");
    ifstream fin("B-large.in");
    int cases;
    fin >> cases;
    ofstream fout("solution2large.txt");


    for(int i=0; i<cases;i++){
        double c,f,x;
        fin >> c;
        fin >> f;
        fin >> x;

        double time = 0.0;
        double cookie_rate = 2.0;
        double cookies = 0.0;
        while(cookies < x){
            double n_time = c/cookie_rate;
            double c_time = x/cookie_rate;
            if(c_time > n_time){
                if(time+n_time + x/(cookie_rate+f) > time + c_time){
                    time += c_time;
                    cookies += x;
                }else{
                    time += n_time;
                    cookie_rate += f;
                }

            }else{
                time += c_time;
                cookies += x;
            }

        }
        fout << std::fixed;
        fout.precision(7);
        fout << "Case #" << i+1 << ": " << time  << endl;

    }

    return 0;
}
