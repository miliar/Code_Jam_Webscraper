#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <fstream>
#include <iomanip>

using namespace std;
double a[10004];
double b[10004];
long long n;
/*
long long f(long long msk1, long long msk2)
{
 //   myfile<<msk1<<" "<<msk2<<"\n";
    long long cnt=0;
    for (long long i=0;i<n;i++){
        if ( (msk1&(1<<i)) == 0){
            cnt++;
        }
    }
    //myfile<<"cnt="<<cnt<<"\n";
    long long t=10000000;
    long long ind1=-1, ind2=-1;
    for (long long i=0;i<n;i++){
        if ((msk1&(1<<i))==0){
            ind1=i;
            break;
        }
    }
    for (long long i=0;i<n;i++){
        if ((msk2&(1<<i))==0){
            ind2=i;
            break;
        }
    }
    if (cnt==1){
        if (a[ind1]>b[ind2]){
            return 1;
        } else {
            return 0;
        }
    }
   // myfile<<"index  "<<ind1<<" "<<ind2<<"\n";
    long long temp=-1;
    for (long long i=0;i<n;i++){
        if ((msk2&(1<<i))==0){
            temp=i;
        }
    }
    if (a[ind1]<b[ind2]){
        return f(msk1|(1<<ind1), msk2|(1<<temp));
    } else {
        long long t=f(msk1|(1<<ind1), msk2|(1<<temp));
        t=max(t, 1+f(msk1|(1<<ind1), msk2|(1<<ind2)));
        return t;
    }
}
*/

long long d[1020][1020]={0};
long long fun(long long j, long long k){

    if (d[j][k]!=-1){
        //myfile<<"Asd";
        return d[j][k];
    }
    if ( k < j)
        return 0;
    long long i=n-(k-j)-1;
    if (j==k){
        if (a[i]>b[j]){
            return 1;
        } else {
            return 0;
        }
    }



    if (a[i]<b[j]){
        long long t=d[j][k]=fun(j, k-1);
        return t;
    } else {
        //myfile<<"fuckU\n";
        long long t=1+fun(j+1, k);
        t=max(t, fun(j, k-1));
        return d[j][k]=t;
    }
}

int main()
{
    ofstream myfile;;
    myfile.open("vats.txt");

    std::ifstream input("vats123.txt");
   // int a;
    long long test;
    input>>test;
    long long c=1;
    double x;




    while (test--){
        int cnt=0;
        memset(d, -1, sizeof(d));
        input >> n;
        //scanf("%d", &n);
        for (long long i=0;i<n;i++){
            input >> x;
            a[i]=x;
            //scanf("%f", &a[i]);
            cnt++;
           // myfile<<cnt<<"\n";
        }
        for (long long i=0;i<n;i++){
            //scanf("%f", &b[i]);
            input >> x;
            b[i]=x;
            cnt++;
         //   myfile<<cnt<<"\n";
        }
        sort (a, a+n);
        sort (b, b+n);
        myfile<<"Case #"<<c<<": ";
        c++;
        myfile<<fun(0, n-1)<<" ";
        long long ans2=0;
        long long visited[1010]={0};
        for (long long i=0;i<n;i++){
            double tem=-1;
            long long ind=-1;
            for (long long j=0;j<n;++j){
                if (visited[j]==0){
                    if (a[i]<b[j]){
                        if (tem==-1){
                            tem=b[j];
                            ind=j;
                        } else if (b[j]<tem){
                            tem=b[j];
                            ind=j;
                        }
                    }
                }
            }
            if (ind==-1){
                ans2++;
                for (long long i=0;i<n;i++){
                    if (visited[i]==0){
                        visited[i]=1;
                        break;
                    }
                }
            } else {
                visited[ind]=1;
            }
        }
        myfile<<ans2<<"\n";
    }
    return 0;
}
