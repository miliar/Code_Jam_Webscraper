#include<bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
int main()
{
    std:ios::sync_with_stdio(false);
    ifstream infile;
    ofstream outfile;
    infile.open("input.txt");
    outfile.open("output.txt");
    int T;
    //cin>>T;
    infile>>T;
    for (int i=0 ; i<T ; i++)
    {
        string s;
        //cin>>s;
        infile>>s;
        int X=s.size();
        string A;
        A=A+s[0];
        for (int j=1 ; j<X ; j++)
        {
            if(A[0]>s[j])
            {
                A=A+s[j];
            }
            else
                A=s[j]+A;
        }
        //cout<<"Case #:"<<i+1<<": "<<A<<endl;
        outfile<<"Case #"<<i+1<<": "<<A<<endl;
    }
    cout<<"Hello World\n";
}
