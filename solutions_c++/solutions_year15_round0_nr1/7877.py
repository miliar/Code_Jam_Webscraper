#include<iostream>
#include<fstream>

using namespace std;
int calc(char *str,int n)
{

int i,sum=str[0]-'0',gap=0,gap_here;
for(i=1;i<=n;i++)
{
gap_here=0;
if(sum<i)
{
gap_here+=i-sum;
gap+=gap_here;
}
sum+=str[i]-'0'+gap_here;

}
return gap;
}

int main()
{
    ifstream inp;
    ofstream outp;
    inp.open("A-large.in");
    outp.open("A-large.out");
int t,i,m;
inp>>t;
for(i=0;i<t;i++)
{
inp>>m;
char arr[m+1];
inp>>arr;
outp<<"Case #"<<i+1<<": "<<calc(arr,m)<<endl;
}
inp.close();
outp.close();
}
