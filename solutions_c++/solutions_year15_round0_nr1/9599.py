#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T,t;
    cin>>T;
    for (t = 0; t < T; t++)
    {
        int n, ar[1001];
        char c;
        cin>>n;
        for (int i=0;i<=n;i++)
        {
            cin>>c;
            ar[i] = c - '0';
        }
        int sum = 0, counter = 0;
        for (int i=0;i<=n;i++)
        {
            if (sum >= i)
                sum += ar[i];
            else
                counter += i - sum,
                sum += i-sum + ar[i];
        }
        cout<<"Case #"<< t+1 <<": "<< counter<<endl;
    }
    return 0;
}
