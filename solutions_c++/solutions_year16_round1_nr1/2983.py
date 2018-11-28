#include <iostream>
#include <string>
using namespace std;

char buffer[3000];
void solve(int position, string &cad)
{
    int start = 1500;
    int finish = start;
    for(int i=0;i<(int)cad.length();i++)
    {
        if(i>0 && cad[i]>=buffer[start])
        {
            start--;
            buffer[start] = cad[i];
        }
        else
        {
            buffer[finish] = cad[i];
            finish++;
        }
    }
    buffer[finish] = 0;
    cout<<"Case #"<<position<<": "<<&buffer[start]<<endl;
}

int main()
{
    string cad;
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>cad;
        solve(i+1, cad);
    }
    return 0;
}
