#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <vector>
#include <set>
#include <stack>
#include <iostream>
#include <string>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
using namespace std;
int main ()
{
READ("A-small-attempt0.in");
WRITE("out.out");
int t ; 
cin >> t;
int array[4][4];
int FR,SE;
int sZ;
int res=0;
int cnt=1;
while(cnt<=t)
{
        set<int> s;
        cin>>FR;    
        for(int i=0; i<4; i++)
        {      for(int j=0;j<4 ;j++)
               {
                        cin>> array[i][j];
                        if((i+1)==FR)s.insert(array[i][j]);
                        
               }
        }
        sZ=s.size();
        cin>>SE;    
        for(int i=0; i<4; i++)
        {      for(int j=0;j<4 ;j++)
               {
                        cin>> array[i][j];
                        if((i+1)==SE)
                        {
                                     s.insert(array[i][j]);
                                     if(sZ==s.size()) res= array[i][j];
                                     else sZ=s.size();
                                                                            
                        }
                                   
               }
        }
               if(s.size()==7)
               cout <<"Case #" <<cnt<<": " <<res<<endl;
               else if (s.size()==8) cout <<"Case #" <<cnt<<": Volunteer cheated!" <<endl;
               else if (s.size()>=4 && s.size()<=6) cout <<"Case #" <<cnt<<": Bad magician!" <<endl;
              cnt++;
}


return 0;
}


