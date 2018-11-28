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
double a[1004];
double b[1004];
int n;
int f(int msk1, int msk2)
{
 //   myfile<<msk1<<" "<<msk2<<"\n";
    int cnt=0;
    for (int i=0;i<n;i++){
        if ( (msk1&(1<<i)) == 0){
            cnt++;
        }
    }
    //cout<<"cnt="<<cnt<<"\n";
    int t=10000000;
    int ind1=-1, ind2=-1;
    for (int i=0;i<n;i++){
        if ((msk1&(1<<i))==0){
            ind1=i;
            break;
        }
    }
    for (int i=0;i<n;i++){
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
   // cout<<"index  "<<ind1<<" "<<ind2<<"\n";
    int temp=-1;
    for (int i=0;i<n;i++){
        if ((msk2&(1<<i))==0){
            temp=i;
        }
    }
    if (a[ind1]<b[ind2]){
        return f(msk1|(1<<ind1), msk2|(1<<temp));
    } else {
        int t=f(msk1|(1<<ind1), msk2|(1<<temp));
        t=max(t, 1+f(msk1|(1<<ind1), msk2|(1<<ind2)));
        return t;
    }
}

int main()
{
    ofstream myfile;;
    myfile.open("vats.txt");
    int test;
    cin>>test;
    int c=1;
    while (test--){
        cin>>n;
        for (int i=0;i<n;i++){
            cin>>a[i];
        }
        for (int i=0;i<n;i++){
            cin>>b[i];
        }
        sort (a, a+n);
        sort (b, b+n);

       /* for (int i=0;i<n;i++){
            cout<<a[i]<<" ";
        }
        cout<<"\n";
        for (int i=0;i<n;i++){
            cout<<b[i]<<" ";
        }*/
        myfile<<"Case #"<<c<<": ";
        c++;
        myfile<<f(0, 0)<<" ";
        int ans2=0;
        int visited[1001]={0};
        for (int i=0;i<n;i++){
            double tem=-1;
            int ind=-1;
            for (int j=0;j<n;++j){
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
                for (int i=0;i<n;i++){
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
