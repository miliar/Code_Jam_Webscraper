#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<vector>
#include<math.h>

using namespace std;

typedef vector<long long> V_LL;

class FS{
     public:
        void ReadFile();
        ifstream RF;
        V_LL vec_b;
        V_LL vec_e;
};

void FS :: ReadFile()
{
    long long beg, end;
    int tcs;
    string str;

    RF.open("Small_Input");
    //RF.open("Large_Input");
    if(RF.is_open())
    {
       getline(RF,str);
       tcs = atoi(str.c_str());
    }

    while(tcs>0 && RF.good()){
       getline(RF,str);
       istringstream iss(str);  
       iss >> beg >> end;
       vec_b.push_back(beg);
       vec_e.push_back(end);
              tcs--;
    }
    
    ostringstream convert;
    string str_f, str_r;
    double sr;
    long long sr_I;
    long long int_part;
    for(int i=0; i<vec_b.size(); i++){
        int cnt=0;
        for(long long j=vec_b[i]; j<= vec_e[i]; j++){

            int rem = j%10;
            if(rem == 2 || rem == 3 || rem == 7 || rem == 8){
               continue;
            }

            convert << j;
            str_f = string(convert.str());
            convert.str("");

            if(str_f.at(0) != str_f.at(str_f.size()-1)){
               continue;
            }

            str_r = string(str_f.rbegin(), str_f.rend());
            if(str_f != str_r){
               continue;
            }
         
            sr = sqrt(j);
            sr_I = (long long) sr;

            if(sr_I*sr_I != j){
               continue;
            }
            
            int_part = (long long) sr;
            convert << int_part; 

            str_f = string(convert.str());
            str_r = string(str_f.rbegin(), str_f.rend());
            convert.str("");

            if(str_f != str_r){
               continue;
            }
            cnt++;
            cout << "J:" << j << endl;
        }
        cout << "Case #"<< i+1 << ": " << cnt << endl;
    }        
}

int main()
{
    FS f; 
    f.ReadFile();
    return 1;
}
