#include <iostream>
#include <fstream>
#include <cstdlib>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

int justBigger(vector<double> in, double n);

int main()
{
    std::ifstream in("D-large.in");
    std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

    std::ofstream out("out.txt");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

    int ncase;
    cin >> ncase;

    for(int i = 1; i<= ncase; i++){
        //getline(infile, line);
        int n;
        cin >> n;

        vector<double> nao(n, 0.0);
        vector<double> ken(n, 0.0);

        for(int j=0;j<n;j++) cin >> nao[j];
        for(int j=0;j<n;j++) cin >> ken[j];

        int ans1 = 0, ans2 = 0;
        sort(nao.begin(), nao.end());
        sort(ken.begin(), ken.end());//asscending

//        for(int j=0;j<n;j++) cout << nao[j] << ' ';
//        cout << endl;
//        for(int j=0;j<n;j++) cout << ken[j] << ' ';
//        cout << endl;
        //solve part 1
        vector<double> nao_copy(nao);
        vector<double> ken_copy(ken);

        for(int j=0;j<n;j++){
            if(nao_copy.back() < ken_copy.back()){ //must lose, use smallest to lose
                nao_copy.erase(nao_copy.begin());
                ken_copy.pop_back();
            }
            else{ //win
                nao_copy.pop_back();
                ken_copy.pop_back();
                ans1++;
            }
//            for(int k=0;k<n;k++) cout << nao[k] << ' ';
//            cout << endl;
//            for(int k=0;k<n;k++) cout << ken[k] << ' ';
//            cout << endl;
        }
        //ans1 = n - ans1;
        //cout << "ans1: " << ans1 << endl;


        for(int j=0;j<n;j++){
            if(nao[0] > ken.back()) break;

            int loc = justBigger(ken, nao[0]);
            //for(int k=0;k<n;k++) cout << nao[k] << ' ';
            //cout << endl;
            //cout << "size: " << nao.size() << "here2\n";
            nao.erase(nao.begin());
            //cout << "here3\n";
            ken.erase(ken.begin() + loc);

//            for(int k=0;k<nao.size();k++) cout << nao[k] << ' ';
//            cout << endl;
//            for(int k=0;k<ken.size();k++) cout << ken[k] << ' ';
//            cout << endl;
        }
        ans2 = nao.size();
        //char c[500];
        //sprintf(c, "Case #%d: %d %.7f\n", i, fnf, answer);
        //cout << c;

        cout << "Case #" << i << ": "  << ans1 << ' ' << ans2 << endl;
    }

    return 0;
}


int justBigger(vector<double> in, double n){
    vector<double>::iterator result = in.begin();
    int i;
    for(i=0;i<in.size();i++){
        //cout << *result << ' ' << n << endl;
        if(*result > n) break;
        else result++;
    }
    //cout << "going to return..";
    return i;
}
