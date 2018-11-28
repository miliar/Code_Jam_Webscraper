#include <vector>
#include <list>
#include <map>
#include <fstream>
#include <iostream>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


using namespace std;

int play_war(vector<double> a, vector<double> b){
    int count = 0;
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    int a_iter = 0;
    int b_iter = 0;
    for (a_iter = 0;a_iter < a.size();a_iter++){
        if (a[a_iter]>b[b_iter]){
                                 count++;
                                 //a_iter++;
                                 b_iter++;
                                 }
        else {
             while (a_iter<a.size() && a[a_iter]<b[b_iter])a_iter++;
             a_iter--;
             }
        
    }
    return count;
    
}
ifstream fin("D-large.in");
ofstream fout("D-out.out");
int main(){
int t;
fin>>t;
for (int tests=0;tests<t;tests++){
int n;
fin>>n;
vector <double> first,second;
for (int i=0;i<2*n;i++){
    double temp;
    fin>>temp;
    if (i<n)first.push_back(temp);
    else second.push_back(temp);
}
fout<<"Case #"<<tests+1<<": ";
fout<<play_war(first,second)<<" ";
fout<<first.size()-play_war(second,first)<<endl;

}

//system("pause");
return 0;
}
