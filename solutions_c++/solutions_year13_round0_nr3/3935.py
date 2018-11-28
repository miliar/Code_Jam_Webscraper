#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<fstream>
#include<cmath>
#include<string>
bool cp(int p)
{
    int i,c=0,r,s=0;
    int temp=p;
    while(temp)
    {
        temp=temp/10;
        c++;
    }
    temp=p;
    while(temp && c>=0)
    {
        r=temp%10;
        s+=r*(int(pow(10.0,c-1)));
        temp=temp/10;
        c--;
    }
    if(s==p)
    {
        return true;
    }
    else
        return false;
}
using namespace std;
int main()
{
    int n,m;
    string s;
    ifstream fin;
    ofstream fout;
    fin.open("cji3.txt");
    fout.open("cjo3.txt");
    int t,i,j,flag=0,temp;
    fin>>t;
    getline(fin,s);
    for(j=0;j<t;j++)
    {
        flag=0;
        fin>>n>>m;
        getline(fin,s);
        for(i=n;i<=m;i++)
        {
            temp=int(sqrt(float(i)));

            if(temp*temp==i && cp(temp) && cp(i))
            {
                flag++;
            }
        }
        fout<<"Case #"<<j+1<<": "<<flag<<endl;
    }
    fout.close();

}
