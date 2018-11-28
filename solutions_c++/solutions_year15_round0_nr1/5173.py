#include<iostream>
#include<fstream>
using namespace std;
int main(){
    int ti;
    char ch;
    int n,sum,yuan;
    int a[1000];
    ifstream fin;
    ofstream fout;
    fin.open("in.txt");
    fout.open("out.txt");
    fin>>ti;
    for (int i=0; i < ti; i++)
    {
        fin>>n;fin.get(ch);
        for (int j=0;j<n+1;j++)
        {
            fin.get(ch);
            a[j]=(int)ch-'0';

        }
        sum=a[0];
        yuan=a[0];
        for (int j=1;j<n+1;j++)
        {
            yuan+=a[j];
            if (j>sum) sum=j+a[j];
            else sum=sum+a[j];
        }
        fout<<"Case #"<<i+1<<": "<<sum-yuan<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
