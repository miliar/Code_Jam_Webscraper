#include<bits/stdc++.h>

using namespace std;

int main(){
    ifstream cin;
    ofstream cout;
    cin.open("C:\\Users\\PANKAJ\\Documents\\code-block-c++\\practice-for-cpp\\in.in");
    cout.open("C:\\Users\\PANKAJ\\Documents\\code-block-c++\\practice-for-cpp\\out.out");
    int T;
    cin>>T;
    int t = 1;
    while(t <= T)
    {
        int Smax;
        cin>>Smax;

        int sum = 0, required = 0;
        string SmaxArray;
        cin>>SmaxArray;

        sum = SmaxArray[0]- '0';

        for(int i = 1; i < Smax+1; i++)
        {
            if(sum < i)
            {
                required = required + i - sum;
                sum = sum + (SmaxArray[i] - '0') + i - sum;
            }
            else
                sum = sum + (SmaxArray[i] - '0');
        }
        cout <<"Case #"<<t<<": "<<required<<endl;
        t++;
    }
    return 0;
}
