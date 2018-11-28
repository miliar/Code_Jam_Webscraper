#include <iostream>
#include <string>

using namespace std;

int main(void)
{
    int T;
    cin>>T;
    for (int t = 1; t <= T; t++)
    {
        int K, C, S;
        cin>>K;
        cin>>C;
        cin>>S;
        string result = "";
        for (int i=1; i <= K; i++)
            result += to_string(i) + " ";
        cout<<"Case #"<<t<<": "<<result<<endl;
    }
}
