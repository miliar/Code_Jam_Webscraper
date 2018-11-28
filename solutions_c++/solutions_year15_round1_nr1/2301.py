#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream fout("key.txt", ios::out);
    ifstream fin("inl.txt", ios::in);
    int T, n;
    int num[10002];
    fin>>T;
    int i=1;
    while(T--)
    {
        fin>>n;
        for(int i=0; i<n; i++)
        {
            fin>>num[i];
            cout<<num[i]<<" ";
        }
        cout<<endl;
        int y=0;
        for(int i=1; i<n; i++)
        {
            if(num[i-1] > num[i])
                y+=num[i-1]-num[i];
        }
        int z=0;
        int diff=0;
        for(int i=1; i<n; i++)
        {
            diff=max(num[i-1]-num[i],diff);
        }
        cout<<diff<<endl;
        for(int i=0; i<n-1; i++)
        {
            z+=min(diff, num[i]);
        }
        //if(z > num[n-1])
        //z=z-num[n-1];
        fout<<"Case #"<<i<<": "<<y<<" "<<z<<endl;
        i++;
    }
    fout.close();
    fin.close();
    return 0;
}
