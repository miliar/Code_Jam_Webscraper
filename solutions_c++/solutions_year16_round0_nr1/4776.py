#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <cmath> 

using namespace std;
void digits(int n, vector<int> &temp){
    if(n == 0) return;
    temp.push_back(n%10);
    digits((n-n%10)/10,temp);

}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t, count=1, n;
    bool found=false;
    cin >> t;
    for(int q=0;q<t;q++){
        cout << "Case #" << q+1 << ": ";
        cin >> n;
        if(n == 0){
            cout << "INSOMNIA"<<endl;
            continue;
        }
        vector <int> curdigits;
        count = 1;
        while(curdigits.size() != 10){
            vector <int> temp;
            digits(count*n,temp);
            sort(temp.begin(),temp.end());
            for(int i=0;i<temp.size();i++){
                found = false;
                for(int j=0;j<curdigits.size();j++){
                    if(temp[i] == curdigits[j]) found = true;
                }
                if(!found) curdigits.push_back(temp[i]);
            }
            if(curdigits.size() == 10) cout << count*n <<endl;
            count++;     
        }
        


    }


    return 0;
}