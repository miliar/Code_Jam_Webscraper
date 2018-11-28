#include<iostream>
#include<conio.h>
#include<vector>
#include<math.h>
#include<string>
#include<map>
using namespace std;
int main()
{
    int count = 0;
    cin>>count;
    int q = 0;
    while(q<count) {
                   cout<<"Case #"<<q+1<<": ";
                   int N,M;
                   cin>>N;
                   cin>>M;
                   vector<int> rowMax;
                   vector<int> colMax;
                   rowMax.resize(N, 0);
                   colMax.resize(M, 0);
                   vector< vector<int> > inp;
                   vector<int> rowInp;
                   for(int i =0; i<N; i++) {
                           for(int j=0; j<M; j++) {
                                   int temp;
                                   cin>>temp;
                                   rowInp.push_back(temp);
                           }
                           inp.push_back(rowInp);
                           rowInp.clear();
                   }
                   for(int i =0; i<N; i++) {
                           int max = 0;
                           for(int j =0; j<M; j++) {
                                   if(inp[i][j] > max) {
                                                max = inp[i][j];
                                   }
                           }
                           rowMax[i] = max;
                   }
                   for(int j = 0; j<M; j++) {
                           int max = 0;
                           for(int i =0; i<N;i++) {
                                   if(inp[i][j] > max) {
                                                max = inp[i][j];
                                   }
                           }
                           colMax[j] = max;
                   }
                   bool possible = true;
                   for(int i=0; i<N; i++) {
                           for(int j =0; j<M; j++) {
                                   if(inp[i][j]<rowMax[i]&&inp[i][j]<colMax[j]) {
                                                                                possible = false;
                                   }
                           }
                   }
                   if(possible) {
                                cout<<"YES";
                   } else {
                          cout<<"NO";
                   }
                   cout<<endl;
                   rowMax.clear();
                   colMax.clear();
                   q++;
    }
}
