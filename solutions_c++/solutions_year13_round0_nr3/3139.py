//Fair and Square by Shintero
#include<iostream>
#include<cstdio>
#include<vector>
#include<cmath>
#include<string>
using namespace std;

int TAB[5]={1, 4, 9, 121, 484};
int N, a, b, ile;

int main()
{
ios_base::sync_with_stdio(0);
cin >> N;
for(int i=1; i<=N; i++)
   {ile=0;
   cin >> a >> b; 
   for(int j=0; j<5; j++)
      if(TAB[j]>=a && b>=TAB[j])
         ile++;
   cout << "Case #" << i << ": " << ile << endl;}
return 0;   
}
