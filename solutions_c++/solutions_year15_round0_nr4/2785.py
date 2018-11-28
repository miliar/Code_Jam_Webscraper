#include<iostream>
#include<math.h>
#include<cstring>
#include<fstream>
using namespace std;

int main()
{
    long long tc;
    ifstream infile;
    infile.open("A-large.in",ios::in);
    ofstream myfile;
    myfile.open("A-out.txt",ios::out);
    infile>>tc;
    for(long long t=1;t<=tc;t++){
                long long mx;
                infile>>mx;
                char ch[mx+1];
                infile>>ch;
                long long arr[mx+1];
                for(long long i=0;i<=mx;i++)
                    arr[i]=ch[i]-'0';

                long long sum[mx+1];
                for(long long j=0;j<=mx;j++)
                    sum[j]=0;
                    sum[0]=arr[0];

                for(long long i=1;i<=mx;i++)
                    sum[i]=(sum[i-1]+arr[i]);



                long long cnt=0;
                for(long long i=1;i<=mx;i++){

                    if((sum[i-1]+cnt)<i)
                        cnt+=(i-(sum[i-1]+cnt));

                 }
                myfile<<"Case #";myfile<<t;myfile<<": ";
                myfile<<cnt<<endl;

    }
        myfile.close();
    return 0;
}

