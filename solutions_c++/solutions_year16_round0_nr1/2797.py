#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>
using namespace std;

int main(){


int T;
cin>>T;

for (int i=0;i<T;i++){
	int N;
    cin>>N;
    int arr[10];
    for (int k = 0;k<10;k++){
        arr[k]=k;
    }
    int sum=0;
    int vis[10];
    for (int k = 0;k<10;k++){
        vis[k]=0;
    }
    
    int p=0;


    for (int j=1;j<=1000000;j++){
        int number=j*N;

        int n=number;
        vector<int> digits;
        while(n){
    
        digits.push_back(n%10);
        n /= 10;
        //cout<<n<<endl;
        }
        sort(digits.begin(), digits.end());
        vector<int>::iterator it;
        it = unique(digits.begin(), digits.end());  

        digits.resize(distance(digits.begin(),it));

        for (int k=0;k<digits.size();k++){
            int d=digits[k];
            //cout<<d<<endl;
            if (vis[d]==0){
                vis[d]=1;
                sum+=1;
            }
        }  
        //cout<<sum<<endl;
        if (sum==10){
            p=number;
            break;
        }
    }
    cout<<"Case #"<<i+1<<": ";
    if (p!=0){
        cout<<p<<endl;
    }
    else{
        cout<<"INSOMNIA"<<endl;
    }

}

return 0;

}

