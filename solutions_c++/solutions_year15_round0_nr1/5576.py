#include <iostream>
#include <cstdio>
using namespace std;

int main()
{


    int t,cas=0;
    cin >> t;
    while(t--){
        int n,counter1=0,counter2=0;
        string name;
        cin >> n;
        cin >> name;
        for(int i=0;i<n+1;i++){
            if(i-counter1>0){counter2+=i-counter1;counter1+=i-counter1;}
        	counter1+=name[i]-'0';
        }
        cout << "Case #" << ++cas<<": "<<counter2<<endl;
    }
    return 0;
}
