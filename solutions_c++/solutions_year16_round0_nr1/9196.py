#include <iostream>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
using namespace std;

bool check [10];
int N;
int main()
{
ifstream fin ("A-large.in");
 ofstream fout("outputttt.out");
    int t; fin >> t;
for(int tc = 1; tc <= t; tc++) {
   for(int i=0; i < 10;  i++)
      check[i] =0;
    fin>> N ;

    //int N=0;
    int N_mult ;

    if (N==0 ){
     fout << "Case #" << tc << ": " << "INSOMNIA"<< endl;
     continue ;}
//    cout <<"Enter a number";
   // cin >> N;
    for (int i=1 ; i<1000000000000000 ;i++){
        N_mult = N*i;
        std ::stringstream ss;
        ss << N_mult;
        string str = ss.str();
        for(int j = 0; j < str.length(); j++) {
            char c = str[j];
            int x = c - '0';
            check[x]=true ;
        }
        bool b = 1;
        for (int j =0 ;j<10;j++){
            if (check[j]==false){
               b = 0;
               break;
            }
        }
        if(b){
      //  cout << N*i ;
          fout << "Case #" << tc << ": " << N*i<< endl;
            break;
        }
        }
}
 fin.close();
    fout.close();
return 0;


}
