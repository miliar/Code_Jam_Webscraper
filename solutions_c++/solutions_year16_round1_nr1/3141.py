#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>
#include <deque>
#include <math.h>

using namespace std;






int main(){
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);

int T;
cin>>T;


for (int i=0;i<T;i++){
    cout<<"Case #"<<i+1<<": ";
    string S;
    cin>>S;
    string sol="";
    for (int i=0;i<S.length();i++){
        char a=S.at(i);
        if (sol.length()==0){
            sol+=a;
        }
        else{
            int first=(int)sol.at(0);
            int asc=(int)a;
            if(asc>=first){
                sol=a+sol;
            }
            else{
                sol=sol+a;
            }
        }
    }

    cout<<sol<<endl;
















    
}

return 0;

}

