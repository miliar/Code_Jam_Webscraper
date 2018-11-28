#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include <cstring>
#include <cstdlib>
using namespace std;
long int num;
int cnt[10];
void update(int num)
{
    int dig=0;
    while(num%10!=num)
    {
        dig=num%10;
        cnt[dig]=1;
        num=num-dig;
        num=num/10;
    }
    dig=num%10;
    cnt[dig]=1;
}

int ttl()
{
    int total=0;
    for(int i=0;i<10;i++)
{
    total+=cnt[i];
}
return total;
}

int main()
{
string number,arr[110];
ifstream inp_file;
inp_file.open("question.txt");
ofstream out_file;
out_file.open("uv_ans.txt");
getline(inp_file,number);
int lim;
stringstream conver(number);
conver>>lim;
cout<<"\ntest: "<<lim<<endl;
for(int m=0;m<lim;m++)
{
getline(inp_file,arr[m]);
stringstream conver(arr[m]);
conver>>num;
cout<<num;
for(int i=0;i<10;i++)
{
    cnt[i]=0;
}
cout<<"num is: "<<num;
update(num);
int total=0;
total=ttl();
cout<<"CNT: "<<endl;
for(int i=0;i<10;i++)
{
    cout<<cnt[i]<<endl;
}
int n=2;
bool flag;
flag=false;
long int num1=0;
while(total!=10)
{
    num1=n*num;
    update(num1);
    total=ttl();
    n++;
    if(n>10000)
    {
        cout<<"INSOMNIA";
        flag=true;
        break;
    }

    //cout<<"\nnum n total: "<<num<<" "<<total;
    }

cout<<"fnum: "<<num1;
if(flag)
{
    out_file<<"Case #"<<(m+1)<<": INSOMNIA"<<"\n";
    cout<<"\nCase #"<<(m+1)<<": INSOMNIA"<<"\n";
}
else
{
    out_file<<"Case #"<<(m+1)<<": "<<num1<<"\n";
    cout<<"\nCase #"<<(m+1)<<": "<<num1<<"\n";
}



}

return 0;
}
