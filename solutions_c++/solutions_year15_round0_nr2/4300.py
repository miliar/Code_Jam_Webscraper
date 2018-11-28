#include<iostream>
#include<fstream>
using namespace std;
int main(){
    int ti;
    char ch;
    int n,sum,yuan;
    int a[1000];
    int ans;
    ifstream fin;
    ofstream fout;
    fin.open("in.txt");
    fout.open("out.txt");
    fin>>ti;
    for (int i=0; i < ti; i++)
    {
        fin>>n;
        for(int j=0;j<n;j++)
            fin>>a[j];
        ans=100000;
        for(int j=1;j<1000;j++)
        {
            sum=j;
            for(int k=0;k<n;k++)
            if (a[k] % j==0) sum=sum+a[k]/j-1;else sum=sum+a[k]/j;
            if (sum<ans)ans=sum;
        }
        fout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
