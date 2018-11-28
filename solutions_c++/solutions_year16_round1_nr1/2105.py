#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<queue>
using namespace std;


int main() {

    long long int n;
    cin>>n;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    for(long long int i=0;i<n;i++)
        {
        char a[1000],x[100000],flag;
        cin>>a;
               long long int c=1000,p=1001;
        x[c]=a[0];
        flag=a[0];
        for(long long int j=1;a[j]!='\0';j++)
            {
            if(a[j]>=flag)
                {
                    c--;
                    x[c]=a[j];
                flag=x[c];
                //printf("%lld %c",c,x[c]);

                }
            else
                {

                    x[p]=a[j];

               //printf("%lld %c",p,x[j]);
                    p++;
                }



        }
        cout<<"Case #"<<i+1<<": ";
        for(long long int j=c;j<p;j++)
            printf("%c",x[j]);
            cout<<"\n";
    }



    return 0;
}
