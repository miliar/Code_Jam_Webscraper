#include<iostream>

#include<string>

#include<vector>
#include<queue>

using namespace std;

int main(){
   int n;
   int m;
   cin >> n;
   for(int t=1;t<=n;t++){
      cin >> m;
      int i;
      vector<int> plates;
      int max_p=0;
      for(i=0;i<m;i++){
         int p;
         cin >> p;
         if(max_p < p){
            max_p = p;
         }
         plates.push_back(p);
      }
      int tmin = max_p;
      int j;
      for(i=1;i<max_p;i++){
         int time;
         time = 0;
         for(j=0;j<plates.size();j++){
            if(plates[j] > i){
               // Add time for moving pancakes.
               time += (plates[j]-1) / i;
            }
         }
         // Start eating.
         time += i;
         if(time < tmin){
            tmin = time;
         }
      }
      cout << "Case #" << t << ": " << tmin << '\n';
   }

   return 0;
}
