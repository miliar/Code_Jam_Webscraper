#include <fstream>
#include<bits/stdc++.h>

using namespace std;


long long int checkprime(long long int n){
    if (n == 2)
        return 0;
    if (n == 3)
        return 0;
    if (n % 2 == 0)
        return 2;
    if (n % 3 == 0)
        return 3;
    long long int i,w;
    i = 5;
    w = 2;
    while(i * i <= n){
        if (n % i == 0)
            return i;
        i += w;
        w = 6 - w;
    }
    return 0;
}

long long int power[9][16]={{1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768}
,{1,3,9,27,81,243,729,2187,6561,19683,59049,177147,531441,1594323,4782969,14348907}
,{1,4,16,64,256,1024,4096,16384,65536,262144,1048576,4194304,16777216,67108864,268435456,1073741824}
,{1,5,25,125,625,3125,15625,78125,390625,1953125,9765625,48828125,244140625,1220703125,6103515625,30517578125}
,{1,6,36,216,1296,7776,46656,279936,1679616,10077696,60466176,362797056,2176782336,13060694016,78364164096,470184984576}
,{1,7,49,343,2401,16807,117649,823543,5764801,40353607,282475249,1977326743,13841287201,96889010407,678223072849,4747561509943}
,{1,8,64,512,4096,32768,262144,2097152,16777216,134217728,1073741824,8589934592,68719476736,549755813888,4398046511104,35184372088832}
,{1,9,81,729,6561,59049,531441,4782969,43046721,387420489,3486784401,31381059609,282429536481,2541865828329,22876792454961,205891132094649}
,{1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000,100000000000,1000000000000,10000000000000,100000000000000,1000000000000000}};

long long int converttobase(string s,int b)
{
    long long int n=0;
    for(int i=s.size()-1,j=0;i>=0;i--,j++)
        if(s[i]=='1')
        n+=power[b-2][j];
    return n;
}
int main()
{
    fstream fin;
    fstream fout;
    fin.open("input.in",ios::in);
    fout.open("output.out",ios::out);
    int n,j;
    fin>>n;
    fin>>n>>j;
    string s(n,'0');
    s[0]='1';
    s[n-1]='1';
    int count=0,i;
    long long int num;
    long long int a[11];
    bool flag;
    fout<<"Case #1:\n";
    while(count<j)
    {
        flag=true;
        for(i=2;i<=10;i++)
        {
            num=converttobase(s,i);
            a[i]=checkprime(num);
            if(a[i]==0){
                flag=false;
                break;
            }
        }
        if(flag==false)
        {
            num=converttobase(s,2);
            num+=2;
            s =bitset<16>(num).to_string();
            continue;
        }
        fout<<s<<" ";
        for(int i=2;i<=10;i++)
            fout<<a[i]<<" ";
        fout<<endl;
        num=converttobase(s,2);
        num+=2;
        s = bitset<16>(num).to_string();
        count++;
    }

    return 0;
}
