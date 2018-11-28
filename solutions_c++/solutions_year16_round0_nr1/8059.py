#include<iostream>
#include<fstream>
using namespace std;
 ifstream fin;

    ofstream fout;
int check(int n);
int count=0;
int a[10];
int k,nfix;
void fil(int n)
{
        int n1=n;
        int r;
        k=0;
        while(n)
    {
        r=n%10;
        a[r]++;
        n=n/10;
    }
    for(int i=0;i<10;i++)
    {
        if(a[i]<1)
        {
            k=1;

            break;
        }
       // else

    }
    //cout<<k;
    if(k==1){

    //cout<<n1+nfix;
     check(n1+nfix);
    }
     else{
        fout<<"\nCase #"<<++count<<": "<<n1;
}
}
int check(int n)
{

    //int n1=n;
//int r,d;
    fil(n);


}
int main()
{
    int t,n; fin.open("input.in");

    fout.open("output.txt");
    fin>>t;//cout<<"\n";
    for(int i=0;i<t;i++)
    {
   //cout<<"\n";
        fin>>n;
       if(n==0)
        fout<<"Case #"<<++count<<": "<<"INSOMNIA";
       else {
       for(int h=0;h<10;h++)
        a[h]=0;
       // cout<<"\n";
      /*  for(int k=0;k<10;k++)
    {
        cout<<a[k]<<" ";
    }*/
        nfix=n;
      //  cout<<nfix;
        check(n);
    }
    }
    return 0;
}
