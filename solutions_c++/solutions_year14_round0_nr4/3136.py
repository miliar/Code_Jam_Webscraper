#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
   ifstream fin("D-large.in");
   ofstream fout("D-largeans.out");

   int N, T, point1, point2, point1a, point2a, war=0, dwar=0;
   double temp;
   vector<double> a, b;
   fin >> N;
   for(int i=0; i<N; i++){
     war=0;
     dwar=0;
     a.clear();
     b.clear();
     fin >> T;
     for(int j=0; j<T; j++){
        fin >> temp;
        //cout << temp << endl;
        a.push_back(temp);
     }
     for(int j=0; j<T; j++){
        fin >> temp;
        b.push_back(temp);
     }
     sort(a.begin(), a.end());
     sort(b.begin(), b.end());
     /*for(int q=0; q<T; q++){
        cout << a.at(q) << " " << b.at(q) << endl;
     }*/
     point1=T-1;
     point2=T-1;
     while(point1>=0){
       if(a.at(point1)>b.at(point2)){
         war++;
         point1--;
       }
       else{
         point1--;
         point2--;
       }
     }
     point1a=0;
     point2a=0;
     while(point1a<T){
       if(a.at(point1a)>b.at(point2a)){
         dwar++;
         point1a++;
         point2a++;
       }
       else{
         point1a++;
       }
     }
     fout << "Case #" << i+1 << ": " << dwar << " " << war << endl;
   }

   return 0;
}
